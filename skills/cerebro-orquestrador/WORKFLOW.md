# Workflow — Cérebro Orquestrador

Fluxo obrigatorio para todas as solicitacoes.

## Visao Geral

```
┌─────────────────────────────────────────────────────────────┐
│                    SOLICITACAO DO USUARIO                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PASSO 1: CARREGAR TODAS AS SKILLS (skills/*/SKILL.md)     │
│  - gsap-scrolltrigger, lenis, r3f-threejs-drei, etc.       │
│  - Ler SKILL.md, AGENTS.md, WORKFLOW.md de cada skill      │
│  - Extrair keywords de cada skill                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PASSO 2: CARREGAR MATERIAIS DE TREINAMENTO (OBRIGATORIO)  │
│  - agentos-training/*.txt (40+ arquivos, ~5MB)             │
│  - BENNI_MASTER_OS_V10_*.txt                               │
│  - CODIGOS_SECRETOS_DOMINAM_TUDO_V11.txt                   │
│  - PACOTE_DOMINA_TUDO_V11_FINAL.txt                        │
│  - Shopify_Editions_Winter26_*.txt                         │
│  - GSAP_*.txt, Lenis_*.txt, ThreeJS_*.txt, etc.            │
│  - Extrair padroes, tecnicas, codigos de cada arquivo      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PASSO 3: CLASSIFICAR INTENCAO DO USUARIO                  │
│  - hero_scroll, landing, hero_3d, microinteraction, etc.   │
│  - Usar keywords do Passo 1 + padroes do Passo 2           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PASSO 4: SELECIONAR SKILLS RELEVANTES                     │
│  - Primary: skill principal para intencao                  │
│  - Secondary: skills complementares                        │
│  - Required: accessibility-a11y, performance-budget        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PASSO 5: DELEGAR PARA AGENTS ESPECIALIZADOS               │
│  - ArchitectAgent: estrutura do projeto                    │
│  - CodeAgent: implementacao do codigo                      │
│  - AssetAgent: instrucoes de assets nao-codigo             │
│  - QualityAgent: validacao de qualidade                    │
│  - EvidenceAgent: coleta de metrics e screenshots          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  PASSO 6: CONSOLIDAR E ENTREGAR                            │
│  - Codigo completo                                         │
│  - Asset instructions claras                               │
│  - Evidence packet completo                                │
└─────────────────────────────────────────────────────────────┘
```

## Passo 1: Carregar Todas as Skills

**Objetivo:** Ter contexto completo de todas as capacidades disponiveis.

**Acao:**
```pseudo
function loadAllSkills():
  skillsDir = "skills/"
  allSkills = []
  
  for skillFolder in listDirectories(skillsDir):
    skill = {
      name: skillFolder,
      manifest: readFile(skillsDir + skillFolder + "/SKILL.md"),
      agents: readFile(skillsDir + skillFolder + "/AGENTS.md"),
      workflow: readFile(skillsDir + skillFolder + "/WORKFLOW.md"),
      inputContract: parseYaml(readFile(skillsDir + skillFolder + "/INPUT_CONTRACT.yaml")),
      outputContract: parseYaml(readFile(skillsDir + skillFolder + "/OUTPUT_CONTRACT.yaml")),
      keywords: extractKeywords(skillFolder + "/SKILL.md")
    }
    allSkills.push(skill)
  
  return buildKeywordIndex(allSkills)
```

**Output:** Indice de keywords mapeando cada skill as suas capacidades.

## Passo 2: Carregar Materiais de Treinamento (NOVO - OBRIGATORIO)

**Objetivo:** Incorporar todo o conhecimento tecnico dos arquivos de engenharia reversa e padroes.

**Acao:**
```pseudo
function loadTrainingMaterials():
  trainingDir = "agentes-training/"
  allMaterials = []
  
  for file in listFiles(trainingDir):
    if file.endsWith(".txt"):
      content = readFile(trainingDir + file)
      material = {
        name: file,
        content: content,
        patterns: extractPatterns(content),
        techniques: extractTechniques(content),
        codeSnippets: extractCodeSnippets(content)
      }
      allMaterials.push(material)
  
  return buildTrainingIndex(allMaterials)
```

**Arquivos a carregar:**
- `BENNI_MASTER_OS_V10_ARTE_SUPREMA_SEM_DEPENDENCIAS.txt`
- `BENNI_MASTER_OS_V10_ULTRA_200_PADROES.txt`
- `CODIGOS_SECRETOS_DOMINAM_TUDO_V11.txt`
- `PACOTE_DOMINA_TUDO_V11_FINAL.txt`
- `PACOTE_FINAL_DEDUPLICADO_V3.txt`
- `SHOPIFY_EDITIONS_WINTER26_ACIMA_AWWWARDS_LIMPO.txt`
- `SHOPIFY_EDITIONS_WINTER26_ULTRA_200_PADROES_LIMPO.txt`
- `GSAP_*`, `SCROLLTRIGGER_*`, `LENIS_*`, `LOCOMOTIVE_*`
- `THREEJS_*`, `R3F_*`, `DREI_*`, `SHADERS_*`
- `SPLINE_*`, `RIVE_*`, `LOTTIEFILES_*`, `THEATREJS_*`
- `BARBA_*`, `SWUP_*`, `PIXI_*`, `OGL_*`, `LYGIA_*`
- `WEBGPU_*`, `TONEJS_*`, `RAPIER_*`, `P5_*`
- `ANIMEJS_*`, `MOTION_*`, `TEMPLATE_PREMIADO_*`

**Output:** Indice de padroes, tecnicas e codigos extraidos de todo o material.

## Passo 3: Classificar Intencao

**Objetivo:** Entender o que o usuario quer construir.

**Categorias:**
- `hero_scroll` - Hero com scroll que revela conteudo
- `landing` - Landing page completa
- `hero_3d` - Hero com 3D, particulas, shaders
- `microinteraction` - Buttons, cards, hover effects
- `site_completo` - Site multi-page
- `page_transition` - Transicoes de pagina
- `generative` - Arte generativa, creative coding
- `audio_interactive` - Audio/visual interativo

**Acao:**
```pseudo
function classifyIntent(userRequest, skillsIndex, trainingIndex):
  keywords = extractKeywords(userRequest)
  matchedSkills = matchKeywords(keywords, skillsIndex)
  matchedPatterns = matchPatterns(keywords, trainingIndex)
  
  intent = {
    type: determineIntentType(matchedSkills, matchedPatterns),
    confidence: calculateConfidence(matchedSkills, matchedPatterns),
    matchedSkills: matchedSkills,
    matchedPatterns: matchedPatterns
  }
  
  return intent
```

## Passo 4: Selecionar Skills

**Objetivo:** Escolher as skills relevantes para a intencao.

**Mapeamento:**
```yaml
hero_scroll:
  primary: gsap-scrolltrigger
  secondary: [lenis, motion-framer]
  required: [accessibility-a11y, performance-budget]

hero_3d:
  primary: r3f-threejs-drei
  secondary: [webgpu-gpgpu, lygia, spline-runtime]
  required: [accessibility-a11y, performance-budget]

landing:
  primary: gsap-scrolltrigger
  secondary: [lenis, barba-swup]
  required: [accessibility-a11y, performance-budget, seo-metadata]

microinteraction:
  primary: motion-framer
  secondary: [gsap-core, animejs]
  required: [accessibility-a11y]

generative:
  primary: webgpu-gpgpu
  secondary: [p5js, rapier-physics]
  required: [performance-budget]

audio_interactive:
  primary: tonejs
  secondary: [webaudio-api, p5js]
  required: [accessibility-a11y, performance-budget]
```

## Passo 5: Delegar para Agents

**Objetivo:** Distribuir trabalho para agents especializados.

**Agents:**

### ArchitectAgent
**Responsabilidade:** Estrutura do projeto, selecao de templates, setup.

**Input:**
```yaml
intent_type: hero_scroll
selected_skills: [gsap-scrolltrigger, lenis, accessibility-a11y]
training_patterns: [scroll-reveal, smooth-scroll, parallax]
```

**Output:**
```yaml
project_structure:
  - src/components/Hero.tsx
  - src/styles/globals.css
  - public/assets/
dependencies: [gsap, @studio-freight/lenis]
template: hero-scroll-nextjs
```

### CodeAgent
**Responsabilidade:** Implementacao do codigo.

**Input:**
```yaml
project_structure: ...
selected_skills: ...
training_code_snippets: ...
```

**Output:**
```tsx
// src/components/Hero.tsx
import { useGSAP } from 'gsap-triggers'
import { useLenis } from '@studio-freight/lenis'

export default function Hero() {
  // implementacao completa
}
```

### AssetAgent
**Responsabilidade:** Gerar instrucoes claras de assets nao-codigo.

**Input:**
```yaml
intent_type: hero_scroll
selected_skills: ...
```

**Output:**
```markdown
Para entrega final, enviar:

1. Logo (SVG ou PNG, 500x500 min, fundo transparente)

2. Imagens:
   - Hero background (1920x1080, JPG, < 500kB)
   - Product shot 1 (800x600, PNG, fundo transparente)
   - Product shot 2 (800x600, PNG, fundo transparente)

3. Fontes: Inter (Google Fonts, gratuito)
```

### QualityAgent
**Responsabilidade:** Validar qualidade do codigo e experiencia.

**Checklist:**
- [ ] Lighthouse performance >= 80
- [ ] Frame time p95 < 16ms
- [ ] WCAG AA contraste
- [ ] Keyboard navigation completa
- [ ] Reduced motion respeitado

**Output:**
```yaml
quality_report:
  lighthouse_performance: 92
  frame_time_p95: 12ms
  wcag_aa_contrast: pass
  keyboard_navigation: pass
  reduced_motion: pass
```

### EvidenceAgent
**Responsabilidade:** Coletar evidencias de qualidade.

**Output:**
- Screenshots (desktop + mobile)
- Lighthouse metrics
- Frame time metrics
- Bundle size
- Video demos (scroll, keyboard, reduced-motion)

## Passo 6: Consolidar e Entregar

**Objetivo:** Entregar pacote completo ao usuario.

**Entrega:**
```yaml
delivery:
  code: src/components/Hero.tsx
  asset_instructions: asset-instructions-output.md
  quality_report: quality-report.yaml
  evidence:
    - screenshots/
    - lighthouse-report.json
    - video-demos/
  delivery_state: prototype | ready
```

## Metricas de Sucesso

| Metrica | Target |
|---------|--------|
| Intent Accuracy | > 95% |
| Skill Relevance | > 90% |
| Training Material Coverage | 100% |
| Asset Detection | 100% |
| Response Time | < 500ms |
| User Clarity | > 4.5/5 |

## Exemplo de Execucao

**Input do Usuario:**
```
"Quero um hero com scroll que revela produtos"
```

**Execucao:**

1. **Carregar Skills:** gsap-scrolltrigger, lenis, accessibility-a11y, performance-budget
2. **Carregar Treinamento:** GSAP_*.txt, LENIS_*.txt, SCROLLTRIGGER_*.txt
3. **Classificar:** intent_type = `hero_scroll`, confidence = 0.98
4. **Selecionar Skills:** primary=gsap-scrolltrigger, secondary=lenis, required=[a11y, perf]
5. **Delegar:**
   - ArchitectAgent: estrutura Next.js + dependencies
   - CodeAgent: Hero.tsx com GSAP ScrollTrigger + Lenis
   - AssetAgent: logo + 3 imagens
   - QualityAgent: validar performance + a11y
   - EvidenceAgent: screenshots + metrics
6. **Entregar:** codigo + asset instructions + evidence packet

**Output:**
```tsx
// Codigo completo do Hero
```

```markdown
## Asset Instructions

Para entrega final, enviar:
1. Logo (SVG ou PNG, 500x500 min)
2. Hero background (1920x1080, JPG)
3. Product shots (800x600, PNG)
```

```yaml
# Evidence Packet
delivery_state: prototype
quality_report:
  lighthouse_performance: 92
  wcag_aa_contrast: pass
```

## Rollback

Se algo falhar:
- Reverter para `WORKFLOW.md` anterior
- Manter consulta de skills (Passo 1)
- Manter classificacao de intencao (Passo 3)
- Opcional: remover consulta de treinamento (Passo 2) se causar lentidao
