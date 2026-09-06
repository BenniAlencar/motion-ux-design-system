# Project Instructions

## Visao Geral

Este repositorio e um **sistema de skills dedicadas para design de sites e UI/UX**, consumido por IDEs e agentes como Perplexity, Google Antigravity e ambientes compativeis com leitura de arquivos Markdown/YAML.

**Nao e** um runtime Python/Node independente. O "runtime" e a IDE/agente que carrega e executa as instrucoes das skills.

## Principios

1. **Skills dedicadas** - Cada skill e independente e especializada
2. **Enxame declarativo** - Cada skill define multiplos agentes (analyst, planner, implementer, reviewer, qa)
3. **Contratos explicitos** - INPUT_CONTRACT.yaml e OUTPUT_CONTRACT.yaml definem interfaces
4. **Workflow obrigatorio** - WORKFLOW.md descreve passos que devem ser seguidos
5. **Fallback sempre** - Toda skill deve ter fallback para browsers/devices limitados
6. **Asset Gate antes de entrega** - Verificar assets antes de declarar entrega final
7. **Quality Gate antes de publicar** - QA, acceptance, evidence, rollback

## Como Usar em uma IDE

### Passo 1: Carregar Cerebro

Sempre carregue `skills/cerebro-orquestrador/SKILL.md` primeiro. O cerebro:
- Classifica a intencao do usuario
- Seleciona skills relevantes
- Cria plano de execucao
- Coordena asset gate e quality gate

### Passo 2: Executar Skills Selecionadas

Para cada skill selecionada:
1. Ler SKILL.md para entender stack e agentes
2. Ler AGENTS.md para entender papeis e outputs
3. Ler WORKFLOW.md para seguir fluxo obrigatorio
4. Consultar INPUT_CONTRACT.yaml para validar entrada
5. Gerar OUTPUT_CONTRACT.yaml como saida

### Passo 3: Asset Gate

Antes de entregar resultado final:
1. Executar `skills/asset-gate/SKILL.md`
2. Verificar assets necessarios (logo, imagens, copy, fontes, 3D)
3. Se assets pendentes, entregar prototype com placeholders
4. Documentar no run_snapshot

### Passo 4: Quality Gate

Antes de publicar:
1. Executar `skills/quality-gate/SKILL.md`
2. Rodar checklists (funcional, performance, a11y, visual, motion)
3. Coletar evidence packet (screens, metrics, logs)
4. Preparar rollback plan
5. Criar run_snapshot

### Passo 5: Snapshot Final

Entregar run_snapshot com:
- trace_id e timestamp
- skills usadas
- asset_state
- quality_state
- acceptance (met/not met)
- delivery_state (final/prototype/blocked)
- next_action

## Renderer Ladder

Toda skill que gera efeitos visuais deve seguir renderer ladder:

| Tier | Tecnologia | Uso |
|------|------------|-----|
| A | HTML/CSS/SVG | Fallback sempre disponivel |
| B | Canvas 2D | Generativo leve, particulas 2D |
| C | WebGL2 | 3D completo com shaders |
| D | WebGPU | Compute pesado, 50k+ particulas |
| E | Poster + HTML | Foto + descricao para browsers sem WebGL |

## Reduced Motion

Toda animacao deve respeitar `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Accessibility

Toda skill deve garantir:
- WCAG AA contraste (4.5:1 texto normal)
- Keyboard navigation completa
- Focus visible
- Screen reader text
- Skip link

## Performance Budgets

### Landing Page
- Lighthouse performance >= 90
- FCP < 1.5s, LCP < 2.5s
- JS < 150kB, CSS < 50kB
- Frame time p95 < 16ms

### Hero 3D
- Lighthouse performance >= 80
- FCP < 2.0s, LCP < 3.0s
- JS < 250kB
- Draw calls < 100 mobile, < 300 desktop
- Texture memory < 64MB mobile, < 256MB desktop

## Provenance e Direitos

Toda skill que usa assets externos deve:
- Documentar origem (URL, autor, fonte)
- Verificar licenca de uso
- Incluir digest (sha256) para versionamento

## Rollback

Toda entrega deve ter rollback plan:
- Trigger conditions (performance abaixo de X, erro critico, a11y blocker)
- Rollback steps (revert commit, reduzir effects, desabilitar 3D)
- Fallback tiers (A/B/C/D/E)

## Exemplo de Uso

```
User: "Quero um hero com scroll que revela produtos"

1. Cerebro classifica: intent = hero_scroll
2. Skills selecionadas: gsap-scrolltrigger, lenis, motion-fundamentals, a11y, performance
3. Asset Gate verifica: logo pending, imagens pending
4. Executar gsap-scrolltrigger:
   - Narrative Analyst cria motion plan
   - Implementation Engineer gera codigo
   - Performance Reviewer valida FPS
   - Accessibility Reviewer valida reduced motion
5. Quality Gate:
   - QA Coordinator roda checklists
   - Evidence Collector captura screens e metrics
   - Snapshot Writer cria run_snapshot
6. Entrega:
   - Prototype com placeholders
   - run_snapshot com asset_state = asset_pending
   - next_action = "Aguardar logo e imagens para final delivery"
```

## Contribuindo

Para adicionar uma nova skill:
1. Criar pasta `skills/<skill-slug>/`
2. Adicionar SKILL.md, AGENTS.md, WORKFLOW.md
3. Adicionar INPUT_CONTRACT.yaml, OUTPUT_CONTRACT.yaml
4. Adicionar PATTERNS.md, IMPLEMENTATION.md, QUALITY_GATE.md, EVALS.md
5. Adicionar exemplos em `skills/<skill-slug>/examples/`
6. Atualizar README.md com nova skill

## License

MIT
