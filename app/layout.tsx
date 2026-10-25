import type { Metadata, Viewport } from "next";
import { Open_Sans, Roboto } from "next/font/google";
import type { ReactNode } from "react";
import { CustomCursor } from "@/components/motion/CustomCursor";
import { MotionShell } from "@/components/motion/MotionShell";
import { SiteFooter } from "@/components/layout/SiteFooter";
import { SiteHeader } from "@/components/layout/SiteHeader";
import { FloatingActions } from "@/components/layout/FloatingActions";
import { Preloader } from "@/components/motion/Preloader";
import { EnquiryExperience } from "@/components/enquiry/EnquiryExperience";
import "./globals.css";

const displayFont = Roboto({
  subsets: ["latin"],
  variable: "--font-display",
  weight: ["400", "500", "700"],
  display: "swap",
});

const bodyFont = Open_Sans({
  subsets: ["latin"],
  variable: "--font-body",
  weight: ["400", "500", "600", "700"],
  display: "swap",
});

const siteUrl = "https://www.m3mindia.com";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: "M3M India | Considered Living",
    template: "%s | M3M India",
  },
  description:
    "A considered expression of place. Explore residences, destinations and spaces by M3M India.",
  alternates: {
    canonical: "/",
  },
  openGraph: {
    type: "website",
    siteName: "M3M India",
    title: "M3M India | Considered Living",
    description:
      "A considered expression of place. Explore residences, destinations and spaces by M3M India.",
    url: siteUrl,
  },
  twitter: {
    card: "summary_large_image",
    title: "M3M India | Considered Living",
    description:
      "A considered expression of place. Explore residences, destinations and spaces by M3M India.",
  },
};

export const viewport: Viewport = {
  themeColor: "#ffffff",
  colorScheme: "light",
};

const organizationSchema = {
  "@context": "https://schema.org",
  "@type": "Organization",
  name: "M3M India",
  url: siteUrl,
  telephone: "+91-1800-123-3333",
  address: {
    "@type": "PostalAddress",
    streetAddress:
      "41st Floor, Tower-1, M3M International Financial Center, Sector-66, Golf Course Road (Extn.)",
    addressLocality: "Gurugram",
    postalCode: "122101",
    addressCountry: "IN",
  },
};

export default function RootLayout({
  children,
}: Readonly<{ children: ReactNode }>) {
  return (
    <html lang="en" className={`${displayFont.variable} ${bodyFont.variable}`}>
      <body>
        <a className="skip-link" href="#main-content">
          Skip to content
        </a>
        <SiteHeader />
        <MotionShell>{children}</MotionShell>
        <SiteFooter />
        <FloatingActions />
        <EnquiryExperience />
        <CustomCursor />
        <Preloader />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(organizationSchema),
          }}
        />
      </body>
    </html>
  );
}
