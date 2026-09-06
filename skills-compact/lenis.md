# lenis

**Skill compactada — conteudo completo**
Fonte: `skills/lenis/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Lenis

## Manifesto

Smooth scroll moderno e leve para experiencias de scroll inerciais de alta qualidade.

## Stack

- @studio-freight/lenis (npm)
- requestAnimationFrame para animacoes
- CSS scroll-behavior: smooth (fallback)

## Keywords

smooth, scroll, lenis, inertia, momentum, scroll-animation, scroll-experience

## Visao Geral

Lenis e uma biblioteca de smooth scroll que:
1. Intercepta scroll nativo
2. Aplica inercia e momentum
3. Mantem compatibilidade com GSAP ScrollTrigger
4. Oferece performance otimizada (60fps+)

## Como Usar

```js
import Lenis from '@studio-freight/lenis'

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: 'vertical',
  gestureDirection: 'vertical',
  smooth: true,
  mouseMultiplier: 1,
  touchMultiplier: 2,
  infinite: false,
})

function animate(time) {
  lenis.raf(time)
  requestAnimationFrame(animate)
}

requestAnimationFrame(animate)
```

## Integracao com GSAP

```js
const lenis = new Lenis()

lenis.on('scroll', ScrollTrigger.update)

gsap.ticker.add((time) => {
  lenis.raf(time * 1000)
})

gsap.ticker.lagSmoothing(0)
```

## Metricas de Sucesso

- Scroll suave a 60fps+
- Compatibilidade total com ScrollTrigger
- Baixo overhead de performance
- Suporte a touch e mouse

