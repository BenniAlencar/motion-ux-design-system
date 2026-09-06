---
name: scrollsmoother
description: GSAP ScrollSmoother para scroll suave com pin e secoes fixas
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - scrollsmoother
    - gsap scroll
    - smooth scroll gsap
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
  - gsap-scrolltrigger
outputs:
  - scrollsmoother_config
  - sections_plan
  - integration_code
  - fallback_lenis
---

# GSAP ScrollSmoother

## Stack

- GSAP ScrollSmoother (Club GSAP)
- ScrollTrigger
- Fallback Lenis (se nao tiver license GSAP)

## Enxame de Agentes

1. **Scroll Analyst** - Analisa necessidade de ScrollSmoother vs Lenis
2. **Config Engineer** - Configura smoothness, speed, effects
3. **Sections Planner** - Planeja pin, parallax, fixed sections
4. **Integration Engineer** - Gera codigo Next/React
5. **Fallback Designer** - Cria versao Lenis se necessario

## Configuracao Padrao

```ts
import ScrollSmoother from 'gsap/ScrollSmoother'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger, ScrollSmoother)

const smoother = ScrollSmoother.create({
  smooth: 2, // segundos para parar
  effects: 1, // parallax effects
  speed: 1, // velocidade global
  normalizeScroll: true,
  ignoreMobileResize: true,
})

// Se precisar de ScrollTrigger sync
smoother.scrollTop() // retorna scroll atual
```

## Sections com Pin

```ts
// Secao que fica fixa enquanto conteudo scrolla
ScrollTrigger.create({
  trigger: '.fixed_section',
  start: 'top top',
  end: '+=100%',
  pin: true,
  scrub: true,
})
```

## Fallback Lenis

```ts
// Se nao tiver ScrollSmoother (license)
import Lenis from 'lenis'

const lenis = new Lenis({ duration: 1.2 })
lenis.on('scroll', ScrollTrigger.update)
gsap.ticker.add((t) => lenis.raf(t * 1000))
```

## Output

```yaml
scrollsmoother_plan:
  smoother_available: true
  config:
    smooth: 2
    effects: 1
    speed: 1
  sections_pinned: 2
  fallback: lenis
  integration: nextjs
```
