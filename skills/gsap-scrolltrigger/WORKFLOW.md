---
name: gsap-workflow
version: 1.0.0
---

# GSAP ScrollTrigger - Workflow

## Passo 1: Receber Motion Plan do Cerebro

```yaml
motion_plan:
  narrative:
    - act: introducao
      scroll_range: 0-0.3
      elements: [hero_title, hero_subtitle]
    - act: revelacao
      scroll_range: 0.3-0.7
      elements: [product_grid, feature_cards]
    - act: climax
      scroll_range: 0.7-1.0
      elements: [cta, social_proof]
  constraints:
    - performance_budget: 16ms p95
    - a11y_target: AA
    - motion_policy: full + reduced
```

## Passo 2: Narrative Analyst

Transformar narrativa em triggers GSAP:

```yaml
triggers:
  - element: .hero_title
    trigger: .hero
    start: top top
    end: bottom top
    scrub: true
    pin: false
    animation:
      y: [0, -100]
      opacity: [1, 0]
      duration: 1
  
  - element: .product_grid
    trigger: .products
    start: top center
    end: bottom center
    scrub: 1
    pin: true
    animation:
      scale: [0.9, 1]
      opacity: [0, 1]
```

## Passo 3: Timeline Planner

Definir duracoes, easings, delays:

```yaml
timeline:
  duration_total: 3s
  easing: power2.inOut
  stagger:
    elements: .product_card
    amount: 0.1
    from: center
  reduced_motion:
    strategy: remove_scrub_keep_fade
    duration: 0.5
```

## Passo 4: Implementation Engineer

Gerar codigo Next.js/React:

```tsx
'use client'
import { useEffect, useRef } from 'react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

export function HeroScroll() {
  const heroRef = useRef<HTMLDivElement>(null)
  const productsRef = useRef<HTMLDivElement>(null)
  
  useEffect(() => {
    const ctx = gsap.context()
    
    // Hero title
    gsap.to(heroRef.current?.querySelector('.hero_title'), {
      scrollTrigger: {
        trigger: heroRef.current,
        start: 'top top',
        end: 'bottom top',
        scrub: true,
      },
      y: -100,
      opacity: 0,
      duration: 1,
    })
    
    // Product grid
    gsap.to(productsRef.current?.querySelectorAll('.product_card'), {
      scrollTrigger: {
        trigger: productsRef.current,
        start: 'top center',
        end: 'bottom center',
        scrub: 1,
        pin: true,
      },
      scale: 1,
      opacity: 1,
      stagger: { amount: 0.1, from: 'center' },
      duration: 1,
      ease: 'power2.inOut',
    })
    
    return () => ctx.revert()
  }, [])
  
  return (
    <>
      <section ref={heroRef} className="hero">
        <h1 className="hero_title">Titulo</h1>
      </section>
      <section ref={productsRef} className="products">
        {/* Product cards */}
      </section>
    </>
  )
}
```

## Passo 5: Performance Reviewer

Verificar:

```yaml
performance_check:
  - layout_thrashing: false
  - paint_heavy: false
  - pin_count: 2 (max recomendado: 3)
  - will_change_usage: minimal
  - mobile_fps_estimate: 55
  
recommendations:
  - "Usar transform em vez de top para parallax"
  - "Limitar pin a 2 secoes"
```

## Passo 6: Accessibility Reviewer

Verificar reduced-motion:

```css
@media (prefers-reduced-motion: reduce) {
  .hero_title {
    animation: none !important;
    transition: opacity 0.5s ease !important;
    transform: none !important;
  }
  
  .product_card {
    transition: opacity 0.5s ease !important;
    transform: none !important;
  }
}
```

## Passo 7: QA Synthesizer

Consolidar:

```yaml
qa_report:
  motion_plan: delivered
  implementation: delivered
  reduced_motion_variant: delivered
  performance: pass (p95 12ms)
  accessibility: pass
  accepted: true
  
evidence:
  - "ScrollTrigger atualiza com Lenis"
  - "Reduced-motion remove scrub, mantem fade"
  - "Keyboard navega por todos elementos"
```
