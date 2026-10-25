"use client";

import Image from "next/image";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import { EnquiryTrigger } from "@/components/enquiry/EnquiryTrigger";
import { WhatsAppIcon } from "@/components/ui/WhatsAppIcon";
import colorLogo from "@/images/logo/m3m-logo.png";
import transparentLogo from "@/images/logo/logo_tranparent.webp";

const navigation = [
  { label: "Projects", href: "/#projects" },
  { label: "Our Journey", href: "/#about" },
  { label: "Media", href: "/#media" },
  { label: "Insights", href: "/#insights" },
  { label: "Contact Us", href: "/#contact" },
];

export function SiteHeader() {
  const [scrolled, setScrolled] = useState(false);
  const pathname = usePathname();

  useEffect(() => {
    const updateScroll = () => setScrolled(window.scrollY > 24);
    updateScroll();
    window.addEventListener("scroll", updateScroll, { passive: true });
    return () => window.removeEventListener("scroll", updateScroll);
  }, []);

  return (
    <header
      className={`site-header${scrolled ? " site-header--scrolled" : ""}`}
    >
      <div className="site-header__inner">
        <Link
          className="wordmark"
          href="/"
          aria-label="M3M India home"
          onClick={(event) => {
            if (pathname !== "/") return;

            event.preventDefault();
            if (window.location.hash) {
              window.history.replaceState(
                window.history.state,
                "",
                `${window.location.pathname}${window.location.search}`,
              );
            }
            window.dispatchEvent(new Event("m3m:scroll-to-top"));
          }}
        >
          <Image
            alt=""
            className={`wordmark__logo ${scrolled ? "wordmark__logo--transparent" : "wordmark__logo--color"}`}
            height={56}
            priority
            src={scrolled ? transparentLogo : colorLogo}
            width={180}
          />
          <span className="visually-hidden">M3M India</span>
        </Link>

        <nav className="desktop-nav" aria-label="Main navigation">
          {navigation.map((item) => (
            <Link
              className="desktop-nav__link"
              href={item.href}
              key={item.label}
            >
              {item.label}
            </Link>
          ))}
        </nav>

        <div className="site-header__actions">
          <a className="header-phone" href="tel:18001233333">
            1800 123 3333
          </a>
          <a
            aria-label="Chat with M3M India on WhatsApp"
            className="header-whatsapp"
            href="https://wa.me/919311995812"
            rel="noreferrer"
            target="_blank"
          >
            <WhatsAppIcon />
          </a>
          <EnquiryTrigger className="header-consultation" showArrow>
            Private consultation
          </EnquiryTrigger>
        </div>
      </div>
    </header>
  );
}
