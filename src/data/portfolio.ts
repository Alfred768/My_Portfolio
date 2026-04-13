import type { PortfolioData } from '../types/portfolio'

export const portfolio: PortfolioData = {
  profile: {
    name: 'Gaoyi Wu',
    eyebrow: 'Applied AI Engineer / ML Engineer',
    headline: 'Hybrid AI engineer building applied AI and production ML systems',
    summary:
      'I build practical AI products, machine learning pipelines, and infrastructure that connect research ideas to production-ready systems.',
    portraitSrc: '/assets/gaoyi-wu.jpg',
  },
  primaryLinks: [
    { label: 'View Projects', href: '#projects' },
    { label: 'Resume', href: '/resume/gaoyi-wu-resume.pdf' },
    { label: 'LinkedIn', href: 'https://www.linkedin.com/in/gaoyiwu/' },
    { label: 'GitHub', href: 'https://github.com/Alfred768' },
  ],
  capabilities: [
    {
      title: 'Applied AI Systems',
      summary:
        'LLM workflows, evaluation-heavy applications, and user-facing AI experiences built around practical outcomes.',
    },
    {
      title: 'ML Engineering',
      summary:
        'Training, fine-tuning, experimentation, and model-serving work that turns ML ideas into maintainable systems.',
    },
    {
      title: 'AI Infrastructure',
      summary:
        'Containerized pipelines, distributed workloads, and observability layers for reliable AI development and deployment.',
    },
  ],
  experience: [
    {
      company: 'Intellisys Lab',
      role: 'Research Assistant',
      location: 'Hoboken, NJ',
      period: 'Sep 2024 - Present',
      highlights: [
        'Built federated LLM and fine-tuning workflows on Kubernetes for distributed edge environments.',
        'Orchestrated data ingestion, scheduled retraining, and experiment tracking with MLflow and Kafka.',
        'Designed security and robustness evaluation workflows for transformer backdoor detection and privacy-aware RAG.',
      ],
    },
    {
      company: 'DHL Express',
      role: 'AI/ML Engineer Intern',
      location: 'Shanghai, China',
      period: 'May 2024 - Aug 2024',
      highlights: [
        'Productionized churn-prediction and sentiment models as containerized services on AWS.',
        'Built automated retraining and drift-aware workflows with EventBridge, MLflow, SQL, and Pandas.',
        'Improved model delivery reliability through CI/CD and release automation.',
      ],
    },
    {
      company: 'Stevens Institute of Technology',
      role: 'Graduate Teaching Assistant',
      location: 'Hoboken, NJ',
      period: '2025 - Present',
      highlights: [
        'Supported graduate computer science courses with grading, student guidance, and faculty coordination.',
        'Explained technical concepts clearly across advanced topics and helped students debug their implementations.',
      ],
    },
  ],
  education: [
    {
      school: 'Stevens Institute of Technology',
      degree: 'M.S. Computer Science',
      period: 'Present',
    },
    {
      school: 'Shenzhen University',
      degree: 'B.A. Logistics Management',
      period: 'Jul 2024',
    },
  ],
  proofPoints: [
    'Research-to-production mindset across AI systems and infrastructure',
    'Comfortable with both modeling work and software delivery',
    'Strong fit for recruiter-first scans and technical hiring review',
  ],
  featuredWork: [
    {
      title: 'XClaw',
      tag: 'Applied AI Product',
      summary:
        'A desktop interface for orchestrating AI agents, integrating model access, tool use, and multi-channel automation.',
      href: 'https://github.com/Alfred768/xclaw',
      secondaryHref: 'https://www.x-claw.shop/',
    },
    {
      title: 'iSeal',
      tag: 'AI Security Research',
      summary:
        'A watermarking and ownership-verification system for black-box LLMs, accepted to AAAI 2026.',
      href: 'https://arxiv.org/pdf/2511.08905',
    },
    {
      title: 'LangChain Multi-Agent Auditing & Evaluation Framework',
      tag: 'Applied ML Workflow',
      summary:
        'A multi-agent auditing pipeline for financial workflows with evaluation loops and human feedback.',
      href: 'https://github.com/Alfred768',
    },
    {
      title: 'Ongoing Lab Work',
      tag: 'Federated LLM Infrastructure',
      summary:
        'Current research and implementation work on federated learning, ML infra, LLM evaluation, and robustness.',
      href: '#experience',
    },
  ],
  skills: [
    {
      title: 'AI / ML',
      items: [
        'PyTorch',
        'TensorFlow',
        'Transformers',
        'RAG',
        'LoRA',
        'Federated Learning',
        'Prompt Engineering',
      ],
    },
    {
      title: 'Infra / MLOps',
      items: ['Docker', 'Kubernetes', 'MLflow', 'Kafka', 'AWS ECS', 'EventBridge', 'Jenkins'],
    },
    {
      title: 'Backend / Systems',
      items: ['Python', 'Go', 'Java', 'FastAPI', 'Spring Boot', 'SQL', 'Redis'],
    },
    {
      title: 'Frontend / Product',
      items: ['React', 'TypeScript', 'Electron', 'HTML', 'CSS', 'JavaScript'],
    },
  ],
  contact: {
    email: 'criswu20010728@gmail.com',
    resumeHref: '/resume/gaoyi-wu-resume.pdf',
    links: [
      { label: 'Email', href: 'mailto:criswu20010728@gmail.com' },
      { label: 'LinkedIn', href: 'https://www.linkedin.com/in/gaoyiwu/' },
      { label: 'GitHub', href: 'https://github.com/Alfred768' },
      { label: 'Resume', href: '/resume/gaoyi-wu-resume.pdf' },
    ],
  },
}
