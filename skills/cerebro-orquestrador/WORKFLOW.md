---
name: cerebro-workflow
version: 1.0.0
---

# Cerebro - Workflow Obrigatorio

## Passo 0: Carregamento Automatico (IDE)

```pseudo
// IDE carrega automaticamente TODAS as skills
allSkills = readDirectory("skills/")
for skill in allSkills:
  skill.manifest = readFile(skill + "/SKILL.md")
  skill.agents = readFile(skill + "/AGENTS.md")
  skill.workflow = readFile(skill + "/WORKFLOW.md")
  skill.keywords = parseKeywords(skill.manifest)
```

## Passo 1: Receber Pedido

```yaml
user_request: "Quero um hero com scroll que revela produtos"
context:
  project_name: "Minha Landing"
  brand_name: "Minha Marca"
  industry: "tech"
  reference_urls: []
constraints:
  performance_budget_ms: 16
  a11y_target: AA
  motion_policy: full
  locales: [pt-BR]
assets_provided:
  logo: false
  copy: true
  images: []
  fonts: []
  models_3d: []
```

## Passo 2: Intent Analyst

```yaml
intent_type: hero_scroll
surface: hero
audience: pt-BR, mobile/desktop
constraints:
  - performance_budget: 16ms p95
  - a11y_target: AA
  - motion_policy: full + reduced
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
```

## Passo 3: Skill Router

```yaml
selected_skills:
  - gsap-scrolltrigger (primary, weight: 1.0)
  - lenis (primary, weight: 1.0)
  - accessibility-a11y (secondary, weight: 0.8)
  - performance-budget (secondary, weight: 0.8)
  - asset-gate (required, weight: 1.0)
  - quality-gate (required, weight: 1.0)
```

## Passo 4: Asset Gate

```yaml
asset_check:
  logo:
    status: missing
    required_for: final_delivery
    placeholder: "/assets/placeholder-logo.svg"
  copy:
    status: provided
    content: "Minha Marca - Transformando o futuro"
  images:
    status: missing
    required_for: final_delivery
    instructions: |
      "Enviar 3 imagens:
       1. Hero background (1920x1080, JPG, < 500kB)
       2. Product shot 1 (800x600, PNG, fundo transparente)
       3. Product shot 2 (800x600, PNG, fundo transparente)
       
       Instrucoes de estilo:
       - Iluminacao natural, fundo neutro
       - Paleta: tons de azul e cinza
       - Evitar texto nas imagens"
  fonts:
    status: unknown
    recommendation: "Inter (Google Fonts, gratuito)"

asset_state: asset_pending
delivery_state: prototype_with_placeholders
blocking_assets:
  - type: logo
    status: missing
    required_for: final_delivery
  - type: images
    status: missing
    required_for: final_delivery
    count: 3
```

## Passo 5: Plan Builder

```yaml
execution_plan:
  - step: 1
    skill: gsap-scrolltrigger
    action: generate_motion_plan
    output: motion_plan.yaml
    dependencies: []
  
  - step: 2
    skill: lenis
    action: integrate_scroll
    output: lenis_integration.ts
    dependencies: [step: 1]
  
  - step: 3
    skill: accessibility-a11y
    action: review_keyboard_focus
    output: a11y_report.yaml
    dependencies: [step: 1, step: 2]
  
  - step: 4
    skill: performance-budget
    action: verify_frame_budget
    output: performance_report.yaml
    dependencies: [step: 1, step: 2]
  
  - step: 5
    skill: quality-gate
    action: review_and_accept
    output: quality_report.yaml
    dependencies: [step: 3, step: 4]
```

## Passo 6: Dispatch

Enviar cada step para a skill responsavel.

## Passo 7: Quality Gate

```yaml
quality_review:
  functional:
    status: pass
    details: "ScrollTrigger atualiza com Lenis, pin funciona"
  performance:
    status: pass
    details: "Frame time p95: 12ms (budget: 16ms)"
  accessibility:
    status: pass_with_warnings
    details: "Keyboard OK, focus visible OK, contraste 4.2:1 (minimo 4.5:1)"
  motion:
    status: pass
    details: "Reduced-motion variant gerada, breath_equivalent OK"
  visual:
    status: pass
    details: "Design fiel ao brief, spacing consistente"

accepted: true
accepted_with_warnings: true
warnings:
  - "Contraste 4.2:1 em texto secundario (aceito pelo cliente)"
blocking_issues: []
```

## Passo 8: Snapshot

```yaml
run_snapshot:
  trace_id: trace_001_cerebro
  timestamp: 2026-09-05T23:30:00Z
  project: "Minha Landing"
  intent: hero_scroll
  
  skills_used:
    - cerebro-orquestrador
    - gsap-scrolltrigger
    - lenis
    - accessibility-a11y
    - performance-budget
    - asset-gate
    - quality-gate
  
  asset_state: asset_pending
  asset_instructions: |
    "Para entrega final, enviar:
     1. Logo em SVG ou PNG (min 500x500, fundo transparente)
     2. 3 imagens conforme especificacoes acima
     3. Confirmar fonte: Inter (Google Fonts)"
  
  quality_state:
    functional: pass
    performance: pass
    accessibility: pass_with_warnings
    motion: pass
    visual: pass
  
  acceptance:
    met: true
    warnings:
      - "Contraste 4.2:1 em texto secundario"
  
  delivery_state: prototype
  next_action: "Aguardar logo e imagens para final delivery"
  
  approved_by: Benni Alencar
  approved_at: 2026-09-05T23:30:00Z
```
