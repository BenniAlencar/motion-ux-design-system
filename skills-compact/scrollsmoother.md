# scrollsmoother

**Skill compactada — conteudo completo**
Fonte: `skills/scrollsmoother/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# ScrollSmoother

## Manifesto

Scroll horizontal e efeitos de smooth scroll avancados usando GSAP ScrollSmoother para experiencias de navegacao unicas.

## Stack

- gsap + ScrollSmoother (plugin GSAP)
- GSAP ScrollTrigger
- CSS transforms

## Keywords

scrollsmoother, horizontal-scroll, smooth-scroll, gsap, scroll-effect, parallax

## Visao Geral

ScrollSmoother permite:
1. Scroll horizontal suave
2. Efeitos de parallax no scroll
3. Secoes com velocidades diferentes
4. Integracao perfeita com ScrollTrigger

## Como Usar

```js
import { gsap } from 'gsap';
import ScrollSmoother from 'gsap/ScrollSmoother';
import ScrollTrigger from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollSmoother, ScrollTrigger);

const smoother = ScrollSmoother.create({
  smooth: 2,
  effects: true,
  smoothTouch: false,
  normalizeScroll: true,
});
```

## Efeitos de Parallax

```js
// Elementos com velocidades diferentes
smoother.effects('[data-speed]', { lagFactor: 3 });

// HTML:
// <div data-speed="0.5">Lento</div>
// <div data-speed="1.5">Rapido</div>
// <div data-speed="-0.5">Reverso</div>
```

## Scroll Horizontal

```js
const sections = gsap.utils.toArray('.section');

gsap.to(sections, {
  xPercent: -100 * (sections.length - 1),
  ease: 'none',
  scrollTrigger: {
    trigger: '.horizontal-container',
    pin: true,
    scrub: 1,
    end: () => '+=' + document.querySelector('.horizontal-container').offsetWidth,
  },
});
```

## Metricas de Sucesso

- Scroll suave a 60fps
- Efeitos de parallax funcionando
- Scroll horizontal responsivo
- Compatibilidade mobile

