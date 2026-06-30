import type {
  EditorialEducationEntry,
  EditorialSkillGroup,
  HeroContent,
  Language,
  ProofMetric,
} from '../../types/portfolio'
import { Crosshair } from '../editorial/Crosshair'
import { Reveal } from '../editorial/Reveal'

type EditorialAboutProps = {
  hero: HeroContent
  proof: ProofMetric[]
  skills: EditorialSkillGroup[]
  education: EditorialEducationEntry[]
  language: Language
}

export function EditorialAbout({
  hero,
  proof,
  skills,
  education,
  language,
}: EditorialAboutProps) {
  const copy =
    language === 'zh'
      ? {
          title: '关于我',
          intro: '我专注于把 AI 安全研究、算法设计与可部署的机器学习系统连接起来。',
          profile: '研究档案',
          signal: '成果信号',
          education: '教育',
          focus: '研究方向',
        }
      : {
          title: 'About me',
          intro:
            'I connect AI security research and algorithm design with measurable machine-learning systems that can survive real deployment constraints.',
          profile: 'Research profile',
          signal: 'Evidence signals',
          education: 'Education',
          focus: 'Research focus',
        }

  return (
    <section aria-labelledby="about-title" className="sac-about" id="about">
      <div className="sac-about__left">
        <Reveal>
          <h2 className="sac-section-title" id="about-title">
            {copy.title}
          </h2>
          <p className="sac-about__intro">{copy.intro}</p>
        </Reveal>

        <Reveal>
          <figure className="sac-blueprint">
            <Crosshair className="sac-blueprint__cross sac-blueprint__cross--tl" />
            <Crosshair className="sac-blueprint__cross sac-blueprint__cross--tr" />
            <Crosshair className="sac-blueprint__cross sac-blueprint__cross--bl" />
            <Crosshair className="sac-blueprint__cross sac-blueprint__cross--br" />
            <img alt="" aria-hidden="true" className="sac-blueprint__portrait" src={hero.portraitSrc} />
            <div className="sac-blueprint__label sac-blueprint__label--top">
              <strong>{copy.profile}</strong>
              <span>GAOYI WU / 2026</span>
            </div>
            <div className="sac-blueprint__label sac-blueprint__label--left">
              <strong>SPEC.001</strong>
              <span>FOCUS : LLM SECURITY</span>
              <span>METHOD: ADVERSARIAL ML</span>
              <span>SYSTEM: MULTI-AGENT</span>
            </div>
            <div className="sac-blueprint__label sac-blueprint__label--right">
              <strong>{copy.focus}</strong>
              {skills.slice(0, 3).map((group) => (
                <span key={group.title}>{group.title}</span>
              ))}
            </div>
            <figcaption>HOBOKEN, NJ / 40.7357° N · 74.0301° W</figcaption>
          </figure>
        </Reveal>
      </div>

      <div className="sac-about__right">
        <Reveal>
          <div aria-label={copy.focus} className="sac-flow">
            {['SECURE', 'MEASURE', 'DEPLOY'].map((label, index) => (
              <span className="sac-flow__item" key={label}>
                <span className="sac-flow__node">
                  <strong>{index + 1}</strong>
                  <small>{label}</small>
                </span>
                {index < 2 ? <i aria-hidden="true" /> : null}
              </span>
            ))}
          </div>
        </Reveal>

        <Reveal>
          <div className="sac-signals">
            <header>
              <h3>{copy.signal}</h3>
              <span>VERIFIED / 2026</span>
            </header>
            <ul>
              {proof.map((item, index) => (
                <li key={item.value}>
                  <span className="sac-signals__index">{String(index + 1).padStart(2, '0')}</span>
                  <strong>{item.value}</strong>
                  <span>{item.label}</span>
                  <b>LIVE</b>
                </li>
              ))}
            </ul>
          </div>
        </Reveal>

        <Reveal>
          <div className="sac-education">
            <h3>{copy.education}</h3>
            {education.map((entry) => (
              <article key={entry.school}>
                <span>{entry.period}</span>
                <strong>{entry.school}</strong>
                <p>{entry.degree}</p>
              </article>
            ))}
          </div>
        </Reveal>
      </div>
    </section>
  )
}
