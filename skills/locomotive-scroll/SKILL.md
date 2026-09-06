---
name: locomotive-scroll
description: Locomotive Scroll para scroll custom com inercia
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - locomotive scroll
    - locomotive
    - custom scroll
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
outputs:
  - locomotive_config
  - sections_plan
  - integration_code
  - fallback_lenis
---

# Locomotive Scroll

## Stack

- locomotive-scroll
- Fallback Lenis (recomendado para projetos novos)

## Enxame de Agentes

1. **Scroll Analyst** - Analisa necessidade de Locomotive vs Lenis
2. **Config Engineer** - Configura inertia, direction, touch
3. **Sections Planner** - Planeja data-scroll-section, data-scroll
4. **Integration Engineer** - Gera codigo React/Next
5. **Fallback Designer** - Cria versao Lenis

## Configuracao Padrao

```ts
import LocomotiveScroll from 'locomotive-scroll'

const scroll = new LocomotiveScroll({
  el: document.getElementById('main'),
  smooth: true,
  direction: 'vertical',
  inertia: 0.9,
  touchMultiplier: 2,
  tablet: {
    smooth: true,
  },
  smartphone: {
    smooth: false, // Desliga smooth em mobile para performance
  },
})

// Refresh apos mudancas de DOM
scroll.on('scroll', (obj) => {
  console.log(obj.scroll.y)
})
```

## Sections

```html
<div data-scroll-section>Hero</div>
<div data-scroll-section>
  <h1 data-scroll data-scroll-speed="2">Titulo com parallax</h1>
</div>
<div data-scroll-section data-scroll-section-bg-color="#000">Fundo preto</div>
```

## Fallback Lenis (Recomendado)

```ts
// Locomotive esta menos mantido. Lenis e recomendado.
import Lenis from 'lenis'

const lenis = new Lenis({ duration: 1.2 })
```

## Output

```yaml
locomotive_plan:
  smoother_available: true
  config:
    smooth: true
    inertia: 0.9
    smartphone_smooth: false
  sections: 3
  parallax_elements: 2
  fallback: lenis_recommended
  integration: nextjs
```
