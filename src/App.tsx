function App() {
  return (
    <main className="min-h-screen bg-neutral-50 px-6 py-16 text-slate-900">
      <section className="mx-auto flex max-w-5xl flex-col gap-6 rounded-[32px] bg-white px-8 py-12 shadow-[0_24px_80px_rgba(15,23,42,0.08)]">
        <p className="text-sm font-medium uppercase tracking-[0.2em] text-orange-500">
          Hybrid AI Engineer
        </p>
        <h1 className="text-4xl font-semibold sm:text-5xl">Gaoyi Wu</h1>
        <p className="max-w-2xl text-base leading-7 text-slate-600">
          Building applied AI and production ML systems for recruiter-ready, hiring-manager-readable portfolios.
        </p>
        <div className="flex flex-wrap gap-3">
          <a
            className="rounded-full bg-slate-950 px-5 py-3 text-sm font-medium text-white"
            href="#projects"
          >
            View Projects
          </a>
          <a
            className="rounded-full border border-slate-200 px-5 py-3 text-sm font-medium text-slate-900"
            href="#resume"
          >
            Resume
          </a>
        </div>
      </section>
    </main>
  )
}

export default App
