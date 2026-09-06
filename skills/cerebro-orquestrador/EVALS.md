---
name: cerebro-evals
version: 1.0.0
---

# Cerebro - Avaliacao e Testes

## Test Cases

### Test 1: Hero Scroll

**Input:**
```yaml
user_request: "Quero um hero com scroll que revela produtos"
context:
  project_name: "Minha Landing"
  brand_name: "Minha Marca"
  industry: "tech"
```

**Expected Output:**
```yaml
intent_type: hero_scroll
selected_skills:
  - gsap-scrolltrigger
  - lenis
  - accessibility-a11y
  - performance-budget
asset_state: asset_pending
next_action: "Aguardar logo e imagens para final delivery"
```

**Pass Criteria:**
- intent_type == 'hero_scroll'
- gsap-scrolltrigger e lenis estao em selected_skills
- asset_state == 'asset_pending' (sem assets fornecidos)
- next_action menciona assets faltantes

---

### Test 2: Landing Page

**Input:**
```yaml
user_request: "Preciso de uma landing page para meu SaaS"
context:
  project_name: "Meu SaaS"
  industry: "tech"
  tone: "minimalist"
```

**Expected Output:**
```yaml
intent_type: landing
selected_skills:
  - gsap-scrolltrigger
  - lenis
  - motion-framer
  - accessibility-a11y (required)
  - performance-budget (required)
narrative:
  - act: hero
  - act: problem
  - act: solution
  - act: features
  - act: cta
```

**Pass Criteria:**
- intent_type == 'landing'
- narrative tem 5 acts (hero, problem, solution, features, cta)
- accessibility-a11y e performance-budget sao required

---

### Test 3: Hero 3D

**Input:**
```yaml
user_request: "Hero 3D com particulas que seguem o mouse"
context:
  project_name: "Portfolio 3D"
```

**Expected Output:**
```yaml
intent_type: hero_3d
selected_skills:
  - r3f-threejs-drei (primary)
  - webgpu-gpgpu (primary)
  - lygia (secondary)
  - performance-budget (required)
  - accessibility-a11y (required)
asset_instructions: "Enviar modelos 3D, texturas, HDR environment"
```

**Pass Criteria:**
- intent_type == 'hero_3d'
- r3f-threejs-drei e webgpu-gpgpu sao primary
- asset_instructions menciona modelos 3D

---

### Test 4: Microinteracoes

**Input:**
```yaml
user_request: "Microinteracoes para botoes e cards"
```

**Expected Output:**
```yaml
intent_type: microinteraction
selected_skills:
  - rive (primary) OU lottiefiles (primary)
  - motion-framer (secondary)
  - accessibility-a11y (required)
```

**Pass Criteria:**
- intent_type == 'microinteraction'
- rive OU lottiefiles estao presentes
- accessibility-a11y e required

---

## Metricas de Qualidade

| Metrica | Target | Como Medir |
|---------|--------|------------|
| Intent Accuracy | > 95% | Testes com inputs variados |
| Skill Relevance | > 90% | Revisao manual das skills selecionadas |
| Asset Detection | 100% | Verificar se todos assets faltantes sao identificados |
| Response Time | < 500ms | Benchmark de execucao |
| User Clarity | > 4.5/5 | Feedback de usuarios sobre next_action |

## Regression Tests

Sempre testar apos mudancas:

1. Hero scroll com assets fornecidos
2. Hero scroll sem assets
3. Landing page completa
4. Hero 3D com modelos
5. Hero 3D sem modelos
6. Microinteracoes
7. Site completo

## Fixtures

Armazenar em `evals/fixtures/`:

- `hero_scroll_input.yaml`
- `hero_scroll_expected.yaml`
- `landing_input.yaml`
- `landing_expected.yaml`
- `hero_3d_input.yaml`
- `hero_3d_expected.yaml`
