"use client";

import { usePathname } from "next/navigation";
import { AnimatePresence, motion, useReducedMotion } from "framer-motion";
import type { ReactNode } from "react";
import { useEffect } from "react";
import { SmoothScroll } from "@/components/motion/SmoothScroll";

export function MotionShell({ children }: { children: ReactNode }) {
  const pathname = usePathname();
  const reduceMotion = useReducedMotion();

  useEffect(() => {
    window.dispatchEvent(new Event("m3m:scroll-to-top"));
  }, [pathname]);

  return (
    <>
      <SmoothScroll />
      <AnimatePresence mode="wait" initial={false}>
        <motion.div
          animate={reduceMotion ? { opacity: 1 } : { opacity: 1, y: 0 }}
          exit={reduceMotion ? { opacity: 1 } : { opacity: 0, y: -8 }}
          initial={reduceMotion ? false : { opacity: 0, y: 8 }}
          key={pathname}
          transition={{
            duration: reduceMotion ? 0 : 0.45,
            ease: [0.22, 1, 0.36, 1],
          }}
        >
          {children}
        </motion.div>
      </AnimatePresence>
    </>
  );
}
