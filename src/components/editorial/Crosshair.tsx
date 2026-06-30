import { CrosshairSimple } from '@phosphor-icons/react'

type CrosshairProps = {
  className?: string
}

export function Crosshair({ className = '' }: CrosshairProps) {
  return (
    <CrosshairSimple
      aria-hidden="true"
      className={`editorial-crosshair ${className}`.trim()}
      weight="thin"
    />
  )
}
