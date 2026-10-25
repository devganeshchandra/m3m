import type { Metadata } from "next";
import { Button } from "@/components/ui/Button";
import { SectionLabel } from "@/components/ui/SectionLabel";
import { EnquiryTrigger } from "@/components/enquiry/EnquiryTrigger";

export const metadata: Metadata = {
  title: "Styleguide",
  description: "The visual language and interface foundations for M3M India.",
  alternates: { canonical: "/styleguide" },
  robots: { index: false, follow: false },
};

const colors = [
  { name: "Ink", value: "#0E0E0E", className: "swatch--ink" },
  { name: "Ivory", value: "#F5F1EA", className: "swatch--ivory" },
  { name: "Stone", value: "#D9D2C5", className: "swatch--stone" },
  { name: "Champagne", value: "#B89B6A", className: "swatch--champagne" },
  { name: "Warm grey", value: "#6E6A64", className: "swatch--warm-grey" },
];

export default function StyleguidePage() {
  return (
    <main id="main-content" className="styleguide">
      <section className="styleguide-hero">
        <div className="page-wrap">
          <SectionLabel index="00" label="The visual language" />
          <h1 className="display-heading styleguide-hero__title">
            Ivory Gallery
          </h1>
          <p className="styleguide-hero__intro">
            A quiet, editorial foundation. Warm paper, considered type and space
            enough for architecture to speak.
          </p>
        </div>
      </section>

      <section
        className="styleguide-section page-wrap"
        aria-labelledby="palette-title"
      >
        <SectionLabel index="01" label="Colour" />
        <h2 id="palette-title" className="section-heading">
          A restrained palette
        </h2>
        <div className="swatch-grid">
          {colors.map((color) => (
            <div className="swatch-card" key={color.name}>
              <div className={`swatch ${color.className}`} aria-hidden="true" />
              <p className="swatch-card__name">{color.name}</p>
              <p className="swatch-card__value">{color.value}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="styleguide-section styleguide-section--stone">
        <div className="page-wrap">
          <SectionLabel index="02" label="Typography" />
          <h2 className="section-heading">Room for the words</h2>
          <div className="type-specimen">
            <p className="eyebrow">Cormorant Garamond · Display</p>
            <p className="type-specimen__display">A lasting sense of place.</p>
            <p className="type-specimen__body">
              Manrope · Body and interface. Clear, composed and made for
              reading.
            </p>
            <p className="eyebrow">Small uppercase label · 0.2em tracking</p>
          </div>
        </div>
      </section>

      <section
        className="styleguide-section page-wrap"
        aria-labelledby="controls-title"
      >
        <SectionLabel index="03" label="Interface" />
        <h2 id="controls-title" className="section-heading">
          Considered details
        </h2>
        <div className="styleguide-controls">
          <div className="control-group">
            <p className="control-group__title">Actions</p>
            <div className="button-row">
              <EnquiryTrigger className="button button--solid" showArrow>
                Private consultation
              </EnquiryTrigger>
              <Button href="/#residences" variant="outline">
                Explore residences
              </Button>
            </div>
          </div>
          <form className="styleguide-form" action="#">
            <p className="control-group__title">Form fields</p>
            <div className="field-grid">
              <label className="field">
                <span className="field__label">Your name</span>
                <input
                  className="field__input"
                  autoComplete="name"
                  name="name"
                  placeholder="Name"
                  type="text"
                />
              </label>
              <label className="field">
                <span className="field__label">Email address</span>
                <input
                  className="field__input"
                  autoComplete="email"
                  name="email"
                  placeholder="name@example.com"
                  type="email"
                />
              </label>
            </div>
            <label className="consent-field">
              <input name="consent" type="checkbox" />
              <span>I agree to be contacted about M3M India projects.</span>
            </label>
          </form>
        </div>
      </section>

      <section className="styleguide-note">
        <div className="page-wrap styleguide-note__inner">
          <p className="eyebrow">Foundation · Phase 1</p>
          <p>
            The homepage, project stories and lead experience will be developed
            in the next phases.
          </p>
        </div>
      </section>
    </main>
  );
}
