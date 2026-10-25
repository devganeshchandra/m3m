import type { StaticImageData } from "next/image";
import jacobJewelImage from "@/images/projects_main/m3m_jacob_jewel.jpg";
import jacobResidencesImage from "@/images/projects_main/m3m_jacob_co.jpg";
import cullinanAvenueImage from "@/images/projects_main/m3m_culinen_avenue.webp";
import cullinanImage from "@/images/projects_main/m3m_culinen_m.webp";
import linePentsuitesImage from "@/images/projects_main/m3m_line_pentsuit.jpg";
import lineRetailImage from "@/images/projects_main/m3m_line_Retail_shops.jpg";
import smartworldCommercialImage from "@/images/projects_main/m3m_smar_world_noida_commercial.webp";
import smartworldResidenceImage from "@/images/projects_main/m3m_smart_world_noida_residence.webp";
import trumpTowerImage from "@/images/projects_main/m3m_trump_tower.jpg";

export type Project = {
  slug: string;
  name: string;
  category: string;
  interests: ("residential" | "commercial")[];
  offering: string;
  location: string;
  rera: string;
  image: StaticImageData;
  summary: string;
};

export const projects: Project[] = [
  {
    slug: "m3m-jacob-co-residences",
    name: "M3M Jacob & Co. Residences",
    category: "M3M Jacob & Co.",
    interests: ["residential"],
    offering: "3, 4 & 5 BHK Apartments",
    location: "Sector 97, Noida Expressway",
    rera: "UPRERAPRJ690055/10/2025",
    image: jacobResidencesImage,
    summary:
      "A collection of 3, 4 and 5 BHK residences at Sector 97, Noida Expressway.",
  },
  {
    slug: "m3m-jacob-jewel-crest-noida",
    name: "M3M Jacob Jewel Crest Noida",
    category: "M3M Jacob & Co.",
    interests: ["commercial"],
    offering: "Retail Shops, Food Court & Restaurant",
    location: "Sector 97, Noida Expressway",
    rera: "UPRERAPRJ690055/10/2025",
    image: jacobJewelImage,
    summary:
      "A retail, food court and restaurant destination at Sector 97, Noida Expressway.",
  },
  {
    slug: "m3m-the-line-retail-shops",
    name: "M3M The Line Retail Shops",
    category: "M3M The Line",
    interests: ["residential", "commercial"],
    offering: "Studio Apartments, Retail Shops & Food Court",
    location: "Sector 72, Central Noida",
    rera: "UPRERAPRJ246070",
    image: lineRetailImage,
    summary:
      "Studio apartments, retail shops and a food court at Sector 72, Central Noida.",
  },
  {
    slug: "m3m-the-line-pentsuites",
    name: "M3M The Line Pentsuites",
    category: "M3M The Line",
    interests: ["residential"],
    offering: "1 BHK Serviced Apartment",
    location: "Sector 72, Central Noida",
    rera: "UPRERAPRJ246070",
    image: linePentsuitesImage,
    summary: "1 BHK serviced apartments at Sector 72, Central Noida.",
  },
  {
    slug: "m3m-the-cullinan-residential",
    name: "M3M The Cullinan Residential",
    category: "M3M The Cullinan",
    interests: ["residential"],
    offering: "3, 4 & 5 BHK Apartments",
    location: "Sector 94, Noida Expressway",
    rera: "UPRERAPRJ442214",
    image: cullinanImage,
    summary:
      "A range of 3, 4 and 5 BHK apartments at Sector 94, Noida Expressway.",
  },
  {
    slug: "m3m-the-cullinan-avenue",
    name: "M3M The Cullinan Avenue",
    category: "M3M The Cullinan",
    interests: ["commercial"],
    offering: "Commercial Retail Shops",
    location: "Sector 94, Noida Expressway",
    rera: "UPRERAPRJ442214",
    image: cullinanAvenueImage,
    summary: "Commercial retail shops at Sector 94, Noida Expressway.",
  },
  {
    slug: "smartworld-noida-residential",
    name: "Smartworld Noida Residential",
    category: "Smartworld Noida",
    interests: ["residential"],
    offering: "4 BHK Residence · 4,500 sq. ft.",
    location: "Sector 98, Noida Expressway",
    rera: "UPRERAPRJ300532/12/2025",
    image: smartworldResidenceImage,
    summary:
      "4 BHK residences, with a stated area of 4,500 sq. ft., at Sector 98, Noida Expressway.",
  },
  {
    slug: "smartworld-noida-commercial",
    name: "Smartworld Noida Commercial",
    category: "Smartworld Noida",
    interests: ["residential", "commercial"],
    offering:
      "1 & 2 BHK Serviced Apartments, Lockable Retail, Cafés & Restaurant",
    location: "Sector 98, Noida Expressway",
    rera: "UPRERAPRJ300532/12/2025",
    image: smartworldCommercialImage,
    summary:
      "Serviced apartments, lockable retail, cafés and a restaurant at Sector 98, Noida Expressway.",
  },
  {
    slug: "m3m-trump-tower-noida",
    name: "M3M Trump Tower Noida",
    category: "M3M Trump Tower",
    interests: ["residential"],
    offering: "4 & 5 BHK Apartments",
    location: "Sector 94, Noida Expressway",
    rera: "UPRERAPRJ794824/10/2025",
    image: trumpTowerImage,
    summary:
      "A collection of 4 and 5 BHK apartments at Sector 94, Noida Expressway.",
  },
];

export function getProjectBySlug(slug: string) {
  return projects.find((project) => project.slug === slug);
}
