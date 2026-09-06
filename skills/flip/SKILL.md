---
name: flip
description: GSAP Flip para transicoes de layout sem flash
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - flip
    - gsap flip
    - layout transition
    - expand card
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
  - gsap-scrolltrigger
outputs:
  - flip_plan
  - state_management
  - integration_code
---

# GSAP Flip

## Stack

- GSAP Flip
- ScrollTrigger (opcional)

## Enxame de Agentes

1. **Layout Analyst** - Analisa transicoes de layout necessarias
2. **State Manager** - Planeja Flip.getState e restore
3. **Animation Designer** - Desenha transicao (duration, ease, props)
4. **Integration Engineer** - Gera codigo React/Next

## Expand Card para Modal

```tsx
import Flip from 'gsap/Flip'

function expandCard(card: HTMLElement) {
  const state = Flip.getState(card, { props: 'borderRadius,backgroundColor' })
  
  card.classList.add('expanded') // CSS: fixed, inset:0, z:100
  
  Flip.from(state, {
    duration: 0.7,
    ease: 'power2.inOut',
    absolute: true, // Usa position absolute durante animacao
    scale: true,
    simple: true,
    onEnter: (els) => gsap.from(els, { opacity: 0 }),
    onLeave: (els) => gsap.to(els, { opacity: 0 }),
  })
}
```

## Filter Lista

```ts
function filterList() {
  const state = Flip.getState('.card')
  
  // Muda DOM: esconde alguns cards
  document.querySelectorAll('.card.hidden').forEach(c => c.style.display = 'none')
  
  Flip.from(state, {
    duration: 0.6,
    ease: 'power2.out',
    stagger: 0.02,
    absolute: true,
  })
}
```

## Props Animadas

```ts
const state = Flip.getState('.card', {
  props: 'borderRadius,backgroundColor,boxShadow',
})

// Muda estado
Flip.from(state, {
  duration: 0.5,
  props: 'borderRadius,backgroundColor,boxShadow',
})
```

## Output

```yaml
flip_plan:
  use_cases:
    - type: expand_card_to_modal
      props: [borderRadius, backgroundColor]
      duration: 0.7
    - type: filter_list
      stagger: 0.02
      duration: 0.6
  integration: react
  absolute_positioning: true
```
