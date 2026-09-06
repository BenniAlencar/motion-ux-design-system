---
name: lenis
description: Lenis smooth scroll com integracao GSAP
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - lenis
    - smooth scroll
    - scroll suave
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
  - gsap-scrolltrigger
outputs:
  - lenis_config
  - gsap_integration
  - performance_report
---

# Lenis Smooth Scroll

## Stack

- Lenis 1.2+
- GSAP ScrollTrigger (integracao)

## Enxame de Agentes

1. **Scroll Analyst** - Analisa necessidade de smooth scroll
2. **Config Engineer** - Configura duration, easing, touch
3. **GSAP Integrator** - Sync com ScrollTrigger
4. **Performance Reviewer** - Verifica FPS, jank, mobile

## Configuracao Padrao

```ts
import Lenis from 'lenis'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
  smoothTouch: false,
  syncTouch: false,
  gestureOrientation: 'vertical',
  touchMultiplier: 1.5,
  infinite: false,
})

// Sync com GSAP - SEGREDO APPLE
lenis.on('scroll', ScrollTrigger.update)
gsap.ticker.add((time) => {
  lenis.raf(time * 1000)
})
gsap.ticker.lagSmoothing(0)
ScrollTrigger.normalizeScroll(true)
```

## Performance Checklist

- [ ] duration entre 0.8-1.5s
- [ ] smoothTouch false em mobile (performance)
- [ ] lagSmoothing(0) para sync perfeito
- [ ] normalizeScroll(true) para consistencia
- [ ] Testar em mobile com CPU limitada
