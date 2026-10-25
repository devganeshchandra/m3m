import Link from "next/link";
import { ArrowIcon } from "@/components/ui/ArrowIcon";
import { HeroEnquiryCard } from "@/components/enquiry/HeroEnquiryCard";
import { ContactSection } from "@/components/home/ContactSection";
import { HeroBannerCarousel } from "@/components/home/HeroBannerCarousel";
import { InsightsSection } from "@/components/home/InsightsSection";
import { MediaGallery } from "@/components/home/MediaGallery";
import { NewsSection } from "@/components/home/NewsSection";
import { OurJourneySection } from "@/components/home/OurJourneySection";
import { PersonalizedJourney } from "@/components/home/PersonalizedJourney";
import { ProjectCollection } from "@/components/projects/ProjectCollection";

export default function HomePage() {
  return (
    <main id="main-content">
      <section className="phase-one-hero" aria-labelledby="hero-title">
        <HeroBannerCarousel />
        <div className="phase-one-hero__veil" aria-hidden="true" />
        <div className="phase-one-hero__content">
          <div className="phase-one-hero__copy">
            <p className="eyebrow phase-one-hero__eyebrow">
              <span>M3M India</span>
              <span aria-hidden="true">·</span>
              <span>The Signature Collection</span>
            </p>
            <h1 className="visually-hidden" id="hero-title">
              M3M India | The Signature Collection
            </h1>
            <p className="phase-one-hero__headline">
              A legacy of
              <br />
              <span>living well.</span>
            </p>
            <p className="phase-one-hero__intro">
              Discover landmark residences and destinations by M3M India.
            </p>
            <Link className="text-link" href="/#projects">
              <span>Explore our projects</span>
              <ArrowIcon />
            </Link>
          </div>
          <HeroEnquiryCard />
        </div>
        <div className="phase-one-hero__caption">
          <span>Gurugram · India</span>
          <span>Artistic impression</span>
        </div>
      </section>

      <ProjectCollection />

      <OurJourneySection />
      <NewsSection />
      <MediaGallery />
      <InsightsSection />
      <PersonalizedJourney />
      <ContactSection />
    </main>
  );
}
