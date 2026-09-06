# cerebro-orquestrador

**Skill compactada — conteudo completo**
Fonte: `skills/cerebro-orquestrador/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Cérebro Orquestrador

## Manifesto

Orquestra todas as outras skills, classificando intencao do usuario e delegando para agents especializados.

## Stack

- Python/JavaScript para logica de classificacao
- YAML para contratos de input/output
- Markdown para documentacao

## Keywords

orquestracao, classificacao, intencao, delegation, workflow, agent, skill-routing

## Visao Geral

O cerebro-orquestrador e a skill principal que:
1. Le todas as outras skills
2. Classifica a intencao do usuario
3. Seleciona skills relevantes
4. Delega para agents especializados
5. Consolida o resultado final

================================================================================
## 📄 AGENTS.md
================================================================================

# Agents — Cérebro Orquestrador

## Enxame de Agents

### ClassifierAgent
**Responsabilidade:** Classificar intencao do usuario.

**Input:**
```yaml
user_request: "Quero um hero com scroll que revela produtos"
all_skills: [lista de todas as skills]
```

**Output:**
```yaml
intent_type: hero_scroll
confidence: 0.98
matched_skills: [gsap-scrolltrigger, lenis, accessibility-a11y, performance-budget]
```

### RouterAgent
**Responsabilidade:** Selecionar skills baseado na intencao.

### OrchestratorAgent
**Responsabilidade:** Coordenar execucao dos agents especializados.

### ConsolidatorAgent
**Responsabilidade:** Consolidar resultados de todos os agents.

================================================================================
## 📄 WORKFLOW.md
================================================================================

# Workflow — Cérebro Orquestrador

Fluxo obrigatorio para todas as solicitacoes.

## Visao Geral

```
SOLICITACAO DO USUARIO
         │
         ▼
┌─────────────────────────────────┐
│ 1. CARREGAR TODAS AS SKILLS     │
│    skills/*/SKILL.md            │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 2. CARREGAR TREINAMENTO         │
│    agentes-training/*.txt       │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 3. CLASSIFICAR INTENCAO         │
│    hero_scroll, landing, etc.   │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 4. SELECIONAR SKILLS            │
│    Primary + Secondary + Required│
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 5. DELEGAR PARA AGENTS          │
│    Architect, Code, Asset,      │
│    Quality, Evidence            │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 6. CONSOLIDAR E ENTREGAR        │
│    Codigo + Assets + Evidence   │
└─────────────────────────────────┘
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

## Passo 2: Carregar Materiais de Treinamento

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

## Passo 3: Classificar Intencao

**Objetivo:** Entender o que o usuario quer construir.

**Categorias:**
- `hero_scroll` — Hero com scroll que revela conteudo
- `landing` — Landing page completa
- `hero_3d` — Hero com 3D, particulas, shaders
- `microinteraction` — Buttons, cards, hover effects
- `site_completo` — Site multi-page
- `page_transition` — Transicoes de pagina
- `generative` — Arte generativa, creative coding
- `audio_interactive` — Audio/visual interativo

## Passo 4: Selecionar Skills

**Objetivo:** Escolher as skills relevantes para a intencao.

## Passo 5: Delegar para Agents

**Objetivo:** Distribuir trabalho para agents especializados.

## Passo 6: Consolidar e Entregar

**Objetivo:** Entregar pacote completo ao usuario.

## Metricas de Sucesso

| Metrica | Target |
|---------|--------|
| Intent Accuracy | > 95% |
| Skill Relevance | > 90% |
| Training Material Coverage | 100% |
| Asset Detection | 100% |
| Response Time | < 500ms |
| User Clarity | > 4.5/5 |

================================================================================
## 📄 INPUT_CONTRACT.yaml
================================================================================

intent_type: hero_scroll | landing | hero_3d | microinteraction | site_completo | page_transition | generative | audio_interactive
user_request: string
all_skills: array
  - name: string
    manifest: string
    agents: string
    workflow: string
    keywords: array
training_materials: array
  - name: string
    content: string
    patterns: array
    techniques: array

delivery_state: prototype | ready

================================================================================
## 📄 OUTPUT_CONTRACT.yaml
================================================================================

intent_type: string
confidence: float (0-1)
matched_skills: array
selected_skills:
  primary: string
  secondary: array
  required: array
delegated_agents: array
  - name: string
    responsibility: string
    input: object
    output: object
consolidated_output:
  code: string
  asset_instructions: string
  quality_report: object
  evidence: object

delivery_state: prototype | ready

================================================================================
## 📄 QUALITY_GATE.md
================================================================================

# Quality Gate — Cérebro Orquestrador

## Checklist de Qualidade

- [ ] Todas as skills foram carregadas
- [ ] Materiais de treinamento foram consultados
- [ ] Intencao foi classificada corretamente
- [ ] Skills relevantes foram selecionadas
- [ ] Agents especializados foram delegados
- [ ] Resultado foi consolidado corretamente

## Metricas

| Metrica | Target | Como Medir |
|---------|--------|------------|
| Intent Accuracy | > 95% | Testes com exemplos conhecidos |
| Skill Relevance | > 90% | Feedback do usuario |
| Response Time | < 500ms | Benchmark de execucao |

## Validacao

```pseudo
function validateOutput(output):
  assert output.intent_type is not None
  assert output.confidence > 0.5
  assert len(output.matched_skills) > 0
  assert output.selected_skills.primary is not None
  assert len(output.delegated_agents) > 0
  assert output.consolidated_output.code is not None
  assert output.consolidated_output.asset_instructions is not None
  return True
```

================================================================================
## 📄 IMPLEMENTATION.md
================================================================================

# Implementacao — Cérebro Orquestrador

## Arquitetura

```
┌─────────────────────────────────────────┐
│           Cérebro Orquestrador          │
├─────────────────────────────────────────┤
│  ClassifierAgent                        │
│  RouterAgent                            │
│  OrchestratorAgent                      │
│  ConsolidatorAgent                      │
└─────────────────────────────────────────┘
```

## Implementacao em Python

```python
class CerebroOrquestrador:
    def __init__(self, skills_dir, training_dir):
        self.skills_dir = skills_dir
        self.training_dir = training_dir
        self.skills_index = self.load_all_skills()
        self.training_index = self.load_training_materials()
    
    def process_request(self, user_request):
        # Passo 3: Classificar intencao
        intent = self.classify_intent(user_request)
        
        # Passo 4: Selecionar skills
        selected_skills = self.select_skills(intent)
        
        # Passo 5: Delegar para agents
        agents_output = self.delegate_agents(intent, selected_skills)
        
        # Passo 6: Consolidar
        consolidated = self.consolidate(agents_output)
        
        return consolidated
    
    def classify_intent(self, user_request):
        keywords = extract_keywords(user_request)
        matched = match_keywords(keywords, self.skills_index)
        intent_type = determine_intent_type(matched)
        confidence = calculate_confidence(matched)
        
        return {
            'type': intent_type,
            'confidence': confidence,
            'matched_skills': matched
        }
    
    def select_skills(self, intent):
        mapping = {
            'hero_scroll': {
                'primary': 'gsap-scrolltrigger',
                'secondary': ['lenis', 'motion-framer'],
                'required': ['accessibility-a11y', 'performance-budget']
            },
            # ... outras intencoes
        }
        return mapping.get(intent['type'], {})
    
    def delegate_agents(self, intent, selected_skills):
        agents = [
            ArchitectAgent(intent, selected_skills),
            CodeAgent(intent, selected_skills),
            AssetAgent(intent, selected_skills),
            QualityAgent(intent, selected_skills),
            EvidenceAgent(intent, selected_skills)
        ]
        
        return [agent.execute() for agent in agents]
    
    def consolidate(self, agents_output):
        return {
            'code': agents_output[1].code,
            'asset_instructions': agents_output[2].instructions,
            'quality_report': agents_output[3].report,
            'evidence': agents_output[4].evidence
        }
```

## Implementacao em JavaScript

```javascript
class CerebroOrquestrador {
  constructor(skillsDir, trainingDir) {
    this.skillsDir = skillsDir;
    this.trainingDir = trainingDir;
    this.skillsIndex = this.loadAllSkills();
    this.trainingIndex = this.loadTrainingMaterials();
  }
  
  async processRequest(userRequest) {
    const intent = this.classifyIntent(userRequest);
    const selectedSkills = this.selectSkills(intent);
    const agentsOutput = await this.delegateAgents(intent, selectedSkills);
    return this.consolidate(agentsOutput);
  }
  
  classifyIntent(userRequest) {
    const keywords = extractKeywords(userRequest);
    const matched = matchKeywords(keywords, this.skillsIndex);
    const intentType = determineIntentType(matched);
    const confidence = calculateConfidence(matched);
    
    return { type: intentType, confidence, matchedSkills: matched };
  }
  
  selectSkills(intent) {
    const mapping = {
      hero_scroll: {
        primary: 'gsap-scrolltrigger',
        secondary: ['lenis', 'motion-framer'],
        required: ['accessibility-a11y', 'performance-budget']
      }
    };
    return mapping[intent.type] || {};
  }
  
  async delegateAgents(intent, selectedSkills) {
    const agents = [
      new ArchitectAgent(intent, selectedSkills),
      new CodeAgent(intent, selectedSkills),
      new AssetAgent(intent, selectedSkills),
      new QualityAgent(intent, selectedSkills),
      new EvidenceAgent(intent, selectedSkills)
    ];
    
    return await Promise.all(agents.map(agent => agent.execute()));
  }
  
  consolidate(agentsOutput) {
    return {
      code: agentsOutput[1].code,
      asset_instructions: agentsOutput[2].instructions,
      quality_report: agentsOutput[3].report,
      evidence: agentsOutput[4].evidence
    };
  }
}
```

================================================================================
## 📄 EVALS.md
================================================================================

# Evals — Cérebro Orquestrador

## Testes de Classificacao de Intencao

### Test 1: Hero Scroll

**Input:**
```
"Quero um hero com scroll que revela produtos"
```

**Expected Output:**
```yaml
intent_type: hero_scroll
confidence: 0.98
matched_skills:
  - gsap-scrolltrigger
  - lenis
  - accessibility-a11y
  - performance-budget
```

### Test 2: Hero 3D

**Input:**
```
"Hero 3D com particulas que seguem o mouse"
```

**Expected Output:**
```yaml
intent_type: hero_3d
confidence: 0.95
matched_skills:
  - r3f-threejs-drei
  - webgpu-gpgpu
  - lygia
  - performance-budget
```

### Test 3: Landing Completa

**Input:**
```
"Preciso de uma landing page para meu SaaS"
```

**Expected Output:**
```yaml
intent_type: landing
confidence: 0.92
matched_skills:
  - gsap-scrolltrigger
  - lenis
  - barba-swup
  - accessibility-a11y
  - performance-budget
  - seo-metadata
```

## Metricas de Avaliacao

| Metrica | Target | Como Medir |
|---------|--------|------------|
| Intent Accuracy | > 95% | Testes com exemplos conhecidos |
| Skill Relevance | > 90% | Feedback do usuario |
| Response Time | < 500ms | Benchmark de execucao |
| User Clarity | > 4.5/5 | Pesquisa de satisfacao |

## Benchmark de Performance

```python
import time

def benchmark_cerebro():
    cerebro = CerebroOrquestrador('skills/', 'agentes-training/')
    
    test_cases = [
        "Quero um hero com scroll que revela produtos",
        "Hero 3D com particulas que seguem o mouse",
        "Preciso de uma landing page para meu SaaS"
    ]
    
    times = []
    for request in test_cases:
        start = time.time()
        cerebro.process_request(request)
        end = time.time()
        times.append((end - start) * 1000)  # ms
    
    avg_time = sum(times) / len(times)
    print(f"Tempo medio: {avg_time:.2f}ms")
    assert avg_time < 500, "Response time > 500ms"
```

================================================================================
## 📄 examples/hero-scroll-request.yaml
================================================================================

```yaml
intent_type: hero_scroll
user_request: "Quero um hero com scroll que revela produtos"
all_skills:
  - name: gsap-scrolltrigger
    manifest: "Animacoes baseadas em scroll usando GSAP ScrollTrigger."
    agents: [ScrollAnimationAgent, PinAgent, ParallaxAgent]
    keywords: [scroll, animation, gsap, scrolltrigger, reveal, parallax, pin, scrub]
  - name: lenis
    manifest: "Smooth scroll moderno e leve."
    agents: [SmoothScrollAgent]
    keywords: [smooth, scroll, lenis, inertia, momentum]
  - name: accessibility-a11y
    manifest: "Acessibilidade WCAG AA."
    agents: [A11yAgent]
    keywords: [accessibility, a11y, wcag, keyboard, screen-reader]
  - name: performance-budget
    manifest: "Performance e otimizacao."
    agents: [PerfAgent]
    keywords: [performance, budget, optimization, lighthouse]
training_materials:
  - name: GSAP_ENGENHARIA_REVERSA_ULTRA_100_PAGINAS.txt
    content: "..."
    patterns: [scroll-reveal, smooth-scroll, parallax]
  - name: LENIS-ENGENHARIA-REVERSA-100-PAGINAS.txt
    content: "..."
    patterns: [smooth-scroll, inertia-scroll]

delivery_state: ready
```

