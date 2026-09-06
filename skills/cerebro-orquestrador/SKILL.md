---
name: cerebro-orquestrador
description: Roteador e classificador de intencao para Motion/UX Design System
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - cerebro
    - orquestrador
    - router
    - classifier
    - orchestrator
  routes:
    - core
  priority: 1
  auto_load: true
outputs:
  - intent_classification
  - selected_skills
  - execution_plan
  - asset_requirements
---

# Cerebro Orquestrador

## Funcao

**PRIMEIRA skill a ser carregada automaticamente em TODA solicitacao.**

O cerebro classifica a intencao do usuario e seleciona as skills especializadas para executar o trabalho.

## CARREGAMENTO AUTOMATICO

A IDE/agente DEVE:
1. Carregar cerebro-orquestrador automaticamente em TODA solicitacao
2. Ler TODAS as outras skills do diretorio `skills/` automaticamente
3. Indexar skills por keywords (`activation.keywords`)
4. Nao esperar instrucao explicita do usuario para carregar skills

## Enxame de Agentes

1. **Intent Analyst** - Interpreta o pedido e extrai objetivos
2. **Skill Router** - Seleciona skills baseado em keywords e contexto
3. **Plan Builder** - Cria plano de execucao com ordem e dependencias
4. **Asset Gate** - Verifica assets necessarios antes de executar
5. **Quality Coordinator** - Orquestra revisoes e acceptance

## Processo Obrigatorio

1. Receba o pedido do usuario
2. Classifique a intencao (hero, landing, scroll, 3D, microinteraction, etc)
3. Selecione skills necessarias
4. Verifique assets (logo, imagens, copy, fontes, 3D, etc)
5. Produza plano de execucao
6. Dispatch para skills especializadas
7. Coordene revisoes (performance, a11y, motion)
8. Entregue snapshot com evidencias

## Roteamento por Intencao

| Intencao | Skills Ativadas |
|----------|----------------|
| Hero com scroll | cerebro + gsap-scrolltrigger + lenis + motion-fundamentals |
| Landing page | cerebro + ui-ux-fundamentals + gsap + lenis + a11y |
| Hero 3D | cerebro + r3f-threejs-drei + webgpu + performance-budget |
| Microinteracao | cerebro + rive ou lottie + motion-fundamentals |
| Site completo | cerebro + todas as skills relevantes |

## Contratos

Ver INPUT_CONTRACT.yaml e OUTPUT_CONTRACT.yaml para schema completo.

## Exemplo de Fluxo

```
[IDE carrega automaticamente]
→ skills/cerebro-orquestrador/SKILL.md
→ skills/gsap-scrolltrigger/SKILL.md
→ skills/lenis/SKILL.md
→ ... (todas as 26 skills)

[Usuario]
→ "Quero um hero com scroll que revela produtos"

[Cerebro]
→ intent_type: hero_scroll
→ selected_skills: [gsap-scrolltrigger, lenis, accessibility-a11y, performance-budget]
→ asset_state: asset_pending (logo, imagens)
→ delivery_state: prototype
→ next_action: "Aguardar logo e imagens para final delivery"
```
