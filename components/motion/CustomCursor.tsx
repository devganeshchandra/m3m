"use client";

import { useEffect, useRef } from "react";

export function CustomCursor() {
  const cursorRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const cursor = cursorRef.current;
    const finePointer = window.matchMedia("(pointer: fine)");
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    if (!cursor || !finePointer.matches || reduceMotion.matches) return;

    const onMove = (event: PointerEvent) => {
      cursor.style.setProperty("--cursor-x", `${event.clientX}px`);
      cursor.style.setProperty("--cursor-y", `${event.clientY}px`);
      cursor.dataset.visible = "true";
      const target = event.target;
      const labelledTarget =
        target instanceof Element ? target.closest<HTMLElement>("[data-cursor-label]") : null;
      cursor.dataset.label = labelledTarget?.dataset.cursorLabel ?? "";
      cursor.dataset.active = labelledTarget ? "true" : "false";
      const label = cursor.firstElementChild;
      if (label) label.textContent = labelledTarget?.dataset.cursorLabel ?? "";
    };

    const onLeave = () => {
      cursor.dataset.visible = "false";
    };

    window.addEventListener("pointermove", onMove, { passive: true });
    document.documentElement.addEventListener("pointerleave", onLeave);
    return () => {
      window.removeEventListener("pointermove", onMove);
      document.documentElement.removeEventListener("pointerleave", onLeave);
    };
  }, []);

  return (
    <div className="custom-cursor" ref={cursorRef} aria-hidden="true">
      <span />
    </div>
  );
}
