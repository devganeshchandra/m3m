import Image from "next/image";
import Link from "next/link";
import insightImage1 from "@/images/media/m3.jpeg";
import insightImage2 from "@/images/media/m8.jpeg";
import insightImage3 from "@/images/media/m13.jpeg";
import { ArrowIcon } from "@/components/ui/ArrowIcon";

const insights = [
  {
    image: insightImage1,
    category: "Thoughtful living",
    title: "Wellness woven into the everyday",
    description:
      "Spaces to pause, reset and make time for the moments that matter.",
  },
  {
    image: insightImage2,
    category: "City perspective",
    title: "A new view of Noida",
    description:
      "Discover addresses shaped by the energy and possibilities of the city.",
  },
  {
    image: insightImage3,
    category: "Design & detail",
    title: "The details that define an address",
    description:
      "From arrival to the everyday, thoughtful design leaves its mark.",
  },
];

export function InsightsSection() {
  return (
    <section
      aria-labelledby="insights-title"
      className="insights-section"
      id="insights"
    >
      <div className="insights-section__inner">
        <div className="insights-section__header">
          <div>
            <p className="section-label insights-section__label">
              <span className="section-label__rule" />
              Ideas &amp; perspectives
            </p>
            <h2 id="insights-title">Insights from M3M</h2>
          </div>
          <p>
            A closer look at the ideas, details and city stories behind each
            address.
          </p>
        </div>
        <div className="insights-grid">
          {insights.map((insight) => (
            <article className="insight-card" key={insight.title}>
              <div className="insight-card__image">
                <Image
                  alt=""
                  fill
                  sizes="(max-width: 700px) 90vw, (max-width: 1000px) 45vw, 30vw"
                  src={insight.image}
                />
              </div>
              <div className="insight-card__content">
                <p>{insight.category}</p>
                <h3>{insight.title}</h3>
                <span>{insight.description}</span>
                <Link href="/#projects" aria-label="Explore M3M projects">
                  Explore projects
                  <ArrowIcon />
                </Link>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
