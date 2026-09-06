---
name: cerebro-implementation
version: 1.0.0
---

# Cerebro - Implementacao de Referencia

## Pseudocodigo do Orquestrador

```typescript
interface CerebroOrchestrator {
  // Passo 0: Carregamento automatico
  loadAllSkills(): Promise<SkillManifest[]>
  
  // Passo 1: Classificar intencao
  classifyIntent(request: UserRequest): IntentClassification
  
  // Passo 2: Selecionar skills
  selectSkills(intent: IntentClassification): SelectedSkill[]
  
  // Passo 3: Verificar assets
  checkAssets(request: UserRequest): AssetGateReport
  
  // Passo 4: Criar plano
  createPlan(intent: IntentClassification, skills: SelectedSkill[]): ExecutionPlan
  
  // Passo 5: Executar
  execute(plan: ExecutionPlan): Promise<ExecutionResult>
  
  // Passo 6: Quality Gate
  qualityGate(result: ExecutionResult): QualityReport
  
  // Passo 7: Snapshot
  createSnapshot(result: ExecutionResult, quality: QualityReport): RunSnapshot
}
```

## Implementacao Classificacao

```typescript
function classifyIntent(request: UserRequest): IntentClassification {
  const keywords = request.user_request.toLowerCase()
  
  if (keywords.includes('hero') && keywords.includes('scroll')) {
    return {
      intent_type: 'hero_scroll',
      surface: 'hero',
      narrative: buildHeroScrollNarrative(request)
    }
  }
  
  if (keywords.includes('landing') || keywords.includes('saas')) {
    return {
      intent_type: 'landing',
      surface: 'page',
      narrative: buildLandingNarrative(request)
    }
  }
  
  if (keywords.includes('3d') || keywords.includes('three') || keywords.includes('particulas')) {
    return {
      intent_type: 'hero_3d',
      surface: 'hero',
      narrative: build3DNarrative(request)
    }
  }
  
  // ... outros patterns
  
  return {
    intent_type: 'site_completo',
    surface: 'site_completo',
    narrative: buildFullSiteNarrative(request)
  }
}
```

## Implementacao Selecao de Skills

```typescript
function selectSkills(intent: IntentClassification): SelectedSkill[] {
  const skillMap: Record<string, SelectedSkill[]> = {
    hero_scroll: [
      { name: 'gsap-scrolltrigger', type: 'primary', weight: 1.0 },
      { name: 'lenis', type: 'primary', weight: 1.0 },
      { name: 'accessibility-a11y', type: 'secondary', weight: 0.8 },
      { name: 'performance-budget', type: 'secondary', weight: 0.8 },
    ],
    landing: [
      { name: 'gsap-scrolltrigger', type: 'primary', weight: 1.0 },
      { name: 'lenis', type: 'primary', weight: 1.0 },
      { name: 'motion-framer', type: 'secondary', weight: 0.8 },
      { name: 'accessibility-a11y', type: 'required', weight: 1.0 },
      { name: 'performance-budget', type: 'required', weight: 1.0 },
    ],
    hero_3d: [
      { name: 'r3f-threejs-drei', type: 'primary', weight: 1.0 },
      { name: 'webgpu-gpgpu', type: 'primary', weight: 1.0 },
      { name: 'lygia', type: 'secondary', weight: 0.8 },
      { name: 'performance-budget', type: 'required', weight: 1.0 },
      { name: 'accessibility-a11y', type: 'required', weight: 1.0 },
    ],
  }
  
  return skillMap[intent.intent_type] || []
}
```

## Implementacao Asset Gate

```typescript
function checkAssets(request: UserRequest): AssetGateReport {
  const missing: BlockingAsset[] = []
  
  if (!request.assets_provided.logo) {
    missing.push({
      type: 'logo',
      status: 'missing',
      required_for: 'final_delivery',
      instructions: 'Enviar logo em SVG ou PNG (min 500x500, fundo transparente)'
    })
  }
  
  if (!request.assets_provided.images || request.assets_provided.images.length === 0) {
    missing.push({
      type: 'images',
      status: 'missing',
      required_for: 'final_delivery',
      count: 3,
      instructions: generateImageInstructions(request.context)
    })
  }
  
  return {
    asset_state: missing.length > 0 ? 'pending' : 'provided',
    delivery_state: missing.length > 0 ? 'prototype' : 'final',
    blocking_assets: missing,
    asset_instructions: generateAssetInstructions(missing)
  }
}
```

## Exemplo de Uso

```typescript
// IDE carrega automaticamente
const allSkills = await loadAllSkills()

// Usuario faz pedido
const request: UserRequest = {
  user_request: 'Quero um hero com scroll que revela produtos',
  context: {
    project_name: 'Minha Landing',
    brand_name: 'Minha Marca',
    industry: 'tech'
  },
  constraints: {
    performance_budget_ms: 16,
    a11y_target: 'AA'
  }
}

// Cerebro processa
const intent = classifyIntent(request)
const skills = selectSkills(intent)
const assets = checkAssets(request)
const plan = createPlan(intent, skills)
const result = await execute(plan)
const quality = qualityGate(result)
const snapshot = createSnapshot(result, quality)

// Retorna para usuario
return {
  intent_classification: intent,
  selected_skills: skills,
  execution_plan: plan,
  asset_gate_report: assets,
  quality_state: quality,
  delivery_state: assets.delivery_state,
  next_action: generateNextAction(assets),
  run_snapshot: snapshot
}
```
