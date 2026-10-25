import Image from "next/image";
import Link from "next/link";
import { EnquiryTrigger } from "@/components/enquiry/EnquiryTrigger";
import { projects } from "@/components/projects/projectData";
import { ArrowIcon } from "@/components/ui/ArrowIcon";

export function ProjectCollection() {
  return (
    <section
      aria-labelledby="projects-title"
      className="projects-section"
      id="projects"
    >
      <div className="projects-section__inner">
        <div className="projects-section__header">
          <div>
            <p className="section-label projects-section__label">
              <span className="section-label__rule" />
              M3M projects · Noida
            </p>
            <h2 className="projects-section__title" id="projects-title">
              A new view
              <br />
              <em>of Noida.</em>
            </h2>
          </div>
          <p className="projects-section__intro">
            Nine distinctive residences and destinations across Noida
            Expressway and Central Noida. Find the address that feels like
            yours.
          </p>
        </div>

        <div className="projects-section__divider" aria-hidden="true">
          <span />
          <span>Explore the collection</span>
          <span />
        </div>

        <div className="projects-grid">
          {projects.map((project, index) => (
            <article className="project-card" key={project.slug}>
              <div className="project-card__visual">
                <Link
                  aria-label={`Discover ${project.name}`}
                  className="project-card__image-link"
                  href={`/projects/${project.slug}`}
                >
                  <span className="project-card__image-frame">
                    <Image
                      alt={project.name}
                      className="project-card__image"
                      fill
                      sizes="(max-width: 700px) 82vw, (max-width: 1100px) 42vw, 28vw"
                      src={project.image}
                    />
                    <span className="project-card__image-shade" />
                    <span className="project-card__discover">
                      <span>Discover address</span>
                      <span className="project-card__discover-icon">
                        <ArrowIcon />
                      </span>
                    </span>
                  </span>
                </Link>
              </div>

              <div className="project-card__content">
                <p className="project-card__category">
                  <span>{project.category}</span>
                  <span className="project-card__index">
                    {String(index + 1).padStart(2, "0")}
                  </span>
                </p>
                <h3 className="project-card__title">
                  <Link href={`/projects/${project.slug}`}>{project.name}</Link>
                </h3>
                <p className="project-card__offering">{project.offering}</p>
                <dl className="project-card__facts">
                  <div>
                    <dt>Location</dt>
                    <dd>{project.location}</dd>
                  </div>
                  <div>
                    <dt>Project RERA No.</dt>
                    <dd>{project.rera}</dd>
                  </div>
                </dl>
                <div className="project-card__actions">
                  <EnquiryTrigger className="project-card__enquire">
                    Enquire now
                    <ArrowIcon />
                  </EnquiryTrigger>
                  <Link
                    className="project-card__details"
                    href={`/projects/${project.slug}`}
                  >
                    Project details
                    <ArrowIcon />
                  </Link>
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
