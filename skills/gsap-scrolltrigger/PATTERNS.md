---
name: gsap-patterns
version: 1.0.0
---

# GSAP ScrollTrigger - Patterns

## 1. Pin-Scroll (Hero Fixo)

```tsx
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

gsap.to('.hero_content', {
  scrollTrigger: {
    trigger: '.hero',
    start: 'top top',
    end: '+=100%',
    pin: true,
    scrub: true,
  },
  scale: 0.8,
  opacity: 0,
})
```

**Uso:** Hero que fica fixo enquanto conteudo sobe por cima.

**Reduced Motion:**
```css
@media (prefers-reduced-motion: reduce) {
  .hero_content {
    animation: none;
    opacity: 1;
    transform: none;
  }
}
```

## 2. Horizontal Scroll

```tsx
gsap.to('.horizontal_wrapper', {
  scrollTrigger: {
    trigger: '.horizontal_section',
    start: 'top top',
    end: '+=300%',
    pin: true,
    scrub: 1,
  },
  xPercent: -100 * (slides.length - 1),
  ease: 'none',
})
```

**Uso:** Seção que scrolla horizontalmente.

**Fallback:** Em reduced-motion, mostrar grid vertical.

## 3. Reveal on Scroll

```tsx
gsap.utils.toArray('.reveal').forEach((el) => {
  gsap.from(el, {
    scrollTrigger: {
      trigger: el,
      start: 'top 80%',
      toggleActions: 'play none none reverse',
    },
    y: 50,
    opacity: 0,
    duration: 1,
    ease: 'power3.out',
  })
})
```

**Uso:** Elementos que aparecem ao scrollar.

## 4. Flip Modal (Transição de Layout)

```tsx
import Flip from 'gsap/Flip'

function expandCard(card: HTMLElement) {
  const state = Flip.getState(card, { props: 'borderRadius,backgroundColor' })
  
  card.classList.add('expanded')
  
  Flip.from(state, {
    duration: 0.7,
    ease: 'power2.inOut',
    absolute: true,
    scale: true,
  })
}
```

**Uso:** Card expandindo para modal sem flash.

## 5. Parallax com Velocity

```tsx
import Lenis from 'lenis'

const lenis = new Lenis()

lenis.on('scroll', ({ velocity, scroll }) => {
  const v = velocity * 0.01
  gsap.to('.parallax_slow', { y: scroll * 0.2 + v * 10, overwrite: 'auto' })
  gsap.to('.parallax_fast', { y: scroll * -0.3 + v * -5, overwrite: 'auto' })
})
```

**Uso:** Parallax que reage à velocidade do scroll.

## 6. Observer (Hover/Press em Mobile)

```tsx
import { Observer } from 'gsap/Observer'

gsap.registerPlugin(Observer)

Observer.create({
  target: '.interactive_element',
  onHoverStart: () => gsap.to('.element', { scale: 1.05 }),
  onHoverEnd: () => gsap.to('.element', { scale: 1 }),
  onPressStart: () => gsap.to('.element', { scale: 0.95 }),
  onPressEnd: () => gsap.to('.element', { scale: 1.05 }),
})
```

**Uso:** Hover/press em dispositivos touch.
