import type { ProofMetric } from '../../types/portfolio'

type EvidenceStripProps = {
  proof: ProofMetric[]
}

export function EvidenceStrip({ proof }: EvidenceStripProps) {
  return (
    <section className="evidence-strip" aria-label="Career evidence">
      {proof.map((item) => (
        <article key={item.value}>
          <strong>{item.value}</strong>
          <span>{item.label}</span>
        </article>
      ))}
    </section>
  )
}
