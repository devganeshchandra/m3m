import Image from "next/image";
import mediaImage1 from "@/images/media/m1.jpeg";
import mediaImage2 from "@/images/media/m2.jpeg";
import mediaImage3 from "@/images/media/m3.jpeg";
import mediaImage4 from "@/images/media/m4.jpeg";
import mediaImage5 from "@/images/media/m5.jpeg";
import mediaImage6 from "@/images/media/m6.jpeg";
import mediaImage7 from "@/images/media/m7.jpeg";
import mediaImage8 from "@/images/media/m8.jpeg";
import mediaImage9 from "@/images/media/m9.jpeg";
import mediaImage10 from "@/images/media/m10.jpeg";
import mediaImage11 from "@/images/media/m11.jpeg";
import mediaImage12 from "@/images/media/m12.jpeg";
import mediaImage13 from "@/images/media/m13.jpeg";
import { ArrowIcon } from "@/components/ui/ArrowIcon";

const mediaImages = [
  { image: mediaImage1, caption: "A welcoming sense of arrival" },
  { image: mediaImage2, caption: "Spaces made for gathering" },
  { image: mediaImage3, caption: "Wellness, thoughtfully considered" },
  { image: mediaImage4, caption: "An architectural first impression" },
  { image: mediaImage5, caption: "A quieter moment by the water" },
  { image: mediaImage6, caption: "Room to move and reset" },
  { image: mediaImage7, caption: "A pool framed by the city" },
  { image: mediaImage8, caption: "Evenings with a point of view" },
  { image: mediaImage9, caption: "Landscaped spaces to unwind" },
  { image: mediaImage10, caption: "A little more room to play" },
  { image: mediaImage11, caption: "A landmark on the skyline" },
  { image: mediaImage12, caption: "An illuminated expression of design" },
  { image: mediaImage13, caption: "A new perspective on the city" },
];

export function MediaGallery() {
  return (
    <section aria-labelledby="media-title" className="media-section" id="media">
      <div className="media-section__inner">
        <div className="media-section__header">
          <div>
            <p className="section-label media-section__label">
              <span className="section-label__rule" />A closer look
            </p>
            <h2 id="media-title">
              Spaces made
              <br />
              <em>to be experienced.</em>
            </h2>
          </div>
          <p>
            Explore the details, destinations and everyday moments that shape
            the M3M point of view.
          </p>
        </div>

        <div className="media-gallery">
          {mediaImages.map((image, index) => (
            <figure className="media-gallery__item" key={image.image.src}>
              <div className="media-gallery__image">
                <Image
                  alt={image.caption}
                  fill
                  priority={index < 2}
                  sizes="(max-width: 600px) 88vw, (max-width: 900px) 45vw, 25vw"
                  src={image.image}
                />
                <span className="media-gallery__index">
                  {String(index + 1).padStart(2, "0")}
                </span>
                <span aria-hidden="true" className="media-gallery__arrow">
                  <ArrowIcon />
                </span>
              </div>
              <figcaption>{image.caption}</figcaption>
            </figure>
          ))}
        </div>
      </div>
    </section>
  );
}
