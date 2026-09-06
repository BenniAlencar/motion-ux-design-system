# Skills Compact

Pasta com todas as 28 skills compactadas em **arquivos unicos .md** com **conteudo COMPLETO**.

Cada arquivo `{skill}.md` tem ~10KB+ com TODO o conteudo dos arquivos originais da skill.

---

## Como Usar no Perplexity/IDEs

### Opcao 1: Carregar Skill Especifica (Recomendado)

No Perplexity, carregue apenas o arquivo da skill que voce precisa:

```
@skills-compact/gsap-scrolltrigger.md
@skills-compact/lenis.md
@skills-compact/r3f-threejs-drei.md
@skills-compact/cerebro-orquestrador.md
```

**Vantagem:** Menor uso de contexto, mais rapido, focado na skill necessaria.

### Opcao 2: Carregar Multiplas Skills

Carregue varias skills juntas para projetos mais complexos:

```
@skills-compact/gsap-scrolltrigger.md @skills-compact/lenis.md @skills-compact/accessibility-a11y.md

Quero um hero com scroll que revela produtos.
```

### Opcao 3: Carregar Toda a Pasta

Se sua IDE suportar, carregue toda a pasta `skills-compact/` de uma vez.

**Vantagem:** Contexto completo de todas as 28 skills.

---

## Estrutura de Cada Arquivo

Cada `{skill}.md` contem TODO o conteudo completo dos arquivos originais:

```
# {skill}

## 📄 SKILL.md
Conteudo completo do arquivo SKILL.md original

## 📄 AGENTS.md
Conteudo completo do arquivo AGENTS.md original

## 📄 WORKFLOW.md
Conteudo completo do arquivo WORKFLOW.md original

## 📄 INPUT_CONTRACT.yaml
Conteudo completo do arquivo INPUT_CONTRACT.yaml original

## 📄 OUTPUT_CONTRACT.yaml
Conteudo completo do arquivo OUTPUT_CONTRACT.yaml original

## 📄 PATTERNS.md
Conteudo completo do arquivo PATTERNS.md original (se existir)

## 📄 IMPLEMENTATION.md
Conteudo completo do arquivo IMPLEMENTATION.md original (se existir)

## 📄 QUALITY_GATE.md
Conteudo completo do arquivo QUALITY_GATE.md original (se existir)

## 📄 EVALS.md
Conteudo completo do arquivo EVALS.md original (se existir)

## 📄 examples/
Conteudo completo de todos os arquivos de exemplo
```

---

## Lista de Skills (28 total)

| # | Skill | Arquivo | Tamanho Aprox |
|---|-------|---------|---------------|
| 1 | Cerebro Orquestrador | `cerebro-orquestrador.md` | ~22KB |
| 2 | GSAP + ScrollTrigger | `gsap-scrolltrigger.md` | ~10KB |
| 3 | Lenis | `lenis.md` | ~5KB |
| 4 | R3F + Three.js + Drei | `r3f-threejs-drei.md` | ~15KB |
| 5 | Motion + Framer | `motion-framer.md` | ~5KB |
| 6 | Accessibility A11y | `accessibility-a11y.md` | ~8KB |
| 7 | Performance Budget | `performance-budget.md` | ~5KB |
| 8 | Asset Gate | `asset-gate.md` | ~12KB |
| 9 | Quality Gate | `quality-gate.md` | ~10KB |
| 10 | WebGPU + GPGPU | `webgpu-gpgpu.md` | ~12KB |
| 11 | Spline Runtime | `spline-runtime.md` | ~8KB |
| 12 | LottieFiles | `lottiefiles.md` | ~8KB |
| 13 | Rive | `rive.md` | ~8KB |
| 14 | Theatre.js | `theatrejs.md` | ~8KB |
| 15 | Tone.js | `tonejs.md` | ~8KB |
| 16 | Barba | `barba.md` | ~8KB |
| 17 | Swup | `swup.md` | ~8KB |
| 18 | Locomotive Scroll | `locomotive-scroll.md` | ~8KB |
| 19 | ScrollSmoother | `scrollsmoother.md` | ~8KB |
| 20 | Observer | `observer.md` | ~8KB |
| 21 | Flip | `flip.md` | ~8KB |
| 22 | Anime.js | `animejs.md` | ~8KB |
| 23 | Lygia | `lygia.md` | ~8KB |
| 24 | Pixi | `pixi.md` | ~8KB |
| 25 | OGL | `ogl.md` | ~8KB |
| 26 | P5.js | `p5js.md` | ~8KB |
| 27 | Rapier | `rapier.md` | ~8KB |
| 28 | WebGPU WGSL/TSL | `webgpu-wgsl-tsl.md` | ~8KB |

---

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

---

## Geracao dos Arquivos

Os arquivos sao gerados automaticamente pelo script:

```bash
python scripts/generate_all_compact_skills.py
```

Isso vai:
1. Ler todas as skills em `skills/`
2. Consolidar TODOS os arquivos de cada skill
3. Gerar `{skill}.md` com conteudo COMPLETO em `skills-compact/`

---

## Status

- ✅ `cerebro-orquestrador.md` — 22KB, 9 arquivos + exemplos
- ✅ `gsap-scrolltrigger.md` — 10KB, 6 arquivos + exemplos
- 🔄 Demais 26 skills — Em geracao

---

**Nota:** Esta pasta e gerada automaticamente. Nao edite os arquivos manualmente.
