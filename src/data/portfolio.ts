import type { Language, PortfolioContent, PortfolioData } from '../types/portfolio'

export const portfolio: PortfolioData = {
  intro: {
    brandMark: 'GW',
    footerWordmark: 'GAOYI',
    pages: [
      {
        id: 'cover',
        meta: 'Apr 2026',
        fromLabel: 'From,',
        fromLines: ['Gaoyi Wu', 'Applied AI Engineer', 'ML Engineer'],
        toLabel: 'To,',
        toLines: ['Recruiters, hiring managers,', 'and collaborators'],
        portfolioLabel: 'AI Portfolio',
        displayName: 'GAOYI',
        entryLabel: 'Enter Portfolio',
      },
      {
        id: 'about',
        heading: 'About Me',
        profileName: 'Gaoyi Wu',
        profileRole: 'Applied AI Engineer / ML Engineer',
        portraitSrc: '/assets/gaoyi-wu-portrait-studio.jpg',
        paragraphs: [
          'I turn AI research into products, pipelines, and systems people can actually use.',
          'LLM systems. ML infra. AI security. Product-minded engineering.',
        ],
      },
      {
        id: 'note',
        heading: 'Disclaimer',
        sections: [
          {
            title: 'Built For Review',
            lines: [
              'A focused portfolio for Applied AI, ML Engineering, AI Infra, and AI Security roles.',
            ],
          },
          {
            title: 'Public + In Progress',
            lines: [
              'XClaw and iSeal are public.',
              'Active lab work stays high-level while it is still in progress.',
            ],
          },
          {
            title: 'What To Notice',
            lines: [
              'Research-to-product thinking, clear communication, and practical system ownership.',
            ],
          },
        ],
      },
    ],
  },
  profile: {
    name: 'Gaoyi Wu',
    eyebrow: 'Applied AI Engineer / ML Engineer',
    headline: 'Applied AI Engineer building practical ML systems and production-ready AI products',
    summary:
      'I build practical AI products, machine learning pipelines, and infrastructure that connect research ideas to systems teams can actually ship and maintain.',
    portraitSrc: '/assets/gaoyi-wu-portrait-studio.jpg',
    introLabel: 'Hello!',
    quote:
      'I focus on the space between research ideas and usable systems, where model quality, delivery speed, and engineering discipline all matter.',
    heroStat: 'AI + ML',
    heroStatLabel: 'Research depth, production thinking, and system ownership in one profile.',
  },
  primaryLinks: [
    { label: 'Enter Portfolio', href: '#portfolio-main' },
    { label: 'Resume', href: '/resume/gaoyi-wu-resume.pdf' },
    { label: 'LinkedIn', href: 'https://www.linkedin.com/in/gaoyiwu/' },
    { label: 'GitHub', href: 'https://github.com/Alfred768' },
  ],
  capabilities: [
    {
      kicker: '01',
      title: 'Applied AI Products',
      summary:
        'User-facing AI experiences built around product utility, orchestration, and clean interaction design rather than isolated demos.',
      imageSrc: '/assets/xclaw-product-ui.png',
      imageAlt: 'XClaw product website preview',
    },
    {
      kicker: '02',
      title: 'ML Engineering',
      summary:
        'Training, evaluation, fine-tuning, and serving workflows that turn ML ideas into repeatable systems with measurable behavior.',
      imageSrc: '/assets/xclaw-product-proof.png',
      imageAlt: 'XClaw GitHub repository preview',
    },
    {
      kicker: '03',
      title: 'AI Security Research',
      summary:
        'Security, ownership verification, and robustness work for LLM systems, backed by ongoing research and implementation.',
      imageSrc: '/assets/iseal-paper.png',
      imageAlt: 'iSeal paper preview from arXiv',
    },
  ],
  experience: [
    {
      company: 'DHL Express',
      role: 'AI/ML Engineer Intern',
      location: 'Shanghai, China',
      period: 'May 2024 - Aug 2024',
      logoSrc: '/assets/logos/dhl-express.svg',
      logoAlt: 'DHL Express logo',
      highlights: [
        'Productionized churn-prediction and sentiment models as containerized services on AWS.',
        'Built automated retraining and drift-aware workflows with EventBridge, MLflow, SQL, and Pandas.',
        'Improved model delivery reliability through CI/CD and release automation.',
      ],
    },
    {
      company: 'Intellisys Lab',
      role: 'Research Assistant',
      location: 'Hoboken, NJ',
      period: 'Sep 2024 - Present',
      logoSrc: '/assets/logos/intellisys-lab.svg',
      logoAlt: 'Intellisys Lab logo',
      highlights: [
        'Built federated LLM and fine-tuning workflows on Kubernetes for distributed edge environments.',
        'Orchestrated data ingestion, scheduled retraining, and experiment tracking with MLflow and Kafka.',
        'Designed security and robustness evaluation workflows for transformer backdoor detection and privacy-aware RAG.',
      ],
    },
    {
      company: 'Stevens Institute of Technology',
      role: 'Graduate Teaching Assistant',
      location: 'Hoboken, NJ',
      period: '2025 - Present',
      logoSrc: '/assets/logos/stevens.svg',
      logoAlt: 'Stevens Institute of Technology logo',
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
      period: '2024 - 2026',
      logoSrc: '/assets/logos/stevens.svg',
      logoAlt: 'Stevens Institute of Technology logo',
    },
    {
      school: 'Shenzhen University',
      degree: 'B.A. Logistics Management',
      period: '2020 - 2024',
      logoSrc: '/assets/logos/shenzhen-university.png',
      logoAlt: 'Shenzhen University logo',
    },
  ],
  proofPoints: [
    {
      title: 'Research grounded',
      detail:
        'Current lab work and published security research keep the technical foundation strong.',
    },
    {
      title: 'Production minded',
      detail:
        'I think in terms of deployment paths, reliability, data flow, and maintainable systems.',
    },
    {
      title: 'Clear communicator',
      detail:
        'Teaching assistant work and cross-team collaboration make complex topics easy to explain.',
    },
  ],
  featuredWork: [
    {
      title: 'XClaw',
      tag: 'Applied AI Product',
      summary:
        'A desktop interface for orchestrating AI agents, integrating model access, tool use, and multi-channel automation.',
      href: 'https://github.com/Alfred768/xclaw',
      linkLabel: 'Open Repo',
      secondaryHref: 'https://www.x-claw.shop/',
      secondaryLabel: 'Live Site',
      imageSrc: '/assets/xclaw-product-ui.png',
      imageAlt: 'XClaw live site preview',
      logoSrc: '/assets/xclaw-icon.png',
      logoAlt: 'XClaw logo',
      stack: ['AI Agents', 'Electron', 'React'],
    },
    {
      title: 'iSeal',
      tag: 'AI Security Research',
      summary:
        'A watermarking and ownership-verification system for black-box LLMs, accepted to AAAI 2026.',
      href: 'https://arxiv.org/pdf/2511.08905',
      linkLabel: 'Read Paper',
      imageSrc: '/assets/iseal-paper.png',
      imageAlt: 'iSeal paper preview',
      stack: ['LLM Security', 'Watermarking', 'Research'],
    },
    {
      title: 'LangChain Multi-Agent Auditing & Evaluation Framework',
      tag: 'Applied ML Workflow',
      summary:
        'A multi-agent auditing pipeline for financial workflows with evaluation loops and human feedback.',
      href: 'https://github.com/Alfred768',
      linkLabel: 'Open GitHub',
      stack: ['LangChain', 'Evaluation', 'Workflow'],
    },
    {
      title: 'Ongoing Lab Work',
      tag: 'Federated LLM Infrastructure',
      summary:
        'Current research and implementation work on federated learning, ML infra, LLM evaluation, and robustness.',
      href: '#experience',
      linkLabel: 'See Experience',
      stack: ['Kubernetes', 'MLflow', 'Kafka'],
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
  notes: [
    {
      title: 'Previous work experience',
      summary:
        'DHL, Stevens, and current lab work show how I move between applied research, delivery, and collaboration.',
      href: '#experience',
      ctaLabel: 'See Experience',
    },
    {
      title: 'Technology skill',
      summary:
        'My stack spans model development, infra, backend systems, and the frontend layer needed to ship an AI product.',
      href: '#skills',
      ctaLabel: 'See Skills',
    },
    {
      title: 'Open roles',
      summary:
        'I am focused on Applied AI Engineer and ML Engineer roles where product outcomes and engineering quality both matter.',
      href: 'https://www.linkedin.com/in/gaoyiwu/',
      ctaLabel: 'Open LinkedIn',
    },
  ],
  tickerItems: [
    'Applied AI Engineer',
    'ML Engineer',
    'LLM Systems',
    'AI Security',
    'ML Infra',
    'Full-Stack AI',
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

export const portfolioByLanguage: Record<Language, PortfolioContent> = {
  en: {
    navigation: {
      about: 'About',
      research: 'Research',
      experience: 'Experience',
      projects: 'Projects',
      skills: 'Skills',
      education: 'Education',
      contact: 'Contact',
      resume: 'Resume',
      openMenu: 'Open navigation',
      closeMenu: 'Close navigation',
    },
    hero: {
      name: 'Gaoyi Wu',
      role: 'AI Algorithm Engineer',
      specialization: 'LLM Security × Multi-Agent Systems × Applied ML',
      summary:
        'I build secure, measurable AI systems—from research-grade algorithms to production ML pipelines that hold up under real-world constraints.',
      location: 'Hoboken, New Jersey',
      availability: 'Open to AI Algorithm & Applied AI / ML roles',
      portraitSrc: '/assets/gaoyi-wu-cutout.png',
      portraitAlt: 'Portrait of Gaoyi Wu',
      resumeLabel: 'View Resume',
      contactLabel: 'Contact Me',
    },
    proof: [
      { value: 'AAAI 2026', label: 'LLM ownership verification' },
      { value: '2 Published Papers', label: 'LLM security & agent systems' },
      { value: '100+ Edge Devices', label: 'Federated fine-tuning at scale' },
      { value: '61% → 94% Accuracy', label: 'AG News over DP baseline' },
    ],
    researchEyebrow: 'Selected Research',
    researchHeading: 'Algorithms built to survive adversarial conditions.',
    researchIntro:
      'My research focuses on the failure modes that appear when powerful models meet hostile users, opaque systems, and real deployment constraints.',
    research: [
      {
        id: 'iseal',
        number: '01',
        title: 'iSeal',
        subtitle: 'Encrypted Fingerprinting for Reliable LLM Ownership Verification',
        venue: 'AAAI 2026',
        period: 'May 2025 — Aug 2025',
        summary:
          'A cryptographic key-bound fingerprinting system that keeps ownership verification reliable even when a model thief controls the full inference process.',
        contributions: [
          'Trained a LoRA-based key-bound encoder in 5 minutes on an A100—46× faster than the WLM baseline.',
          'Reached 100% fingerprint success rate across 12 LLMs from 125M to 13B parameters.',
          'Maintained verification under 10+ attacks, Alpaca fine-tuning, and 8/16-bit quantization.',
        ],
        benchmarkValue: '100% FSR',
        benchmarkLabel: 'Across 12 LLMs under collusion-based unlearning and response manipulation',
        detailLabel: 'Read methodology',
        collapseLabel: 'Hide methodology',
        detail:
          'iSeal binds an HMAC-SHA256 key to both a model-side encoder and an external probing process. Similarity-aware verification and a Bayesian threshold separate ownership evidence from harmless model variation while resisting verification-time attacks.',
        tags: ['LLM Security', 'Fingerprinting', 'LoRA', 'Adversarial Evaluation'],
        imageSrc: '/assets/iseal-editorial-diagram.webp',
        imageAlt: 'Editorial diagram of encrypted LLM ownership verification',
        links: [{ label: 'Read Paper', href: 'https://arxiv.org/abs/2511.08905' }],
      },
      {
        id: 'webweaver',
        number: '02',
        title: 'WebWeaver',
        subtitle: 'Breaking Topology Confidentiality in LLM Multi-Agent Systems',
        venue: 'arXiv 2026',
        period: 'Sep 2025 — Mar 2026',
        summary:
          'A topology inference attack that reconstructs an LLM multi-agent communication graph by compromising one arbitrary agent and observing only agent contexts.',
        contributions: [
          'Removed the unrealistic requirement to compromise the administrative node or query agent identities.',
          'Designed both a covert jailbreak-based path and a fully jailbreak-free diffusion path.',
          'Outperformed state-of-the-art baselines by about 60% inference accuracy under active defenses.',
        ],
        benchmarkValue: '~60%',
        benchmarkLabel: 'Higher inference accuracy than SOTA baselines under active anti-jailbreak defenses',
        detailLabel: 'Read methodology',
        collapseLabel: 'Hide methodology',
        detail:
          'WebWeaver infers topology from contextual traces rather than explicit identities. Its diffusion design uses masking to preserve known graph structure while recovering missing communication links, allowing stealthier inference when jailbreaks are blocked.',
        tags: ['Multi-Agent Systems', 'Topology Inference', 'Diffusion', 'AI Security'],
        imageSrc: '/assets/webweaver-editorial-diagram.webp',
        imageAlt: 'Editorial diagram of multi-agent topology inference',
        links: [{ label: 'Read Paper', href: 'https://arxiv.org/abs/2603.11132' }],
      },
    ],
    experienceEyebrow: 'Applied ML Experience',
    experienceHeading: 'Research depth, measured in deployed outcomes.',
    experienceIntro:
      'I work across training, evaluation, security, and infrastructure—then tie each system back to a measurable operating result.',
    experience: [
      {
        company: 'Intellisys Lab',
        role: 'Research Assistant',
        location: 'Hoboken, NJ',
        period: 'Sep 2024 — Present',
        logoSrc: '/assets/logos/intellisys-lab.svg',
        logoAlt: 'Intellisys Lab logo',
        highlights: [
          'Scaled privacy-preserving federated fine-tuning to 100+ edge devices, improving AG News accuracy from 61% to 94%.',
          'Built activation-based backdoor detection that reduced adversarial injection success from above 90% to below 30%.',
          'Designed stage-level RAG evaluation that isolated retrieval and generation regressions and raised answer quality by 15%.',
        ],
      },
      {
        company: 'DHL Express',
        role: 'AI/ML Engineer Intern',
        location: 'Shanghai, China',
        period: 'May 2024 — Aug 2024',
        logoSrc: '/assets/logos/dhl-express.svg',
        logoAlt: 'DHL Express logo',
        highlights: [
          'Built an XGBoost churn model on about 12K customer records, improving retention precision from 0.61 to 0.79.',
          'Fine-tuned a DHL-domain BERT sentiment model to 0.92 F1 versus a 0.76 zero-shot baseline.',
          'Implemented PSI-triggered retraining with MLflow auditability, cutting reporting latency by 30%.',
        ],
      },
    ],
    skillsEyebrow: 'Technical Index',
    skillsHeading: 'The systems behind the research.',
    skillsIntro:
      'A focused stack for model development, adversarial evaluation, agent orchestration, and production infrastructure.',
    skills: [
      {
        title: 'LLM & Generative AI',
        items: ['PyTorch', 'Hugging Face Transformers', 'SFT', 'LoRA', 'RLHF / DPO', 'RAG', 'Prompt Engineering'],
      },
      {
        title: 'ML Security Research',
        items: ['LLM Fingerprinting', 'Watermarking', 'Topology Inference', 'Federated Learning', 'Adversarial Evaluation'],
      },
      {
        title: 'Agent Systems',
        items: ['LangChain', 'Multi-Agent Orchestration', 'Tool Use', 'Topology Analysis', 'Autonomous Workflows'],
      },
      {
        title: 'Infrastructure',
        items: ['Python', 'FastAPI', 'Kafka', 'Docker', 'Kubernetes', 'AWS', 'MLflow'],
      },
    ],
    educationEyebrow: 'Education',
    educationHeading: 'Computer science, grounded in systems thinking.',
    education: [
      {
        school: 'Stevens Institute of Technology',
        degree: 'M.S. Computer Science',
        location: 'Hoboken, NJ',
        period: 'Expected May 2026',
        logoSrc: '/assets/logos/stevens.svg',
        logoAlt: 'Stevens Institute of Technology logo',
      },
      {
        school: 'Shenzhen University',
        degree: 'B.Mgmt. Logistics',
        location: 'Shenzhen, China',
        period: 'July 2024',
        logoSrc: '/assets/logos/shenzhen-university.png',
        logoAlt: 'Shenzhen University logo',
      },
    ],
    contact: {
      eyebrow: 'Get in Touch',
      heading: 'Building secure AI that works beyond the benchmark.',
      summary:
        'I am open to AI Algorithm Engineer and Applied AI / ML Engineer roles where research quality and system ownership matter.',
      emailLabel: 'Email',
      email: 'criswu20010728@gmail.com',
      linkedInLabel: 'LinkedIn',
      linkedInHref: 'https://www.linkedin.com/in/gaoyiwu/',
      gitHubLabel: 'GitHub',
      gitHubHref: 'https://github.com/Alfred768',
      resumeLabel: 'Resume',
      resumeHref: '/resume/gaoyi-wu-resume.pdf',
      footer: 'Designed and engineered by Gaoyi Wu.',
    },
  },
  zh: {
    navigation: {
      about: '关于',
      research: '研究',
      experience: '经历',
      projects: '项目',
      skills: '技能',
      education: '教育',
      contact: '联系',
      resume: '简历',
      openMenu: '打开导航',
      closeMenu: '关闭导航',
    },
    hero: {
      name: '吴高艺',
      role: 'AI 算法工程师',
      specialization: '大模型安全 × 多智能体系统 × 应用机器学习',
      summary:
        '我专注于构建安全、可衡量的 AI 系统：从研究级算法到能够应对真实约束的生产级机器学习管线。',
      location: '美国新泽西州霍博肯',
      availability: '求职方向：AI 算法 / 应用 AI 与机器学习工程',
      portraitSrc: '/assets/gaoyi-wu-cutout.png',
      portraitAlt: '吴高艺个人照片',
      resumeLabel: '查看简历',
      contactLabel: '联系我',
    },
    proof: [
      { value: 'AAAI 2026', label: '大模型所有权验证' },
      { value: '2 篇研究论文', label: '大模型安全与多智能体系统' },
      { value: '100+ 边缘设备', label: '大规模联邦微调' },
      { value: '61% → 94% 准确率', label: 'AG News，相较差分隐私基线' },
    ],
    researchEyebrow: '代表性研究',
    researchHeading: '为对抗环境而设计的算法。',
    researchIntro:
      '我的研究关注强大模型在面对恶意用户、黑盒系统与真实部署约束时暴露出的关键失效模式。',
    research: [
      {
        id: 'iseal',
        number: '01',
        title: 'iSeal',
        subtitle: '面向可靠大模型所有权验证的加密指纹',
        venue: 'AAAI 2026',
        period: '2025 年 5 月 — 2025 年 8 月',
        summary:
          '一种与密码学密钥绑定的大模型指纹系统，即使模型窃取者完全控制推理流程，也能保持可靠的所有权验证。',
        contributions: [
          '在 A100 上用 5 分钟完成基于 LoRA 的密钥编码器训练，速度达到 WLM 基线的 46 倍。',
          '在 12 个、规模从 125M 到 13B 的大模型上实现 100% 指纹成功率。',
          '在 10+ 种攻击、Alpaca 微调及 8/16 位量化后仍保持可靠验证。',
        ],
        benchmarkValue: '100% FSR',
        benchmarkLabel: '12 个大模型，在串谋式指纹遗忘与响应操控下',
        detailLabel: '查看方法',
        collapseLabel: '收起方法',
        detail:
          'iSeal 将 HMAC-SHA256 密钥同时绑定到模型侧编码器与外部探测流程。系统通过相似度验证与贝叶斯阈值，将所有权证据和无害的模型波动区分开，并抵抗验证阶段攻击。',
        tags: ['大模型安全', '模型指纹', 'LoRA', '对抗评估'],
        imageSrc: '/assets/iseal-editorial-diagram.webp',
        imageAlt: '大模型加密所有权验证示意图',
        links: [{ label: '阅读论文', href: 'https://arxiv.org/abs/2511.08905' }],
      },
      {
        id: 'webweaver',
        number: '02',
        title: 'WebWeaver',
        subtitle: '突破大模型多智能体系统的拓扑保密性',
        venue: 'arXiv 2026',
        period: '2025 年 9 月 — 2026 年 3 月',
        summary:
          '一种多智能体拓扑推断攻击：仅攻陷任意一个智能体，并只观察上下文，即可重建完整通信图。',
        contributions: [
          '移除了必须控制管理节点或直接查询智能体身份的不现实假设。',
          '同时设计隐蔽越狱路径与完全不依赖越狱的扩散路径。',
          '在主动防御下，推断准确率相较现有最佳基线提升约 60%。',
        ],
        benchmarkValue: '约 60%',
        benchmarkLabel: '主动反越狱防御下，相较 SOTA 基线的推断准确率提升',
        detailLabel: '查看方法',
        collapseLabel: '收起方法',
        detail:
          'WebWeaver 从上下文痕迹而非显式身份中推断系统拓扑。扩散路径通过掩码保留已知图结构，并恢复缺失通信边，使系统在越狱被阻断时仍能隐蔽推断。',
        tags: ['多智能体系统', '拓扑推断', '扩散模型', 'AI 安全'],
        imageSrc: '/assets/webweaver-editorial-diagram.webp',
        imageAlt: '多智能体拓扑推断示意图',
        links: [{ label: '阅读论文', href: 'https://arxiv.org/abs/2603.11132' }],
      },
    ],
    experienceEyebrow: '应用机器学习经历',
    experienceHeading: '让研究深度转化为可衡量的系统结果。',
    experienceIntro:
      '我的工作覆盖训练、评估、安全与基础设施，并将每个系统最终连接到明确的业务或模型指标。',
    experience: [
      {
        company: 'Intellisys Lab',
        role: '研究助理',
        location: '美国新泽西州霍博肯',
        period: '2024 年 9 月 — 至今',
        logoSrc: '/assets/logos/intellisys-lab.svg',
        logoAlt: 'Intellisys Lab 标志',
        highlights: [
          '将隐私保护联邦微调扩展到 100+ 边缘设备，使 AG News 准确率从 61% 提升到 94%。',
          '构建基于激活值的后门检测，将对抗注入成功率从 90% 以上降至 30% 以下。',
          '设计分阶段 RAG 评估，定位检索与生成回归，使答案质量提升 15%。',
        ],
      },
      {
        company: 'DHL Express',
        role: 'AI/ML 工程师实习生',
        location: '中国上海',
        period: '2024 年 5 月 — 2024 年 8 月',
        logoSrc: '/assets/logos/dhl-express.svg',
        logoAlt: 'DHL Express 标志',
        highlights: [
          '基于约 1.2 万条客户记录构建 XGBoost 流失模型，将留存预测精确率从 0.61 提升至 0.79。',
          '微调 DHL 领域 BERT 情感模型，F1 达到 0.92，高于 0.76 的零样本基线。',
          '实现 PSI 触发重训与 MLflow 审计，将报告延迟降低 30%。',
        ],
      },
    ],
    skillsEyebrow: '技术索引',
    skillsHeading: '支撑研究落地的系统能力。',
    skillsIntro: '覆盖模型开发、对抗评估、智能体编排与生产基础设施的核心技术栈。',
    skills: [
      {
        title: '大模型与生成式 AI',
        items: ['PyTorch', 'Hugging Face Transformers', 'SFT', 'LoRA', 'RLHF / DPO', 'RAG', '提示工程'],
      },
      {
        title: '机器学习安全研究',
        items: ['大模型指纹', '数字水印', '拓扑推断', '联邦学习', '对抗评估'],
      },
      {
        title: '智能体系统',
        items: ['LangChain', '多智能体编排', '工具调用', '拓扑分析', '自主工作流'],
      },
      {
        title: '基础设施',
        items: ['Python', 'FastAPI', 'Kafka', 'Docker', 'Kubernetes', 'AWS', 'MLflow'],
      },
    ],
    educationEyebrow: '教育经历',
    educationHeading: '计算机科学，与系统思维。',
    education: [
      {
        school: 'Stevens Institute of Technology',
        degree: '计算机科学硕士',
        location: '美国新泽西州霍博肯',
        period: '预计 2026 年 5 月毕业',
        logoSrc: '/assets/logos/stevens.svg',
        logoAlt: 'Stevens Institute of Technology 标志',
      },
      {
        school: '深圳大学',
        degree: '物流管理学士',
        location: '中国深圳',
        period: '2024 年 7 月',
        logoSrc: '/assets/logos/shenzhen-university.png',
        logoAlt: '深圳大学标志',
      },
    ],
    contact: {
      eyebrow: '联系我',
      heading: '让安全 AI 走出基准测试，进入真实系统。',
      summary:
        '我正在寻找重视研究质量与系统所有权的 AI 算法工程师、应用 AI 或机器学习工程师岗位。',
      emailLabel: '邮箱',
      email: 'criswu20010728@gmail.com',
      linkedInLabel: 'LinkedIn',
      linkedInHref: 'https://www.linkedin.com/in/gaoyiwu/',
      gitHubLabel: 'GitHub',
      gitHubHref: 'https://github.com/Alfred768',
      resumeLabel: '英文简历',
      resumeHref: '/resume/gaoyi-wu-resume.pdf',
      footer: '由吴高艺设计与开发。',
    },
  },
}
