import type { AnchorHTMLAttributes, ReactNode } from 'react'

type PrimaryButtonProps = AnchorHTMLAttributes<HTMLAnchorElement> & {
  children: ReactNode
  variant?: 'solid' | 'ghost'
}

export function PrimaryButton({
  children,
  className = '',
  variant = 'solid',
  ...props
}: PrimaryButtonProps) {
  const variantClassName =
    variant === 'solid'
      ? 'bg-[#fd853a] text-white shadow-[0_20px_40px_rgba(253,133,58,0.28)]'
      : 'border border-slate-300 bg-white/70 text-slate-900'

  return (
    <a
      className={`inline-flex items-center justify-center rounded-full px-5 py-3 text-sm font-medium transition hover:-translate-y-0.5 ${variantClassName} ${className}`.trim()}
      {...props}
    >
      {children}
    </a>
  )
}
