---
name: cerebro-agents
version: 1.0.0
---

# Cerebro - Enxame de Agentes

## 1. Intent Analyst

**Responsabilidade:** Interpretar o pedido do usuario e extrair objetivos claros.

**Input:** Pedido em linguagem natural.

**Output:**
- `intent_type`: hero, landing, scroll_story, 3D_experience, microinteraction, etc
- `surface`: hero, section, page, site_completo
- `audience`: pt-BR/en/es, mobile/desktop
- `constraints`: performance, a11y, motion_policy

**Prompt:**
```
Analise este pedido e extraia:
1. Tipo de intencao (hero, landing, scroll, 3D, micro)
2. Surface (hero, section, page, site)
3. Audience e locales
4. Constraints conhecidas (performance, a11y, reduced-motion)

Pedido: {user_request}
```

## 2. Skill Router

**Responsabilidade:** Selecionar skills baseado na intencao classificada.

**Input:** Intent classification do Analyst.

**Output:** Lista de skills com pesos de relevancia.

**Tabela de Roteamento:**

| Intent | Skills Primarias | Skills Secundarias |
|--------|------------------|--------------------|
| hero_scroll | gsap-scrolltrigger, lenis | motion-fundamentals, a11y |
| hero_3d | r3f-threejs-drei, webgpu | performance-budget, a11y |
| landing | ui-ux-fundamentals, gsap | lenis, a11y, performance |
| microinteraction | rive, lottiefiles | motion-fundamentals |
| spline_hero | spline-runtime | r3f-threejs-drei, a11y |

## 3. Plan Builder

**Responsabilidade:** Criar plano de execucao sequencial.

**Output:**
```yaml
execution_plan:
  - step: 1
    skill: asset-gate
    action: verify_assets
  - step: 2
    skill: gsap-scrolltrigger
    action: generate_motion_plan
  - step: 3
    skill: lenis
    action: integrate_scroll
  - step: 4
    skill: quality-gate
    action: review_and_accept
```

## 4. Asset Gate Coordinator

**Responsabilidade:** Verificar assets antes de execucao.

**Checklist:**
- [ ] Logo (SVG/PNG)
- [ ] Copy real (nome, tagline, CTA)
- [ ] Imagens ou direcao visual
- [ ] Fontes/licenca
- [ ] 3D/GLB/Spline se aplicavel
- [ ] Rive/Lottie se aplicavel

**Output:**
```yaml
asset_state: provided | pending | placeholder_only
blocking_assets:
  - type: logo
    status: missing
    required_for: final_delivery
```

## 5. Quality Coordinator

**Responsabilidade:** Orquestrar revisoes finais.

**Revisoes:**
- Performance budget (frame, memory, draw calls)
- Accessibility (keyboard, focus, screen reader)
- Motion (reduced-motion, breath_equivalent)
- Visual (contrast, spacing, typography)

**Output:**
```yaml
quality_report:
  performance: pass | fail
  accessibility: pass | fail
  motion: pass | fail
  visual: pass | fail
  accepted: true | false
  gaps:
    - description
    - severity
```
