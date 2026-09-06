# Motion/UX Design System

Sistema de skills dedicadas para design de sites e UI/UX.

## Arquitetura

Cada skill e um **enxame declarativo de agentes** com:
- Multiplos papeis (analyst, planner, implementer, reviewer, qa)
- Contratos de entrada e saida
- Workflow obrigatorio
- Patterns e templates
- Evals e acceptance criteria

## Skills

### Core
| Skill | Descricao |
|-------|----------|
| cerebro-orquestrador | Roteador e classificador de intencao |

### Bibliotecas
| Skill | Descricao |
|-------|----------|
| gsap-scrolltrigger | GSAP + ScrollTrigger + Observer + Flip |
| lenis | Lenis smooth scroll + integracao GSAP |
| r3f-threejs-drei | Three.js + R3F + Drei + Shaders |
| spline-runtime | Spline 3D + Runtime Viewer |
| rive | Rive animations + state machines |
| lottiefiles | Lottie JSON + bodymovin |
| webgpu-gpgpu | WebGPU + GPGPU + compute shaders |
| lygia | Lygia shader library |

### Qualidade
| Skill | Descricao |
|-------|----------|
| accessibility-a11y | WCAG, keyboard, focus, screen reader |
| performance-budget | Frame budget, memory, draw calls, bundle |
| asset-gate | Asset intake, manifest, provenance, rights |
| quality-gate | QA, acceptance, evidence, rollback, snapshot |

## Uso em IDEs

1. Carregue `cerebro-orquestrador` primeiro
2. Cerebro classifica a intencao e seleciona skills
3. Cada skill executa seu enxame de agentes
4. Asset Gate verifica assets antes de entrega final
5. Quality Gate valida antes de publicar

## Estrutura de uma Skill

```
skills/<skill>/\n├── SKILL.md           # Manifesto e instrucoes
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

v1.0.0 - Skills dedicadas Motion/UX para design de sites e UI

## Repositorio

https://github.com/BenniAlencar/motion-ux-design-system
