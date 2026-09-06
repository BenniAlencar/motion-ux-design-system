---
name: gsap-scrolltrigger
description: Enxame para GSAP Core + ScrollTrigger + Observer + Flip
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - gsap
    - scrolltrigger
    - scroll
    - pin
    - scrub
    - flip
    - observer
  routes:
    - motion
    - ui_ux
depends_on:
  - cerebro-orquestrador
  - lenis
outputs:
  - motion_plan
  - implementation
  - reduced_motion_variant
  - qa_report
---

# GSAP ScrollTrigger

## Stack

- GSAP Core 3.12+
- ScrollTrigger
- Observer
- Flip
- Lenis (integracao)

## Enxame de Agentes

1. **Narrative Analyst** - Transforma conteudo em sequencia de scroll
2. **Timeline Planner** - Define triggers, distancias, pin, scrub, timing
3. **Implementation Engineer** - Escreve integracao Next, React ou Vanilla
4. **Performance Reviewer** - Detecta reflow, paint, jank, refresh excessivo
5. **Accessibility Reviewer** - Define conteudo sem JS, reduced motion, foco
6. **QA Synthesizer** - Consolida evidencias, lacunas e acceptance

## Processo Obrigatorio

1. Receba intencao e conteudo
2. Liste assets, componentes e dependencias
3. Produza motion_plan.yaml
4. Implemente com fallback definido
5. Produza variante reduced/static
6. Revise performance e acessibilidade
7. Entregue qa_report.yaml e run_snapshot.yaml

## Patterns

Ver PATTERNS.md para pin-scroll, horizontal-scroll, reveal, flip-modal, reduced-motion.
