---
name: quality-gate
description: QA, acceptance criteria, evidence, rollback, run snapshot
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - quality
    - qa
    - gate
    - acceptance
    - evidence
    - rollback
  routes:
    - quality
depends_on:
  - cerebro-orquestrador
  - accessibility-a11y
  - performance-budget
  - asset-gate
outputs:
  - quality_report
  - acceptance_criteria
  - evidence_packet
  - rollback_plan
  - run_snapshot
---

# Quality Gate

## Stack

- QA checklist
- Acceptance criteria
- Evidence collection
- Rollback planning
- Run snapshot

## Enxame de Agentes

1. **QA Coordinator** - Orquestra revisoes de todas as areas
2. **Acceptance Writer** - Define criterios de acceptance
3. **Evidence Collector** - Coleta evidencias (screens, metrics, logs)
4. **Rollback Planner** - Prepara plano de rollback
5. **Snapshot Writer** - Cria run snapshot final

## Quality Checklist

### Funcional

- [ ] Todos elementos interativos funcionam
- [ ] Links navegam corretamente
- [ ] Forms validam e enviam
- [ ] Animacoes disparam nos triggers corretos

### Performance

- [ ] Lighthouse performance >= 80
- [ ] Frame time p95 < 16ms
- [ ] Bundle dentro do budget
- [ ] Memory sem leaks

### Accessibility

- [ ] WCAG AA contraste
- [ ] Keyboard navigation completa
- [ ] Focus visible
- [ ] Reduced motion respeitado
- [ ] Screen reader testado

### Visual

- [ ] Design fiel ao approved
- [ ] Spacing consistente
- [ ] Typography correta
- [ ] Cores conforme tokens

### Motion

- [ ] Timings conforme motion plan
- [ ] Easing consistente
- [ ] Reduced motion variant
- [ ] Sem jank ou stutter

## Acceptance Criteria Template

```yaml
acceptance_criteria:
  functional:
    - "Hero scroll revela produtos corretamente"
    - "CTA navega para pagina de checkout"
    - "Menu mobile abre e fecha"
    
  performance:
    - "Lighthouse performance >= 80"
    - "FCP < 2.5s em 4G"
    - "Frame time p95 < 16ms"
    
  accessibility:
    - "WCAG AA contraste"
    - "Keyboard navigation completa"
    - "Reduced motion respeitado"
    
  visual:
    - "Design fiel ao Figma approved"
    - "Spacing conforme tokens"
```

## Evidence Packet

```yaml
evidence_packet:
  screenshots:
    - desktop_hero.png
    - mobile_hero.png
    - desktop_products.png
    - mobile_products.png
  metrics:
    lighthouse:
      performance: 87
      accessibility: 94
      best_practices: 92
      seo: 89
    frame_time_p95_ms: 14
    bundle_js_kb: 142
  logs:
    - console_clean: true
    - errors: []
    - warnings: ["Contraste 4.2:1 em texto secundario"]
  video:
    - scroll_demo.mp4
    - keyboard_demo.mp4
```

## Rollback Plan

```yaml
rollback_plan:
  trigger_conditions:
    - "Performance abaixo de 70 no Lighthouse"
    - "Erro critico em producao"
    - "A11y blocker identificado"
  rollback_steps:
    - "Revert para ultimo commit estavel"
    - "Reduzir effects para fallback tier"
    - "Desabilitar 3D se necessario"
  fallback_tiers:
    - A: HTML/CSS/SVG (sempre disponivel)
    - B: Canvas 2D
    - C: WebGL2
    - D: WebGPU (apenas se capability OK)
```

## Run Snapshot

```yaml
run_snapshot:
  trace_id: trace_001_quality
  timestamp: 2026-09-05T23:00:00Z
  project: Nome do Projeto
  skills_used:
    - cerebro-orquestrador
    - gsap-scrolltrigger
    - lenis
    - accessibility-a11y
    - performance-budget
    - asset-gate
    - quality-gate
  
  asset_state: asset_pending
  quality_state:
    functional: pass
    performance: pass
    accessibility: pass_with_warnings
    visual: pass
    motion: pass
  
  acceptance:
    met: true
    warnings:
      - "Contraste 4.2:1 em texto secundario (aceito pelo cliente)"
  
  evidence_packet_ref: evidence_001
  rollback_plan_ref: rollback_001
  
  delivery_state: prototype
  next_action: "Aguardar logo e imagens para final delivery"
  
  approved_by: Benni Alencar
  approved_at: 2026-09-05T23:00:00Z
```

## Output Final

```yaml
quality_gate_report:
  accepted: true
  accepted_with_warnings: true
  warnings:
    - "Contraste 4.2:1 em texto secundario"
  blocking_issues: []
  delivery_state: prototype
  next_action: "Aguardar assets pendentes para final delivery"
```
