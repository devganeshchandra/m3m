type SectionLabelProps = {
  index: string;
  label: string;
  light?: boolean;
};

export function SectionLabel({ index, label, light = false }: SectionLabelProps) {
  return (
    <p className={`section-label${light ? " section-label--light" : ""}`}>
      <span>{index}</span>
      <span className="section-label__rule" aria-hidden="true" />
      <span>{label}</span>
    </p>
  );
}
