# gsap-scrolltrigger

**Skill compactada — conteudo completo**
Fonte: `skills/gsap-scrolltrigger/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# GSAP + ScrollTrigger

## Manifesto

Animacoes baseadas em scroll usando GSAP ScrollTrigger para reveal effects, parallax e pinned sections.

## Stack

- gsap (core)
- @gsap/react (opcional, para React)
- ScrollTrigger (plugin GSAP)

## Keywords

scroll, animation, gsap, scrolltrigger, reveal, parallax, pin, scrub

## Visao Geral

GSAP + ScrollTrigger permite:
1. Animacoes triggeradas por scroll
2. Efeitos de parallax
3. Secoes pinned (fixas)
4. Scrub animations (linked ao scroll)

## Como Usar

```js
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

gsap.utils.toArray('.reveal').forEach(element => {
  gsap.from(element, {
    scrollTrigger: {
      trigger: element,
      start: 'top 80%',
      end: 'bottom 20%',
      scrub: true,
    },
    opacity: 0,
    y: 100,
  });
});
```

## Com React

```tsx
import { useGSAP } from 'gsap-triggers';

function Hero() {
  const { ref, tl } = useGSAP((gsap) => {
    const scrollTl = gsap.timeline({
      scrollTrigger: {
        trigger: ref.current,
        start: 'top top',
        end: 'bottom bottom',
        scrub: true,
      },
    });
    
    scrollTl.from('.hero-title', { opacity: 0, y: 100 })
            .from('.hero-image', { scale: 0.8, opacity: 0 }, '<');
    
    return scrollTl;
  });
  
  return (
    <section ref={ref} className="hero">
      <h1 className="hero-title">Scroll Reveals</h1>
      <img src="/hero.jpg" alt="Hero" className="hero-image" />
    </section>
  );
}
```

## Parallax

```js
gsap.to('.parallax-bg', {
  scrollTrigger: {
    trigger: '.section',
    start: 'top bottom',
    end: 'bottom top',
    scrub: true,
  },
  y: -100,
});
```

## Pin Section

```js
gsap.to('.pinned-content', {
  scrollTrigger: {
    trigger: '.section',
    start: 'top top',
    end: '+=100%',
    pin: true,
    scrub: true,
  },
  opacity: 0,
  scale: 0.8,
});
```

## Metricas de Sucesso

- Scroll animations suaves a 60fps
- Parallax funcionando
- Pinned sections travando corretamente
- Scrub animations linked ao scroll

