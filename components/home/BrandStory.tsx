import Image from "next/image";
import cullinanImage from "@/images/projects_main/m3m_culinen_m.webp";
import retailImage from "@/images/projects_main/m3m_line_Retail_shops.jpg";
import signatureImage from "@/images/home_detail.jpg";
import { ArrowIcon } from "@/components/ui/ArrowIcon";

export function BrandStory() {
  return (
    <section aria-labelledby="brand-story-title" className="brand-story">
      <div className="brand-story__inner">
        <p className="brand-story__eyebrow">
          <span />A closer look at what matters
        </p>
        <div className="brand-story__grid">
          <article className="brand-story__lead">
            <Image
              alt=""
              className="brand-story__lead-image"
              fill
              sizes="(max-width: 760px) 100vw, 36vw"
              src={signatureImage}
            />
            <div className="brand-story__lead-shade" />
            <div className="brand-story__lead-copy">
              <p>THE M3M PERSPECTIVE</p>
              <h2 id="brand-story-title">
                Places that make room for <em>more.</em>
              </h2>
              <span>Architecture · Living · Possibility</span>
            </div>
            <span className="brand-story__lead-index" aria-hidden="true">
              M3M
            </span>
          </article>

          <article className="brand-story__image-card">
            <Image
              alt="Artistic impression of M3M The Cullinan"
              className="brand-story__image"
              fill
              sizes="(max-width: 760px) 100vw, 30vw"
              src={cullinanImage}
            />
            <div className="brand-story__image-shade" />
            <div className="brand-story__image-copy">
              <p>01 / ARCHITECTURE</p>
              <h3>A striking sense of place.</h3>
              <ArrowIcon />
            </div>
          </article>

          <article className="brand-story__note brand-story__note--stone">
            <span className="brand-story__note-index">
              02 / EVERYDAY LIVING
            </span>
            <h3>Designed around the moments that matter.</h3>
            <p>
              From a quiet pause to a shared celebration, the best spaces make
              life feel a little more considered.
            </p>
            <span className="brand-story__note-mark" aria-hidden="true">
              M
            </span>
          </article>

          <article className="brand-story__note brand-story__note--olive">
            <span className="brand-story__note-symbol" aria-hidden="true" />
            <span className="brand-story__note-index">03 / THE DETAILS</span>
            <h3>Small details. A different feeling.</h3>
            <p>
              Thoughtful design is more than what you see. It is how a place
              welcomes you, works for you and stays with you.
            </p>
          </article>

          <article className="brand-story__image-card brand-story__image-card--retail">
            <Image
              alt="Retail destination at M3M The Line"
              className="brand-story__image"
              fill
              sizes="(max-width: 760px) 100vw, 30vw"
              src={retailImage}
            />
            <div className="brand-story__image-shade" />
            <div className="brand-story__image-copy">
              <p>04 / DESTINATIONS</p>
              <h3>Room to discover something new.</h3>
              <ArrowIcon />
            </div>
          </article>
        </div>
      </div>
    </section>
  );
}
