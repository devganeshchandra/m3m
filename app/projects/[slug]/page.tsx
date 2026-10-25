import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { EnquiryTrigger } from "@/components/enquiry/EnquiryTrigger";
import {
  getProjectBySlug,
  projects,
} from "@/components/projects/projectData";
import { ArrowIcon } from "@/components/ui/ArrowIcon";

type ProjectPageProps = {
  params: Promise<{ slug: string }>;
};

export function generateStaticParams() {
  return projects.map(({ slug }) => ({ slug }));
}

export async function generateMetadata({
  params,
}: ProjectPageProps): Promise<Metadata> {
  const { slug } = await params;
  const project = getProjectBySlug(slug);

  if (!project) {
    return { title: "Project not found" };
  }

  return {
    title: project.name,
    description: project.summary,
  };
}

export default async function ProjectPage({ params }: ProjectPageProps) {
  const { slug } = await params;
  const project = getProjectBySlug(slug);

  if (!project) {
    notFound();
  }

  return (
    <main className="project-detail" id="main-content">
      <section
        aria-labelledby="project-detail-title"
        className="project-detail__hero"
      >
        <Image
          alt={project.name}
          className="project-detail__image"
          fill
          priority
          sizes="100vw"
          src={project.image}
        />
        <div className="project-detail__shade" />
        <div className="project-detail__hero-content">
          <Link className="project-detail__back" href="/#projects">
            <ArrowIcon />
            All projects
          </Link>
          <p className="project-detail__category">{project.category}</p>
          <h1 id="project-detail-title">{project.name}</h1>
          <p className="project-detail__hero-location">{project.location}</p>
        </div>
        <span className="project-detail__caption">M3M India · Noida</span>
      </section>

      <section className="project-detail__overview">
        <div className="project-detail__copy">
          <p className="section-label">
            <span className="section-label__rule" />
            The address
          </p>
          <h2>A place to make your own.</h2>
          <p>{project.summary}</p>
          <EnquiryTrigger
            className="project-detail__enquire"
            showArrow
          >
            Enquire now
          </EnquiryTrigger>
        </div>
        <dl className="project-detail__facts">
          <div>
            <dt>Offering</dt>
            <dd>{project.offering}</dd>
          </div>
          <div>
            <dt>Location</dt>
            <dd>{project.location}</dd>
          </div>
          <div>
            <dt>Project RERA No.</dt>
            <dd>{project.rera}</dd>
          </div>
        </dl>
      </section>

      <div className="project-detail__footer-link">
        <Link className="text-link" href="/#projects">
          <span>Explore all M3M projects</span>
          <ArrowIcon />
        </Link>
      </div>
    </main>
  );
}
