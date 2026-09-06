# Agentes Training

Instrucoes e materiais para treinar agentes autonomos no Motion/UX Design System.

## Objetivo

Treinar agentes para:
1. Ler automaticamente TODAS as skills em toda solicitacao
2. Classificar intencao do usuario
3. Selecionar skills relevantes
4. Executar workflows autonomamente
5. Gerar instrucoes claras de assets nao-codigo
6. Entregar evidence packet completo

## Materiais de Treinamento

### 1. Skills como Contexto

Cada agente deve ler:
- `skills/*/SKILL.md` - Manifesto e stack
- `skills/*/AGENTS.md` - Enxame de agentes
- `skills/*/WORKFLOW.md` - Fluxo obrigatorio
- `skills/*/INPUT_CONTRACT.yaml` - Schema de entrada
- `skills/*/OUTPUT_CONTRACT.yaml` - Schema de saida

### 2. Exemplos de Input/Output

Ver `skills/*/examples/` para:
- `hero-scroll-request.yaml` - Exemplo de entrada
- `hero-scroll.tsx` - Exemplo de codigo
- `asset-instructions-output.md` - Exemplo de instrucoes
- `quality-report.yaml` - Exemplo de evidence packet

### 3. Templates

Ver `templates/` para:
- `hero-scroll-nextjs/` - Template pronto para usar

## Protocolo de Treinamento

### Passo 1: Carregamento Automatico

O agente DEVE:
```pseudo
function onRequest(userRequest):
  allSkills = readDirectory("skills/")
  for skill in allSkills:
    skill.manifest = readFile(skill + "/SKILL.md")
    skill.agents = readFile(skill + "/AGENTS.md")
    skill.workflow = readFile(skill + "/WORKFLOW.md")
    skill.keywords = parseKeywords(skill.manifest)
  
  keywordIndex = buildKeywordIndex(allSkills)
  return processRequest(userRequest, keywordIndex)
```

### Passo 2: Classificacao de Intencao

O agente DEVE classificar em:
- `hero_scroll` - Hero com scroll que revela conteudo
- `landing` - Landing page completa
- `hero_3d` - Hero com 3D/particulas
- `microinteraction` - Microinteracoes (buttons, cards)
- `site_completo` - Site multi-page
- `page_transition` - Transicoes de pagina
- `generative` - Arte generativa
- `audio_interactive` - Audio interativo

### Passo 3: Selecao de Skills

O agente DEVE selecionar baseado em keywords:
```yaml
hero_scroll:
  - gsap-scrolltrigger (primary)
  - lenis (primary)
  - accessibility-a11y (required)
  - performance-budget (required)

hero_3d:
  - r3f-threejs-drei (primary)
  - webgpu-gpgpu (primary)
  - lygia (secondary)
  - performance-budget (required)
  - accessibility-a11y (required)
```

### Passo 4: Asset Gate

O agente DEVE gerar instrucoes claras:
```markdown
Para entrega final, enviar:

1. Logo (SVG ou PNG, 500x500 min, fundo transparente)

2. Imagens:
   - Hero background (1920x1080, JPG, < 500kB)
   - Product shot 1 (800x600, PNG, fundo transparente)
   - Product shot 2 (800x600, PNG, fundo transparente)

3. Fontes: Inter (Google Fonts, gratuito)
```

### Passo 5: Quality Gate

O agente DEVE validar:
- [ ] Lighthouse performance >= 80
- [ ] Frame time p95 < 16ms
- [ ] WCAG AA contraste
- [ ] Keyboard navigation completa
- [ ] Reduced motion respeitado

### Passo 6: Evidence Packet

O agente DEVE coletar:
- Screenshots (desktop + mobile)
- Lighthouse metrics
- Frame time metrics
- Bundle size
- Video demos (scroll, keyboard, reduced-motion)

## Testes de Validacao

### Test 1: Hero Scroll

**Input:**
```
"Quero um hero com scroll que revela produtos"
```

**Expected Output:**
- intent_type: `hero_scroll`
- selected_skills: `[gsap-scrolltrigger, lenis, accessibility-a11y, performance-budget]`
- asset_instructions: logo + 3 imagens
- delivery_state: `prototype` (sem assets)

### Test 2: Hero 3D

**Input:**
```
"Hero 3D com particulas que seguem o mouse"
```

**Expected Output:**
- intent_type: `hero_3d`
- selected_skills: `[r3f-threejs-drei, webgpu-gpgpu, lygia]`
- asset_instructions: modelos 3D + texturas
- delivery_state: `prototype` (sem assets)

### Test 3: Landing Completa

**Input:**
```
"Preciso de uma landing page para meu SaaS"
```

**Expected Output:**
- intent_type: `landing`
- narrative: 5 acts (hero, problem, solution, features, cta)
- selected_skills: `[gsap-scrolltrigger, lenis, motion-framer]`
- asset_instructions: logo + screenshots do produto

## Metricas de Sucesso

| Metrica | Target |
|---------|--------|
| Intent Accuracy | > 95% |
| Skill Relevance | > 90% |
| Asset Detection | 100% |
| Response Time | < 500ms |
| User Clarity | > 4.5/5 |

## Proximos Passos

1. Treinar agente com exemplos em `skills/*/examples/`
2. Validar com testes acima
3. Iterar baseado em feedback
4. Expandir para mais casos de uso

## Contato

Dudas: Benni Alencar
