---
name: quality-gate-workflow
version: 1.0.0
---

# Quality Gate - Workflow

## Passo 1: Receber Execucao das Skills

```yaml
execution_results:
  gsap-scrolltrigger:
    status: completed
    outputs:
      - motion_plan.yaml
      - implementation.tsx
      - reduced_motion.css
  
  lenis:
    status: completed
    outputs:
      - lenis_integration.ts
  
  accessibility-a11y:
    status: completed
    outputs:
      - a11y_report.yaml
  
  performance-budget:
    status: completed
    outputs:
      - performance_report.yaml
```

## Passo 2: QA Coordinator

Orquestrar revisoes de todas as areas:

```yaml
quality_checklist:
  functional:
    - [ ] Todos elementos interativos funcionam
    - [ ] Links navegam corretamente
    - [ ] Forms validam e enviam
    - [ ] Animacoes disparam nos triggers corretos
    - [ ] Scroll suave (Lenis integrado)
    - [ ] Reduced motion respeitado
  
  performance:
    - [ ] Lighthouse performance >= 80
    - [ ] Frame time p95 < 16ms
    - [ ] Bundle dentro do budget
    - [ ] Memory sem leaks
    - [ ] No long tasks > 50ms
  
  accessibility:
    - [ ] WCAG AA contraste (4.5:1 texto normal)
    - [ ] Keyboard navigation completa
    - [ ] Focus visible em todos elementos
    - [ ] Screen reader text adequado
    - [ ] Skip link presente
  
  visual:
    - [ ] Design fiel ao brief
    - [ ] Spacing consistente (8px grid)
    - [ ] Typography correta
    - [ ] Cores conforme tokens
    - [ ] Imagens otimizadas
  
  motion:
    - [ ] Timings conforme motion plan
    - [ ] Easing consistente
    - [ ] Reduced motion variant
    - [ ] Sem jank ou stutter
    - [ ] Pin count <= 3
```

## Passo 3: Acceptance Writer

Definir criterios de acceptance:

```yaml
acceptance_criteria:
  functional:
    - "Hero scroll revela produtos corretamente"
    - "CTA navega para pagina de checkout"
    - "Menu mobile abre e fecha"
    - "Lenis scroll suave em desktop e mobile"
  
  performance:
    - "Lighthouse performance >= 80"
    - "FCP < 2.5s em 4G"
    - "Frame time p95 < 16ms"
    - "Bundle JS < 250kB"
  
  accessibility:
    - "WCAG AA contraste"
    - "Keyboard navigation completa"
    - "Reduced motion respeitado"
    - "Focus visible em todos elementos"
  
  visual:
    - "Design fiel ao Figma approved"
    - "Spacing conforme tokens (8px grid)"
```

## Passo 4: Evidence Collector

Coletar evidencias:

```yaml
evidence_packet:
  screenshots:
    - desktop_hero.png
    - mobile_hero.png
    - desktop_products.png
    - mobile_products.png
    - keyboard_focus.png
  
  metrics:
    lighthouse:
      performance: 87
      accessibility: 94
      best_practices: 92
      seo: 89
    
    frame_time_p95_ms: 14
    bundle_js_kb: 142
    bundle_css_kb: 48
    memory_mb: 98
  
  logs:
    console_clean: true
    errors: []
    warnings:
      - "Contraste 4.2:1 em texto secundario (aceito)"
  
  video:
    - scroll_demo.mp4
    - keyboard_demo.mp4
    - reduced_motion_demo.mp4
```

## Passo 5: Rollback Planner

Preparar plano de rollback:

```yaml
rollback_plan:
  trigger_conditions:
    - "Performance abaixo de 70 no Lighthouse"
    - "Erro critico em producao"
    - "A11y blocker identificado"
    - "Frame time p95 > 50ms"
  
  rollback_steps:
    - "Revert para ultimo commit estavel"
    - "Reduzir effects para fallback tier"
    - "Desabilitar 3D se necessario"
    - "Remover pins excessivos"
  
  fallback_tiers:
    - A: HTML/CSS/SVG (sempre disponivel)
    - B: Canvas 2D
    - C: WebGL2
    - D: WebGPU (apenas se capability OK)
  
  contacts:
    - "dev@empresa.com"
    - "design@empresa.com"
```

## Passo 6: Snapshot Writer

Criar run snapshot final:

```yaml
run_snapshot:
  trace_id: trace_001_quality
  timestamp: "2026-09-05T23:45:00Z"
  project: "Minha Landing"
  
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
  
  approved_by: "Benni Alencar"
  approved_at: "2026-09-05T23:45:00Z"
```

## Passo 7: Output Final

```yaml
quality_gate_report:
  accepted: true
  accepted_with_warnings: true
  warnings:
    - "Contraste 4.2:1 em texto secundario"
  blocking_issues: []
  delivery_state: prototype
  next_action: "Aguardar assets pendentes para final delivery"
  
  evidence_summary:
    screenshots: 5
    metrics_collected: true
    lighthouse_score: 87
    video_demos: 3
  
  rollback_ready: true
```
