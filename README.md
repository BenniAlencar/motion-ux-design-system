# Motion/UX Design System

**Sistema autonomo de design de sites e UI/UX superior a Awwwards.**

Voce abre o projeto, solicita um site, o sistema solicita os dados/assets necessarios, gera instrucoes para midias nao-codigo, e entrega autonomamente algo **magnanimo e superior**.

**Sem prompts manuais. Sem adivinhacao. Apenas resultados.**

---

## Fluxo Autonomo

### Passo 1: Voce Abre e Pede

```
Voce: "Quero um hero com scroll que revela produtos"
```

### Passo 2: Sistema Carrega Automaticamente

A IDE carrega **TODAS as 26 skills** automaticamente:
- cerebro-orquestrador
- gsap-scrolltrigger, lenis, scrollsmoother, observer, flip
- r3f-threejs-drei, spline-runtime, webgpu-gpgpu, lygia
- rive, lottiefiles
- accessibility-a11y, performance-budget
- asset-gate, quality-gate
- ... e todas as outras

### Passo 3: Cerebro Classifica

```yaml
intent_type: hero_scroll
surface: hero
narrative:
  - act: introducao (scroll 0-0.3)
  - act: revelacao (scroll 0.3-0.7)
  - act: climax (scroll 0.7-1.0)
```

### Passo 4: Asset Gate Solicita Assets

O sistema gera **instrucoes claras de midia nao-codigo**:

```
Para entrega final, enviar:

1. Logo (SVG ou PNG, 500x500 min, fundo transparente)

2. Imagens:
   - Hero background (1920x1080, JPG, < 500kB)
     Sugestoes: Unsplash "minimal blue background"
   - Product shot 1 (800x600, PNG, fundo transparente)
   - Product shot 2 (800x600, PNG, fundo transparente)

3. Fontes: Inter (Google Fonts, gratuito)
```

### Passo 5: Sistema Entrega Prototype

Enquanto aguarda assets, o sistema entrega:
- Codigo completo (Next.js/React)
- Placeholders claramente identificados
- Instrucoes de como substituir placeholders
- Run snapshot com trace_id, approved_by, timestamp

### Passo 6: Voce Envia Assets

Voce envia logo e imagens conforme instrucoes.

### Passo 7: Sistema Atualiza para Final

O sistema:
- Substitui placeholders pelos assets reais
- Roda quality gate completo
- Gera evidence packet (screenshots, metrics, video demos)
- Entrega versao final pronta para deploy

---

## Skills (26 total)

### Core
| Skill | Funcao |
|-------|--------|
| cerebro-orquestrador | Roteador e classificador (carrega primeiro) |

### GSAP Ecosystem
| gsap-scrolltrigger | ScrollTrigger, pin, scrub, parallax |
| scrollsmoother | ScrollSmoother (Club GSAP) |
| observer | Hover, press, enter, leave |
| flip | Layout transitions sem flash |

### Scroll
| lenis | Smooth scroll + integracao GSAP |
| locomotive-scroll | Locomotive Scroll |

### Animation
| motion-framer | Framer Motion (React) |
| animejs | Anime.js (CSS, SVG, JS) |
| theatrejs | Theatre.js (timelines visuais) |

### 3D / WebGL
| r3f-threejs-drei | Three.js + R3F + Drei |
| spline-runtime | Spline 3D |
| webgpu-gpgpu | WebGPU + GPGPU (50k particulas) |
| lygia | Lygia shaders (SDF, noise, palette) |
| webgpu-wgsl-tsl | WebGPU + WGSL + TSL |
| pixi | Pixi.js (2D WebGL) |
| ogl | OGL (WebGL leve) |
| curtains | Curtains.js (WebGL + DOM) |

### Page Transitions
| barba | Barba.js (page transitions) |
| swup | Swup (modern transitions) |

### Animation Formats
| rive | Rive (state machines) |
| lottiefiles | Lottie / dotLottie |

### Physics / Generative
| rapier | Rapier physics (3D) |
| p5js | p5.js (generative art) |

### Audio
| tonejs | Tone.js (audio interativo) |

### Qualidade
| accessibility-a11y | WCAG, keyboard, focus, a11y |
| performance-budget | Frame budget, memory, bundle |
| asset-gate | Asset intake, manifest, instrucoes |
| quality-gate | QA, acceptance, evidence, rollback |

---

## Estrutura de uma Skill

```
skills/<skill>/
├── SKILL.md              # Manifesto, stack, agentes
├── AGENTS.md             # Enxame de agentes (analyst, planner, implementer, reviewer, qa)
├── WORKFLOW.md           # Fluxo obrigatorio passo-a-passo
├── INPUT_CONTRACT.yaml   # Schema de entrada
├── OUTPUT_CONTRACT.yaml  # Schema de saida
├── PATTERNS.md           # Patterns reutilizaveis
├── IMPLEMENTATION.md     # Codigo de referencia
├── QUALITY_GATE.md       # Criterios de qualidade
├── EVALS.md              # Testes e acceptance
└── examples/             # Exemplos de uso
```

---

## Exemplo Completo

### Entrada

```yaml
user_request: "Quero um hero com scroll que revela produtos"
context:
  project_name: "Minha Landing"
  brand_name: "Minha Marca"
  industry: tech
constraints:
  performance_budget_ms: 16
  a11y_target: AA
  motion_policy: full
assets_provided:
  logo: false
  copy: true
  images: []
```

### Saida (Cerebro)

```yaml
intent_type: hero_scroll
selected_skills:
  - gsap-scrolltrigger (primary)
  - lenis (primary)
  - accessibility-a11y (required)
  - performance-budget (required)
  - asset-gate (required)
  - quality-gate (required)

asset_gate_report:
  asset_state: asset_pending
  delivery_state: prototype
  blocking_assets:
    - type: logo
      status: missing
    - type: images
      status: missing
      count: 3
  asset_instructions: |
    "Para entrega final, enviar:
     1. Logo em SVG ou PNG (min 500x500, fundo transparente)
     2. 3 imagens (hero bg + 2 product shots)
     3. Confirmar fonte: Inter (Google Fonts)"

next_action: "Aguardar logo e imagens para final delivery"
```

### Saida (GSAP ScrollTrigger)

```tsx
'use client'
import { useEffect, useRef } from 'react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

export function HeroScroll() {
  const heroRef = useRef<HTMLDivElement>(null)
  const productsRef = useRef<HTMLDivElement>(null)
  
  useEffect(() => {
    const ctx = gsap.context()
    
    gsap.to(heroRef.current?.querySelector('.hero_title'), {
      scrollTrigger: {
        trigger: heroRef.current,
        start: 'top top',
        end: 'bottom top',
        scrub: true,
      },
      y: -100,
      opacity: 0,
      duration: 1,
    })
    
    return () => ctx.revert()
  }, [])
  
  return (
    <section ref={heroRef} className="hero">
      <h1 className="hero_title">Titulo</h1>
    </section>
  )
}
```

### Saida (Asset Gate)

```markdown
## Instrucoes de Assets - Minha Landing

Para entrega final, enviar:

### 1. Logo
- Formato: SVG ou PNG
- Tamanho: 500x500 min
- Fundo: transparente

### 2. Hero Background
- Formato: JPG
- Dimensoes: 1920x1080
- Tamanho: < 500 kB
- Estilo: Iluminacao natural, fundo neutro, tons de azul e cinza
- Sugestoes: Unsplash "minimal blue background"

### 3. Product Shots (2)
- Formato: PNG (fundo transparente)
- Dimensoes: 800x600
- Estilo: Produto isolado, iluminacao studio
```

### Saida (Quality Gate)

```yaml
quality_gate_report:
  accepted: true
  accepted_with_warnings: true
  warnings:
    - "Contraste 4.2:1 em texto secundario (aceito)"
  blocking_issues: []
  delivery_state: prototype
  
  evidence_packet:
    screenshots: 5
    lighthouse:
      performance: 87
      accessibility: 94
    frame_time_p95_ms: 14
    bundle_js_kb: 142
  
  rollback_ready: true
```

---

## Como Usar

### Em uma IDE (Perplexity, Google Antigravity, etc)

1. **Clone o repositorio** ou adicione como dependencia
2. **Configure a IDE** para ler `skills/` automaticamente em toda solicitacao
3. **Voce pede** um site em linguagem natural
4. **Sistema executa** fluxo autonomo completo
5. **Voce recebe** codigo + instrucoes de assets + evidence packet

### Comandos Uteis

```bash
# Ver todas as skills
ls skills/

# Ver estrutura de uma skill
cat skills/gsap-scrolltrigger/SKILL.md
cat skills/gsap-scrolltrigger/WORKFLOW.md

# Ver exemplo de uso
cat skills/gsap-scrolltrigger/examples/hero-scroll.tsx
```

---

## Status

**v1.0.0** - Sistema autonomo funcional

- [x] Cerebro-orquestrador completo
- [x] Asset Gate com instrucoes de midia
- [x] Quality Gate com evidence packet
- [x] 26 skills dedicadas
- [ ] Exemplos em `skills/*/examples/`
- [ ] Templates em `templates/`
- [ ] Evals em `evals/`

---

## Repositorio

https://github.com/BenniAlencar/motion-ux-design-system

## License

MIT
