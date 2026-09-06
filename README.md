# Motion/UX Design System

Sistema de skills dedicadas para design de sites e UI/UX.

## Arquitetura

Cada skill e um **enxame declarativo de agentes** com:
- Multiplos papeis (analyst, planner, implementer, reviewer, qa)
- Contratos de entrada e saida
- Workflow obrigatorio
- Patterns e templates
- Evals e acceptance criteria

## Skills (26 total)

### Core
| Skill | Descricao |
|-------|----------|
| cerebro-orquestrador | Roteador e classificador de intencao |

### GSAP Ecosystem
| Skill | Descricao |
|-------|----------|
| gsap-scrolltrigger | GSAP Core + ScrollTrigger |
| scrollsmoother | GSAP ScrollSmoother |
| observer | GSAP Observer (hover, press, enter, leave) |
| flip | GSAP Flip (layout transitions) |

### Scroll
| Skill | Descricao |
|-------|----------|
| lenis | Lenis smooth scroll |
| locomotive-scroll | Locomotive Scroll |

### Animation
| Skill | Descricao |
|-------|----------|
| motion-framer | Framer Motion (React) |
| animejs | Anime.js (CSS, SVG, JS) |
| theatrejs | Theatre.js (timelines visuais) |

### 3D / WebGL
| Skill | Descricao |
|-------|----------|
| r3f-threejs-drei | Three.js + R3F + Drei |
| spline-runtime | Spline 3D + Runtime |
| webgpu-gpgpu | WebGPU + GPGPU |
| lygia | Lygia shader library |
| webgpu-wgsl-tsl | WebGPU + WGSL + TSL |
| pixi | Pixi.js (2D WebGL) |
| ogl | OGL (WebGL leve) |
| curtains | Curtains.js (WebGL + DOM) |

### Page Transitions
| Skill | Descricao |
|-------|----------|
| barba | Barba.js (page transitions) |
| swup | Swup (modern page transitions) |

### Animation Formats
| Skill | Descricao |
|-------|----------|
| rive | Rive (state machines) |
| lottiefiles | Lottie / dotLottie |

### Physics / Generative
| Skill | Descricao |
|-------|----------|
| rapier | Rapier physics (3D) |
| p5js | p5.js (generative art) |

### Audio
| Skill | Descricao |
|-------|----------|
| tonejs | Tone.js (audio interativo) |

### Qualidade
| Skill | Descricao |
|-------|----------|
| accessibility-a11y | WCAG, keyboard, focus, a11y |
| performance-budget | Frame budget, memory, bundle |
| asset-gate | Asset intake, manifest, rights |
| quality-gate | QA, acceptance, evidence, rollback |

## Uso em IDEs

1. Carregue `cerebro-orquestrador` primeiro
2. Cerebro classifica a intencao e seleciona skills
3. Cada skill executa seu enxame de agentes
4. Asset Gate verifica assets antes de entrega final
5. Quality Gate valida antes de publicar

## Estrutura de uma Skill

```
skills/<skill>/
├── SKILL.md           # Manifesto e instrucoes
├── AGENTS.md          # Enxame de agentes
├── WORKFLOW.md        # Fluxo obrigatorio
├── INPUT_CONTRACT.yaml
├── OUTPUT_CONTRACT.yaml
├── PATTERNS.md        # Patterns reutilizaveis
├── IMPLEMENTATION.md  # Codigo de referencia
├── QUALITY_GATE.md    # Criterios de qualidade
├── EVALS.md           # Avaliacao e acceptance
└── examples/          # Exemplos de uso
```

## Status

v1.0.0 - 26 skills dedicadas Motion/UX para design de sites e UI

## Repositorio

https://github.com/BenniAlencar/motion-ux-design-system
