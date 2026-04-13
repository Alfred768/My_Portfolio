type SectionHeadingProps = {
  eyebrow?: string
  title: string
  accent?: string
  description?: string
  align?: 'left' | 'center'
}

export function SectionHeading({
  eyebrow,
  title,
  accent,
  description,
  align = 'left',
}: SectionHeadingProps) {
  const alignment = align === 'center' ? 'items-center text-center' : 'items-start text-left'

  return (
    <div className={`flex max-w-3xl flex-col gap-3 ${alignment}`}>
      {eyebrow ? (
        <p className="text-sm font-medium uppercase tracking-[0.22em] text-[#fd853a]">{eyebrow}</p>
      ) : null}
      <h2 className="text-3xl font-semibold tracking-[-0.03em] text-slate-950 sm:text-4xl">
        {title}
        {accent ? <span className="text-[#fd853a]"> {accent}</span> : null}
      </h2>
      {description ? <p className="text-base leading-7 text-slate-600">{description}</p> : null}
    </div>
  )
}
