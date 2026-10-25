import Link from "next/link";
import type { ComponentProps, ReactNode } from "react";
import { ArrowIcon } from "@/components/ui/ArrowIcon";

type ButtonProps = {
  children: ReactNode;
  href: string;
  variant?: "solid" | "outline";
} & Omit<ComponentProps<typeof Link>, "children" | "href">;

export function Button({ children, href, variant = "solid", ...props }: ButtonProps) {
  return (
    <Link className={`button button--${variant}`} href={href} {...props}>
      <span>{children}</span>
      <ArrowIcon />
    </Link>
  );
}
