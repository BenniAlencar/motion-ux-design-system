# locomotive-scroll

**Skill compactada — conteudo completo**
Fonte: `skills/locomotive-scroll/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Locomotive Scroll

## Manifesto

Scroll inercial avanzado com suporte a parallax, secoes pinned e efeitos de scroll complexos.

## Stack

- locomotive-scroll (npm)
- GSAP ScrollTrigger (integracao)
- CSS transforms

## Keywords

locomotive, scroll, inertia, parallax, pinned, scroll-effect, smooth-scroll

## Visao Geral

Locomotive Scroll permite:
1. Scroll inercial suave
2. Efeitos de parallax
3. Secoes pinned (fixas)
4. Scroll sections com velocidades diferentes

## Como Usar

```js
import LocomotiveScroll from 'locomotive-scroll';

const scroll = new LocomotiveScroll({
  el: document.getElementById('main'),
  smooth: true,
  inertia: 0.5,
  direction: 'vertical',
  gestureDirection: 'vertical',
  mouseMultiplier: 1,
  touchMultiplier: 2,
  firefoxMultiplier: 15,
});

scroll.start();
```

## Parallax

```html
<div data-scroll data-scroll-speed="1">Elemento rapido</div>
<div data-scroll data-scroll-speed="3">Elemento lento</div>
<div data-scroll data-scroll-speed="-2">Elemento reverso</div>
```

## Secoes Pinned

```html
<section data-scroll-section>
  <div data-scroll data-scroll-sticky data-scroll-target="#sticky">
    Conteudo fixo durante scroll
  </div>
</section>
```

## Integracao com GSAP

```js
const scroll = new LocomotiveScroll({
  el: document.getElementById('main'),
  smooth: true,
});

scroll.on('scroll', (obj) => {
  ScrollTrigger.update();
});

scroll.scrollPage = () => {
  scroll.update();
};
```

## Metricas de Sucesso

- Scroll suave a 60fps
- Parallax funcionando corretamente
- Secoes pinned travando no lugar certo
- Compatibilidade mobile

