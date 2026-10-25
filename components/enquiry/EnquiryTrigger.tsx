"use client";

import type { ReactNode } from "react";
import { ArrowIcon } from "@/components/ui/ArrowIcon";

export function EnquiryTrigger({
  children,
  className,
  showArrow = false,
}: {
  children: ReactNode;
  className: string;
  showArrow?: boolean;
}) {
  return (
    <button
      aria-haspopup="dialog"
      className={className}
      onClick={() => window.dispatchEvent(new Event("m3m:open-enquiry"))}
      type="button"
    >
      {showArrow ? (
        <>
          <span>{children}</span>
          <ArrowIcon />
        </>
      ) : (
        children
      )}
    </button>
  );
}
