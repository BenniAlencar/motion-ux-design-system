# Skills Compact

Pasta com todas as skills compactadas em **arquivos unicos** para facilitar uso em IDEs e agentes de IA.

## Como Usar

### Opcao 1: Carregar Skill Especifica (Recomendado)

No Perplexity ou outra IDE, carregue apenas o arquivo da skill que voce precisa:

```
@skills-compact/gsap-scrolltrigger.md
@skills-compact/lenis.md
@skills-compact/r3f-threejs-drei.md
```

**Vantagem:** Menor uso de contexto, mais rapido.

### Opcao 2: Carregar Todas as Skills

Se sua IDE suportar, carregue toda a pasta `skills-compact/` de uma vez.

**Vantagem:** Contexto completo de todas as skills.

## Estrutura de Cada Arquivo

Cada arquivo `{skill}.md` contem:

```
# {skill}

## SKILL.md
- Manifesto, stack, keywords

## AGENTS.md
- Enxame de agents da skill

## WORKFLOW.md
- Fluxo de trabalho

## INPUT_CONTRACT.yaml
- Schema de entrada

## OUTPUT_CONTRACT.yaml
- Schema de saida

## PATTERNS.md
- Padroes e exemplos de codigo

## examples/
- Exemplos praticos de implementacao
```

## Lista de Skills

| Skill | Arquivo |
|-------|---------|
| GSAP + ScrollTrigger | `gsap-scrolltrigger.md` |
| Lenis | `lenis.md` |
| R3F + Three.js + Drei | `r3f-threejs-drei.md` |
| Motion + Framer | `motion-framer.md` |
| Accessibility A11y | `accessibility-a11y.md` |
| Performance Budget | `performance-budget.md` |
| Asset Gate | `asset-gate.md` |
| Quality Gate | `quality-gate.md` |
| Cerebro Orquestrador | `cerebro-orquestrador.md` |
| WebGPU + GPGPU | `webgpu-gpgpu.md` |
| Spline Runtime | `spline-runtime.md` |
| LottieFiles | `lottiefiles.md` |
| Rive | `rive.md` |
| Theatre.js | `theatrejs.md` |
| Tone.js | `tonejs.md` |
| Barba | `barba.md` |
| Swup | `swup.md` |
| Locomotive Scroll | `locomotive-scroll.md` |
| ScrollSmoother | `scrollsmoother.md` |
| Observer | `observer.md` |
| Flip | `flip.md` |
| Anime.js | `animejs.md` |
| Lygia | `lygia.md` |
| Pixi | `pixi.md` |
| OGL | `ogl.md` |
| P5.js | `p5js.md` |
| Rapier | `rapier.md` |
| WebGPU WGSL/TSL | `webgpu-wgsl-tsl.md` |

## Exemplo de Uso no Perplexity

**Prompt:**
```
@skills-compact/gsap-scrolltrigger.md @skills-compact/lenis.md

Quero um hero com scroll que revela produtos.
```

**Resposta esperada:**
- Codigo completo usando GSAP ScrollTrigger + Lenis
- Asset instructions claras
- Evidence packet com metrics de qualidade

## Atualizacao

Para regenerar os arquivos compactados:

```bash
python scripts/compact_skills.py
```

Isso vai ler todas as skills em `skills/` e gerar arquivos atualizados em `skills-compact/`.

---

**Nota:** Esta pasta e gerada automaticamente. Nao edite os arquivos manualmente.
