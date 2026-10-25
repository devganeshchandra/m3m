import Image from "next/image";
import Link from "next/link";
import colorLogo from "@/images/logo/m3m-logo.png";

const footerLinks = [
  { label: "Projects", href: "/#projects" },
  { label: "Our Journey", href: "/#about" },
  { label: "Media", href: "/#media" },
  { label: "Insights", href: "/#insights" },
  { label: "Contact Us", href: "/#contact" },
];

export function SiteFooter() {
  return (
    <footer className="site-footer">
      <div className="page-wrap">
        <div className="site-footer__top">
          <div className="site-footer__brand">
            <Link
              className="wordmark wordmark--footer"
              href="/"
              aria-label="M3M India home"
            >
              <Image
                alt=""
                className="wordmark__logo wordmark__logo--color"
                height={56}
                src={colorLogo}
                width={180}
              />
              <span className="visually-hidden">M3M India</span>
            </Link>
          </div>
          <div className="site-footer__address">
            <p className="eyebrow">Corporate office</p>
            <address>
              41st Floor, Tower-1, M3M International Financial Center,
              <br />
              Sector-66, Golf Course Road (Extn.), Gurugram-122101
            </address>
            <a href="tel:18001233333">Toll-free 1800 123 3333</a>
          </div>
          <div className="site-footer__links">
            <p className="eyebrow">Explore</p>
            {footerLinks.map((link) => (
              <Link href={link.href} key={link.label}>
                {link.label}
              </Link>
            ))}
          </div>
          <div className="site-footer__connect">
            <p className="eyebrow">Connect</p>
            <a
              href="https://wa.me/919311995812"
              rel="noreferrer"
              target="_blank"
            >
              WhatsApp
            </a>
            <a href="tel:18001233333">Call M3M</a>
          </div>
        </div>

        <details className="footer-disclaimer">
          <summary>Important information</summary>
          <p>
            Images and visuals are artistic impressions and are indicative only.
            Project plans, specifications, amenities, areas and other
            particulars may change, subject to applicable approvals and the
            relevant project documents. Prospective buyers should review the
            applicable RERA registration and project disclosures before making a
            decision. Nothing on this website is an offer, invitation or legal
            or financial advice. Project-specific information will be provided
            with the relevant project materials.
          </p>
        </details>

        <div className="site-footer__bottom">
          <span>
            © {new Date().getFullYear()} M3M India. All rights reserved.
          </span>
          <div>
            <Link href="/privacy">Privacy</Link>
            <Link href="/disclaimer">Disclaimer</Link>
            <Link href="/compliance">Compliance</Link>
          </div>
          <span>Website experience · Phase 1</span>
        </div>
      </div>
    </footer>
  );
}
