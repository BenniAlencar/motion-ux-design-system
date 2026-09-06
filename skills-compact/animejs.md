# animejs

**Skill compactada — conteudo completo**
Fonte: `skills/animejs/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Anime.js

## Manifesto

Biblioteca de animacao JavaScript leve e poderosa para animacoes de SVG, CSS, transforms e mais.

## Stack

- animejs (npm)
- CSS transforms
- SVG animations

## Keywords

animejs, animation, svg, css, transform, timeline, stagger, easing

## Visao Geral

Anime.js permite:
1. Animacoes de SVG complexas
2. Stagger animations
3. Timeline de animacoes
4. Custom easing functions

## Como Usar

```js
import anime from 'animejs';

// Animacao simples
anime({
  targets: '.box',
  translateX: 250,
  rotate: '1turn',
  backgroundColor: '#FFF',
  duration: 800,
});

// Stagger
anime({
  targets: '.item',
  translateY: [-50, 0],
  opacity: [0, 1],
  delay: anime.stagger(100),
  duration: 500,
});

// Timeline
const tl = anime.timeline({
  targets: '.box',
  duration: 800,
  easing: 'easeInOutQuad',
});

tl.add({
  translateX: 250,
}).add({
  rotate: '1turn',
}, '-=400').add({
  scale: 2,
}, '-=400');
```

## SVG Animations

```js
anime({
  targets: 'path',
  strokeDashoffset: [anime.setDashoffset, 0],
  easing: 'easeInOutSine',
  duration: 1500,
  direction: 'alternate',
  loop: true,
});
```

## Metricas de Sucesso

- Animacoes suaves a 60fps
- Stagger funcionando corretamente
- Timeline sincronizada
- SVG animado sem glitches

