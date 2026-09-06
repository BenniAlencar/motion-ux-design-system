---
name: cerebro-workflow
version: 1.0.0
---

# Cerebro - Workflow Obrigatorio

## Passo 1: Receber Pedido

```
user_request: "Quero um hero com scroll que revela produtos"
```

## Passo 2: Intent Analyst

```
intent_type: hero_scroll
surface: hero
audience: pt-BR, mobile/desktop
constraints:
  - performance_budget: 16ms p95
  - a11y_target: AA
  - motion_policy: full + reduced
```

## Passo 3: Skill Router

```
selected_skills:
  - gsap-scrolltrigger (primary)
  - lenis (primary)
  - motion-fundamentals (secondary)
  - accessibility-a11y (secondary)
  - performance-budget (secondary)
```

## Passo 4: Asset Gate

```
asset_check:
  logo: pending
  copy: provided
  images: pending
  fonts: unknown

asset_state: asset_pending
delivery_state: prototype_with_placeholders
```

## Passo 5: Plan Builder

```
execution_plan:
  - skill: gsap-scrolltrigger
    action: generate_motion_plan
    output: motion_plan.yaml
  - skill: lenis
    action: integrate_scroll
    output: lenis_integration.ts
  - skill: motion-fundamentals
    action: apply_easing_choreography
    output: motion_tokens.css
  - skill: accessibility-a11y
    action: review_keyboard_focus
    output: a11y_report.yaml
  - skill: performance-budget
    action: verify_frame_budget
    output: performance_report.yaml
```

## Passo 6: Dispatch

Enviar cada step para a skill responsavel.

## Passo 7: Quality Gate

```
quality_review:
  - performance: pass (p95 12ms)
  - accessibility: pass (keyboard OK)
  - motion: pass (reduced-motion OK)
  - visual: pass (contrast OK)

accepted: true
```

## Passo 8: Snapshot

```
run_snapshot:
  trace_id: trace_001_cerebro
  timestamp: 2026-09-05T22:40:00Z
  intent: hero_scroll
  skills_used:
    - gsap-scrolltrigger
    - lenis
    - motion-fundamentals
    - accessibility-a11y
    - performance-budget
  asset_state: asset_pending
  quality_state: accepted
  delivery_state: prototype
  next_action: "Aguardar logo e imagens para versao final"
```
