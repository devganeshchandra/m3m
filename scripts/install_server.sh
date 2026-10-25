#!/usr/bin/env bash
# Put the site online on an Ubuntu/Debian server: Gunicorn as a systemd
# service behind Nginx, with optional free HTTPS from Let's Encrypt.
#
#   sudo ./scripts/install_server.sh www.m3mindia.com
#
# Run ./scripts/setup.sh --production --domain <domain> first.
set -euo pipefail

DOMAIN="${1:?Usage: sudo ./scripts/install_server.sh www.m3mindia.com}"
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
SERVICE="m3m"
APP_USER="${SUDO_USER:-$(whoami)}"
PORT="${PORT:-8000}"

if [[ $EUID -ne 0 ]]; then
  echo "Please run with sudo." >&2
  exit 1
fi
if [[ ! -x "$ROOT/.venv/bin/gunicorn" ]]; then
  echo "Gunicorn not found. Run ./scripts/setup.sh --production --domain $DOMAIN first." >&2
  exit 1
fi

bare="${DOMAIN#www.}"
if [[ "$bare" == "$DOMAIN" ]]; then SERVER_NAMES="$DOMAIN"; else SERVER_NAMES="$bare $DOMAIN"; fi

echo "==> Installing Nginx"
apt-get update
apt-get install -y nginx

echo "==> Creating the $SERVICE service (runs as $APP_USER)"
cat > "/etc/systemd/system/$SERVICE.service" <<EOF
[Unit]
Description=M3M India website (Gunicorn)
After=network.target

[Service]
User=$APP_USER
Group=$APP_USER
WorkingDirectory=$ROOT
EnvironmentFile=$ROOT/.env
ExecStart=$ROOT/.venv/bin/gunicorn config.wsgi:application --bind 127.0.0.1:$PORT --workers 3 --timeout 60 --access-logfile - --error-logfile -
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable --now "$SERVICE"
systemctl restart "$SERVICE"

echo "==> Configuring Nginx for $SERVER_NAMES"
cat > "/etc/nginx/sites-available/$SERVICE" <<EOF
server {
    listen 80;
    server_name $SERVER_NAMES;

    # Allow large image and brochure uploads from the admin.
    client_max_body_size 30M;

    location / {
        proxy_pass http://127.0.0.1:$PORT;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_read_timeout 60s;
    }
}
EOF
ln -sf "/etc/nginx/sites-available/$SERVICE" "/etc/nginx/sites-enabled/$SERVICE"
rm -f /etc/nginx/sites-enabled/default
nginx -t
systemctl reload nginx

if command -v ufw >/dev/null 2>&1 && ufw status | grep -q "Status: active"; then
  ufw allow 'Nginx Full'
fi

echo
read -r -p "Set up free HTTPS with Let's Encrypt now? The domain must already point to this server. [y/N] " answer || answer=""
set_ssl_redirect() {
  if grep -q '^DJANGO_SECURE_SSL_REDIRECT=' "$ROOT/.env"; then
    sed -i "s/^DJANGO_SECURE_SSL_REDIRECT=.*/DJANGO_SECURE_SSL_REDIRECT=$1/" "$ROOT/.env"
  else
    echo "DJANGO_SECURE_SSL_REDIRECT=$1" >> "$ROOT/.env"
  fi
  systemctl restart "$SERVICE"
}

if [[ "$answer" =~ ^[Yy]$ ]]; then
  apt-get install -y certbot python3-certbot-nginx
  # shellcheck disable=SC2086
  certbot --nginx --redirect $(printf -- '-d %s ' $SERVER_NAMES)
  set_ssl_redirect 1
else
  # Without a certificate, redirecting to https:// would make the site unreachable.
  set_ssl_redirect 0
  echo "HTTPS skipped; the site is served over http:// for now."
  echo "Run this script again later to add HTTPS."
fi

cat <<EOF

Done. Useful commands:
  sudo systemctl status $SERVICE      # is the site running?
  sudo journalctl -u $SERVICE -f      # live logs
  ./scripts/update.sh                 # after pulling new code
EOF
