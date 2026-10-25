import { EnquiryTrigger } from "@/components/enquiry/EnquiryTrigger";

export function FloatingActions() {
  return (
    <nav className="floating-actions" aria-label="Contact M3M India">
      <a href="tel:18001233333">Call</a>
      <a href="https://wa.me/919311995812" rel="noreferrer" target="_blank">
        WhatsApp
      </a>
      <EnquiryTrigger className="floating-actions__enquire">
        Enquire
      </EnquiryTrigger>
    </nav>
  );
}
