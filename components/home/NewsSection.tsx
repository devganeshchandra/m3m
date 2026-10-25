"use client";

import Image, { type StaticImageData } from "next/image";
import { useEffect, useRef, useState } from "react";
import noidaImage from "@/images/projects_main/m3m_culinen_m.webp";
import gurugramImage from "@/images/projects_main/m3m_jacob_co.jpg";
import growthImage from "@/images/projects_main/m3m_smart_world_noida_residence.webp";

type PressItem = {
  title: string;
  source: string;
  date: string;
  summary: string;
  image: StaticImageData;
  articleUrl: string;
};

const pressItems: PressItem[] = [
  {
    title: "M3M bags Rs 1,839 crore mega Noida land deal, pips DLF",
    source: "Moneycontrol",
    date: "8 September 2026",
    summary:
      "Moneycontrol reports on M3M’s reported Noida land acquisition, a major transaction in the region’s real-estate market.",
    image: noidaImage,
    articleUrl:
      "https://news.google.com/rss/articles/CBMivgFBVV95cUxOTV8tN0NhY1hqOTc4SFpLQmluczBYMVpkR283ZTJUclRRVWl5NHhOQmJiaXQ1YWlSaGJNdDNpQnZucFFLaGM3VkpWUmc0eDRQNUpmNThlTTIwQVpCOTFtT1Z3VjJkakk2Rk01MHZGTzg3eHIwZHRHNWpxRkt2bGwwcnZmZWpESWxsektPQ3pMekxISUZaZGJpcm5fZWdyd2JoeFNjWGlQUDZqVmpta0pYY0g4US1iczY2LVRGRk1n0gHDAUFVX3lxTFBLQ0Q3Qk1YNV9wdUk2VEtBYU80S3lHUGZUelM2ck1DMGF0dFp6Q2w4LWZuSDFCR1JRLTlxa3A1WUlFZkpQUEpCWDIyUFBFTlVzT2NzSXhCVm0xeXRwZzFNWFlJNWNNVWFTRGNhQmhlR3FtcmZRVm9jNnBpOG9xQ044VnZEMzZScDU1NUJiVVN1Z0ZxUEg0OXJsOUVUSXJ1VjJTNUtrS1duVVh0S1FiY05RZDdtR2NGdlZWWXg5MHUxbzdSNA?oc=5",
  },
  {
    title:
      "M3M India to invest Rs 600 cr to build commercial project in Gurugram",
    source: "The Economic Times",
    date: "31 July 2026",
    summary:
      "The Economic Times covers M3M India’s announced investment in a commercial development in Gurugram.",
    image: gurugramImage,
    articleUrl:
      "https://news.google.com/rss/articles/CBMi5gFBVV95cUxPY1o2SUQzOVpwM0tJbWlCTmI1Sjd4c0JRR1k5d3k3MENqYlhuaF9Fc2ZCZkZLc0dQMm5TcXA2VUktVy1ZdVZQaHZHaFVEQmtsVkR2Yk9RdGYzaDUtNUV5SUU1emtFNWQwbWdVVzBqZXNibzlZNDk4Zkpmc3BZbW9pRXMyZ0VQRkNJeGpnNE5HcWNyZjZXa1RibkVEczVPaTRwUG5UZkd2d25aRWw4bUFHeER2WV9ULWVOQmtqMWozQWtCZHpIdmd1QXY4eHNnWk5nZUJ1aHZhWTBoLUFIdVVRWUZjNWdMQdIB6wFBVV95cUxQMm8zakh4MFhKQkdGeGloRnhTekdqQXV5YWJIbWVNbmlyZTk3Z1JZaUdaVlNkXzlqWldac25JSy0yVkllbGxaZFJvWmFsZFBLUVVScngzZmQ2Ul90SHczZHYwR2ZBdDhBQk5kYjh2dm5vcm5ySlBNYW44dlN0UWkwV2ZNanJuUFY5OHEtYnQzYXJKTTFsb3Z4ZWU2RU1YMG9GUF82UGtWbU5yV1llQVVxTDdPWDBFMjBUUzVOT1hEMHZtMTlmZDczTk1td0lxcE51UUFXWjhYRFNPNDl2QURydlBGWFBtd3pmNWJZ?oc=5",
  },
  {
    title: "M3M India, Trehan IRIS to invest ₹1,900 crore in Gurugram projects",
    source: "ET Realty",
    date: "30 July 2026",
    summary:
      "ET Realty reports on a planned joint investment by M3M India and Trehan IRIS in Gurugram projects.",
    image: growthImage,
    articleUrl:
      "https://news.google.com/rss/articles/CBMi8gFBVV95cUxOWGJNTm1yUUx0bHM3UE1hQXc5NEV5ZmNoWGgtTGRXamRfQy10Q3ZMa3RfbWQ5MmtuZ3VKUHhFZW9ka3FCWmJZeTkxMURmLTNYejZpTmJLYUZpX1hSdVBVWDNiLUtQZ0VpOVV2WXk0TnBpaWl5VzZtQUFEbnlrTlVFeG1pRGV6SklpTWNWWEpIWW82ZGNNREVKaHJSU0ZHUUcySDM5N3FnMDVzaUt2cHJodjRETG1kcnBYMHNSVDFsNVB6RHlTbXRtQXJOckNsM0JNX2hObFB5OGliSk1LVUNXUFo3eTkxMjNISG1rODhaaHFkUdIB9wFBVV95cUxOSG9RRnhheVBJbGpRdUlLRlhjU05fUktNQjNDZXJWZTNicHBPNEdSS29NLWhtSWpvYUdkUl9meEpZSVhuNnMwZjVMYXJnQUNsNDhwRl8yb2dyanFRZjhkdUtseDUzVkFJODV3bkpPbVU3YUFfT0VyMTB4NVh4R0ZSLXh5NFhGZW9iZ3V3ZVJQaVpkV3BrZEVrN1ZMeUZ0V2xNZURPT1VjWWI3RjlDM0VjT2dXU1ZDbTlTY2RMLWVVcy15R0xqbmlRY3Rhb3U5OThRaVYxR3NIeDVhOE5ud2NpLVNvRHhZQUdia3ROcDJ4d2ZxM1JCajhr?oc=5",
  },
];

export function NewsSection() {
  const [selectedItem, setSelectedItem] = useState<PressItem | null>(null);
  const dialogRef = useRef<HTMLDialogElement>(null);

  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return;

    if (selectedItem && !dialog.open) {
      dialog.showModal();
    } else if (!selectedItem && dialog.open) {
      dialog.close();
    }
  }, [selectedItem]);

  return (
    <section aria-labelledby="news-title" className="press-section" id="news">
      <div className="press-section__inner">
        <div className="press-section__header">
          <div>
            <p className="section-label press-section__label">
              <span className="section-label__rule" />
              In the headlines
            </p>
            <h2 id="news-title">
              M3M, as seen
              <br />
              <em>in the news.</em>
            </h2>
          </div>
          <p>
            A selection of recent coverage from established business and real
            estate publications.
          </p>
        </div>

        <div className="press-grid">
          {pressItems.map((item) => (
            <button
              aria-haspopup="dialog"
              className="press-card"
              key={item.title}
              onClick={() => setSelectedItem(item)}
              type="button"
            >
              <span className="press-card__image">
                <Image
                  alt=""
                  fill
                  sizes="(max-width: 700px) 70vw, 260px"
                  src={item.image}
                />
                <span className="press-card__image-mark" aria-hidden="true">
                  M3M
                </span>
              </span>
              <span className="press-card__meta">
                <span>{item.source}</span>
                <span>{item.date}</span>
              </span>
              <strong>{item.title}</strong>
              <span className="press-card__action">
                Read the story <span aria-hidden="true">↗</span>
              </span>
            </button>
          ))}
        </div>
      </div>

      <dialog
        aria-labelledby="press-dialog-title"
        className="press-dialog"
        onClose={() => setSelectedItem(null)}
        ref={dialogRef}
      >
        {selectedItem && (
          <div className="press-dialog__content">
            <button
              aria-label="Close article details"
              className="press-dialog__close"
              onClick={() => dialogRef.current?.close()}
              type="button"
            >
              <span aria-hidden="true">×</span>
            </button>
            <p className="section-label">
              <span className="section-label__rule" />
              {selectedItem.source} · {selectedItem.date}
            </p>
            <h2 id="press-dialog-title">{selectedItem.title}</h2>
            <p>{selectedItem.summary}</p>
            <a href={selectedItem.articleUrl} rel="noreferrer" target="_blank">
              Continue to {selectedItem.source}
              <span aria-hidden="true">↗</span>
            </a>
          </div>
        )}
      </dialog>
    </section>
  );
}
