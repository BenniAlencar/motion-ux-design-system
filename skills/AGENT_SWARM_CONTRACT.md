# Skill Swarm Contract

**Status:** proposed  
**Purpose:** transformar cada skill em um enxame auditavel de agentes, usando os materiais de `agentes-training/` como fontes de conhecimento.

## Regra de verdade

Uma skill so pode ser marcada como `enriched` quando houver:

- matriz de proveniencia com fontes existentes;
- conteudo-fonte preservado ou referenciado por hash;
- agentes especializados explicitamente definidos;
- input/output contract;
- workflow com gates e rollback;
- exemplos ou fixtures de teste;
- validacao local do gerador.

`SKILL.md` sozinho nao e um enxame.

## Estrutura minima

Cada skill enriquecida deve conter:

```text
skills/<skill>/
├── SKILL.md
├── AGENTS.md
├── WORKFLOW.md
├── INPUT_CONTRACT.yaml
├── OUTPUT_CONTRACT.yaml
├── QUALITY_GATE.md
├── ROLLBACK.md
├── TRAINING_SOURCES.yaml
├── agents/
│   ├── architect.md
│   ├── implementation.md
│   ├── integration.md
│   ├── performance.md
│   ├── accessibility.md
│   ├── quality.md
│   └── evidence.md
└── examples/
```

## Agentes minimos

- `architect`: decide arquitetura e dependencias.
- `implementation`: produz codigo ou configuracao.
- `integration`: integra com outras skills e runtime.
- `performance`: aplica budgets e mede custo.
- `accessibility`: garante teclado, semantica e reduced motion quando aplicavel.
- `quality`: executa checklist e rejeita claims sem evidencia.
- `evidence`: registra testes, versoes, metricas e limitacoes.

Skills visuais podem adicionar agentes especializados, por exemplo:

- `camera-motion`;
- `scroll-systems`;
- `shader`;
- `scene-3d`;
- `physics`;
- `audio`;
- `asset-pipeline`.

## Proveniencia

Cada skill deve declarar fontes em `TRAINING_SOURCES.yaml`:

```yaml
skill: gsap-scrolltrigger
status: proposed
sources:
  - path: agentes-training/GSAP_x5f_ENGENHARIA_x5f_REVERSA_x5f_ULTRA_x5f_100_x5f_PAGINAS (7).txt
    role: primary
  - path: agentes-training/SCROLLTRIGGER_x5f_ENGENHARIA_x5f_REVERSA_x5f_TOTAL (6).txt
    role: primary
  - path: agentes-training/BENNI_x5f_MASTER_x5f_OS_x5f_V10_x5f_ULTRA_x5f_200_x5f_PADROES.txt
    role: cross-cutting
```

A fonte orienta; nao substitui testes, documentacao oficial ou revisao humana.

## Integracao autonoma

O Brain deve:

1. interpretar o resultado desejado;
2. consultar a matriz de proveniencia;
3. ativar os enxames relevantes;
4. incluir `performance`, `accessibility`, `quality` e `evidence` quando aplicavel;
5. declarar `unknown` quando a capability, fonte ou teste nao estiver disponivel;
6. nunca alegar execucao, producao ou metricas sem evidencia datada.

## Mobile e desktop

Todo enxame visual deve declarar:

- estrategia mobile-first;
- adaptacao touch/mouse/keyboard;
- reduced motion;
- fallback sem WebGL quando aplicavel;
- budgets por dispositivo;
- fixtures para pelo menos mobile, tablet e desktop.

## Criterio de promocao

`proposed -> enriched` somente apos:

- `python scripts/build_skill_swarms.py --check` passar;
- todas as fontes existirem;
- todos os arquivos estruturais existirem;
- nenhuma fonte ter sido substituida por resumo inventado;
- relatorio de cobertura ser gerado.
