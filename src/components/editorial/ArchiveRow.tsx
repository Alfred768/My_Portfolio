import { ArrowRight } from '@phosphor-icons/react'

type ArchiveRowProps = {
  index: string
  eyebrow: string
  title: string
  description: string
  meta: string
  href?: string
  imageSrc?: string
  imageAlt?: string
}

export function ArchiveRow({
  index,
  eyebrow,
  title,
  description,
  meta,
  href,
  imageSrc,
  imageAlt = '',
}: ArchiveRowProps) {
  const content = (
    <>
      <span className="archive-row__index">{index}</span>
      <span className="archive-row__rule" aria-hidden="true" />
      <span className="archive-row__body">
        <span className="archive-row__meta">
          <span>{eyebrow}</span>
          <span>{meta}</span>
        </span>
        <strong>{title}</strong>
        <span className="archive-row__description">{description}</span>
      </span>
      {imageSrc ? (
        <span className="archive-row__image">
          <img alt={imageAlt} src={imageSrc} />
        </span>
      ) : null}
      <ArrowRight aria-hidden="true" className="archive-row__arrow" weight="thin" />
    </>
  )

  return href ? (
    <a className="archive-row" href={href} rel="noreferrer" target="_blank">
      {content}
    </a>
  ) : (
    <article className="archive-row">{content}</article>
  )
}
