---
name: observer
description: GSAP Observer para hover, press, enter, leave em mobile e desktop
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - observer
    - gsap observer
    - hover mobile
    - press
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
  - gsap-scrolltrigger
outputs:
  - observer_config
  - interaction_map
  - integration_code
---

# GSAP Observer

## Stack

- GSAP Observer
- ScrollTrigger (opcional)

## Enxame de Agentes

1. **Interaction Analyst** - Analisa interacoes necessarias
2. **Observer Configurer** - Configura callbacks
3. **Integration Engineer** - Gera codigo React/Next
4. **Mobile Tester** - Testa touch vs mouse

## Observers Comuns

```ts
import { Observer } from 'gsap/Observer'

gsap.registerPlugin(Observer)

// Hover/Leave
Observer.create({
  target: '.interactive',
  onHoverStart: (e) => gsap.to(e.target, { scale: 1.05 }),
  onHoverEnd: (e) => gsap.to(e.target, { scale: 1 }),
})

// Press/Release (touch e mouse)
Observer.create({
  target: '.button',
  onPressStart: (e) => gsap.to(e.target, { scale: 0.95 }),
  onPressEnd: (e) => gsap.to(e.target, { scale: 1.05 }),
  onHoverStart: (e) => gsap.to(e.target, { scale: 1.05 }),
  onHoverEnd: (e) => gsap.to(e.target, { scale: 1 }),
})

// Enter/Leave viewport
Observer.create({
  target: '.section',
  onEnter: (e) => gsap.from(e.target.querySelectorAll('.el'), { y: 50, opacity: 0, stagger: 0.1 }),
  onLeave: (e) => gsap.to(e.target.querySelectorAll('.el'), { y: 0, opacity: 1 }),
  tolerance: 50,
})
```

## Mobile vs Desktop

```ts
Observer.create({
  target: '.card',
  onHoverStart: (e) => {
    if (Observer.eventType === 'touch') return // Ignora hover em touch
    gsap.to(e.target, { scale: 1.05 })
  },
  onPressStart: (e) => gsap.to(e.target, { scale: 0.95 }),
})
```

## Output

```yaml
observer_plan:
  interactions:
    - target: .card
      type: hover_press
      callbacks: [onHoverStart, onHoverEnd, onPressStart, onPressEnd]
    - target: .section
      type: enter_leave
      callbacks: [onEnter, onLeave]
  mobile_handling: touch_aware
  integration: react
```
