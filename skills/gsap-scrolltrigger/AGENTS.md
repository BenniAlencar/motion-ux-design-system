---
name: gsap-agents
version: 1.0.0
---

# GSAP ScrollTrigger - Enxame de Agentes

## 1. Narrative Analyst

**Responsabilidade:** Transformar conteudo em sequencia de scroll narrativa.

**Output:**
```yaml
narrative:
  acts:
    - name: introducao
      scroll_range: 0-0.2
      elements: [hero_title, hero_subtitle]
    - name: revelacao
      scroll_range: 0.2-0.5
      elements: [product_grid, feature_cards]
    - name: climax
      scroll_range: 0.5-0.8
      elements: [testimonial_slider, cta]
    - name: resolucao
      scroll_range: 0.8-1.0
      elements: [footer, social_proof]
```

## 2. Timeline Planner

**Responsabilidade:** Definir triggers, pin, scrub, timing.

**Output:**
```yaml
motion_plan:
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

## 3. Implementation Engineer

**Responsabilidade:** Escrever codigo Next/React/Vanilla.

**Output:**
```tsx
// Next.js + React
'use client'
import { useEffect, useRef } from 'react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

export function HeroScroll() {
  const heroRef = useRef<HTMLDivElement>(null)
  
  useEffect(() => {
    const ctx = gsap.context()
    
    gsap.to(heroRef.current?.querySelector('.hero_title'), {
      scrollTrigger: {
        trigger: heroRef.current,
        start: 'top top',
        end: 'bottom top',
        scrub: true,
      },
      y: -100,
      opacity: 0,
    })
    
    return () => ctx.revert()
  }, [])
  
  return (
    <section ref={heroRef} className="hero">
      <h1 className="hero_title">Titulo</h1>
    </section>
  )
}
```

## 4. Performance Reviewer

**Responsabilidade:** Detectar reflow, paint, jank.

**Checklist:**
- [ ] Evitar layout thrashing (ler e escrever DOM separadamente)
- [ ] Usar transform/opacity em vez de top/left/width/height
- [ ] Limitar pin a secoes criticas (max 2-3 pins por pagina)
- [ ] Usar will-change com moderação
- [ ] Testar em mobile com CPU limitada

**Output:**
```yaml
performance_review:
  layout_thrashing: false
  paint_heavy: false
  pin_count: 2
  mobile_fps_estimate: 55
  recommendations:
    - "Usar transform em vez de top para parallax"
```

## 5. Accessibility Reviewer

**Responsabilidade:** Garantir reduced-motion e keyboard.

**Checklist:**
- [ ] prefers-reduced-motion respeitado
- [ ] Conteudo acessivel sem JS
- [ ] Focus visivel em elementos interativos
- [ ] Keyboard navigation funcional

**Output:**
```yaml
a11y_review:
  reduced_motion: pass
  no_js_content: pass
  focus_visible: pass
  keyboard_nav: pass
  issues: []
```

## 6. QA Synthesizer

**Responsabilidade:** Consolidar evidencias e acceptance.

**Output:**
```yaml
qa_report:
  motion_plan: delivered
  implementation: delivered
  reduced_motion_variant: delivered
  performance: pass
  accessibility: pass
  accepted: true
  evidence:
    - "ScrollTrigger atualiza com Lenis"
    - "Reduced-motion remove scrub, mantem fade"
    - "Keyboard navega por todos os elementos"
```
