---
name: animejs
description: Anime.js para animacoes leves de CSS, SVG, JS
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - anime.js
    - animejs
    - css animation
    - svg animation
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
outputs:
  - anime_plan
  - timeline_config
  - integration_code
---

# Anime.js

## Stack

- animejs
- CSS, SVG, JS objects

## Enxame de Agentes

1. **Animation Analyst** - Analisa animacoes necessarias
2. **Timeline Designer** - Configura timelines e delays
3. **Easing Designer** - Seleciona easings
4. **Integration Engineer** - Gera codigo

## Animacao Simples

```ts
import anime from 'animejs'

anime({
  targets: '.el',
  translateX: 250,
  rotate: 180,
  borderRadius: '100%',
  duration: 1000,
  easing: 'easeInOutQuad',
})
```

## Timeline

```ts
const tl = anime.timeline({
  targets: '.card',
  duration: 800,
  easing: 'easeInOutQuad',
})

.add({
  translateX: 250,
})
.add({
  rotate: 180,
  delay: anime.stagger(100),
})
.add({
  scale: 0.5,
})
```

## Stagger

```ts
anime({
  targets: '.card',
  translateY: anime.stagger(-50, {grid: [3, 3], from: 'center'}),
  delay: anime.stagger(100),
})
```

## SVG

```ts
anime({
  targets: 'path',
  strokeDashoffset: [anime.setDashoffset, 0],
  easing: 'easeInOutSine',
  duration: 1500,
  direction: 'alternate',
  loop: true,
})
```

## Output

```yaml
anime_plan:
  animations:
    - type: translate_rotate
      duration: 1000
      easing: easeInOutQuad
    - type: stagger_grid
      grid: [3, 3]
      from: center
    - type: svg_draw
      duration: 1500
      loop: true
  integration: vanilla
```
