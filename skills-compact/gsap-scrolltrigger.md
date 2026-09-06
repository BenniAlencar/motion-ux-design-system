# gsap-scrolltrigger

Skill compactada — todo o conteudo em um unico arquivo

================================================================================

================================================================================
## SKILL.md
================================================================================

# GSAP + ScrollTrigger

## Manifesto

Animacoes baseadas em scroll usando GSAP ScrollTrigger.

## Stack

- gsap (core)
- @gsap/react (opcional, para React)
- ScrollTrigger (plugin GSAP)

## Keywords

scroll, animation, gsap, scrolltrigger, reveal, parallax, pin, scrub

================================================================================
## AGENTS.md
================================================================================

# Agents — GSAP + ScrollTrigger

## Enxame de Agents

### ScrollAnimationAgent
**Responsabilidade:** Criar animacoes baseadas em scroll.

**Input:**
```yaml
intent_type: hero_scroll
selected_skills: [gsap-scrolltrigger, lenis]
```

**Output:**
```tsx
import { useGSAP } from 'gsap-triggers'

export default function Hero() {
  const { ref, tl } = useGSAP((gsap) => {
    const scrollTl = gsap.timeline({
      scrollTrigger: {
        trigger: ref.current,
        start: 'top top',
        end: 'bottom bottom',
        scrub: true,
      },
    })
    
    scrollTl.from('.hero-title', { opacity: 0, y: 100 })
            .from('.hero-image', { scale: 0.8, opacity: 0 }, '<')
    
    return scrollTl
  })
  
  return <div ref={ref}>...</div>
}
```

### PinAgent
**Responsabilidade:** Criar elementos pinned (fixos durante scroll).

### ParallaxAgent
**Responsabilidade:** Criar efeitos de parallax com camadas.

================================================================================
## WORKFLOW.md
================================================================================

# Workflow — GSAP + ScrollTrigger

## Passos

1. **Setup:** Importar GSAP + ScrollTrigger
2. **Trigger:** Definir elemento trigger e timeline
3. **Animation:** Criar animacoes na timeline
4. **Scroll:** Configurar scrollTrigger (start, end, scrub, pin)
5. **Optimize:** Usar will-change, evitar layout thrashing

## Exemplo Basico

```tsx
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

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
  })
})
```

================================================================================
## INPUT_CONTRACT.yaml
================================================================================

intent_type: hero_scroll | landing | page_transition
selected_skills:
  - gsap-scrolltrigger
  - lenis (opcional)
  - accessibility-a11y (required)
  - performance-budget (required)
user_request: string
assets:
  logo: string (url)
  images: string[] (urls)
  fonts: string[] (names)

delivery_state: prototype | ready

================================================================================
## OUTPUT_CONTRACT.yaml
================================================================================

code: string (tsx/ts/js)
asset_instructions: string (markdown)
quality_report:
  lighthouse_performance: number
  frame_time_p95: number
  wcag_aa_contrast: pass | fail
  keyboard_navigation: pass | fail
  reduced_motion: pass | fail
evidence:
  screenshots: string[] (urls)
  lighthouse_metrics: object
  video_demos: string[] (urls)

delivery_state: prototype | ready

================================================================================
## PATTERNS.md
================================================================================

# Patterns — GSAP + ScrollTrigger

## Scroll Reveal

```tsx
const { ref, tl } = useGSAP((gsap) => {
  const scrollTl = gsap.timeline({
    scrollTrigger: {
      trigger: ref.current,
      start: 'top 80%',
      end: 'bottom 20%',
      scrub: true,
    },
  })
  
  scrollTl.from('.reveal', { opacity: 0, y: 100, stagger: 0.2 })
  
  return scrollTl
})
```

## Parallax

```tsx
const { ref } = useGSAP((gsap) => {
  gsap.to('.parallax-bg', {
    scrollTrigger: {
      trigger: ref.current,
      start: 'top bottom',
      end: 'bottom top',
      scrub: true,
    },
    y: -100,
  })
})
```

## Pin Section

```tsx
const { ref, tl } = useGSAP((gsap) => {
  const scrollTl = gsap.timeline({
    scrollTrigger: {
      trigger: ref.current,
      start: 'top top',
      end: '+=100%',
      pin: true,
      scrub: true,
    },
  })
  
  scrollTl.from('.pinned-content', { opacity: 0, scale: 0.8 })
  
  return scrollTl
})
```

================================================================================
## examples/
================================================================================

### hero-scroll.tsx

```tsx
import { useGSAP } from 'gsap-triggers'
import { useLenis } from '@studio-freight/lenis'

export default function Hero() {
  const { ref, tl } = useGSAP((gsap) => {
    const scrollTl = gsap.timeline({
      scrollTrigger: {
        trigger: ref.current,
        start: 'top top',
        end: 'bottom bottom',
        scrub: true,
      },
    })
    
    scrollTl.from('.hero-title', { opacity: 0, y: 100, duration: 1 })
            .from('.hero-image', { scale: 0.8, opacity: 0, duration: 1 }, '<')
            .from('.hero-subtitle', { opacity: 0, y: 50, duration: 0.8 }, '-=0.5')
    
    return scrollTl
  })
  
  useLenis()
  
  return (
    <section ref={ref} className="hero">
      <h1 className="hero-title">Scroll Reveals Products</h1>
      <img src="/hero.jpg" alt="Hero" className="hero-image" />
      <p className="hero-subtitle">Discover our collection</p>
    </section>
  )
}
```

