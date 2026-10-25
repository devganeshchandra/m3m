import { EnquiryTrigger } from "@/components/enquiry/EnquiryTrigger";
import { ArrowIcon } from "@/components/ui/ArrowIcon";
import { WhatsAppIcon } from "@/components/ui/WhatsAppIcon";

export function ContactSection() {
  return (
    <section
      aria-labelledby="contact-title"
      className="contact-section"
      id="contact"
    >
      <div className="contact-section__inner">
        <div className="contact-section__intro">
          <p className="section-label contact-section__label">
            <span className="section-label__rule" />
            We’re here to help
          </p>
          <h2 id="contact-title">
            Let’s find
            <br />
            <em>your next address.</em>
          </h2>
          <p>
            Tell us what you’re looking for. Our team can help you explore the
            right M3M project and answer your questions.
          </p>
          <EnquiryTrigger className="contact-section__enquire" showArrow>
            Speak with our team
          </EnquiryTrigger>
        </div>

        <div className="contact-section__details">
          <div className="contact-section__detail">
            <span className="contact-section__eyebrow">Call us</span>
            <a href="tel:18001233333">1800 123 3333</a>
            <span>Toll-free · M3M India</span>
          </div>
          <div className="contact-section__detail">
            <span className="contact-section__eyebrow">Visit us</span>
            <address>
              41st Floor, Tower-1, M3M International Financial Center,
              Sector-66, Golf Course Road (Extn.), Gurugram-122101
            </address>
          </div>
          <a
            className="contact-section__whatsapp"
            href="https://wa.me/919311995812"
            rel="noreferrer"
            target="_blank"
          >
            <WhatsAppIcon />
            <span>Continue the conversation on WhatsApp</span>
            <ArrowIcon />
          </a>
        </div>
      </div>
      <div className="contact-section__footer">
        <span>M3M INDIA</span>
        <span>Considered spaces. Personal conversations.</span>
      </div>
    </section>
  );
}
