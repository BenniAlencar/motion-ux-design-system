# Autonomous Engine — Cérebro Orquestrador

**Status:** Obrigatorio  
**Modo:** Autonomo  
**Regra:** O usuario descreve o RESULTADO desejado. O Brain decide AUTOMATICAMENTE quais skills, agents, patterns e tecnicas ativar.

---

## Principio Fundamental

> O usuario NUNCA precisa pedir uma tecnologia, biblioteca ou efeito especifico. Ele descreve o que quer criar. O Brain analisa a intencao e ativa TODAS as skills necessarias autonomamente.

**Errado (modo chatbot):**
```
Usuario: "Use GSAP e Three.js para criar um site"
Sistema: "Aqui esta um exemplo com GSAP e Three.js"
```

**Correto (modo autonomo):**
```
Usuario: "Quero um site com scrolling cinematico e 3D"
Brain: [analisa intencao]
Brain: [ativa automaticamente: gsap-scrolltrigger, lenis, r3f-threejs-drei,
        webgpu-gpgpu, lygia, accessibility-a11y, performance-budget,
        asset-gate, quality-gate]
Brain: [seleciona patterns: parallax, pinned sections, scroll-reveal,
        3D particles, shader effects, smooth scrolling]
Brain: [delega agents: Architect, 3D, Animation, Asset, Quality, Evidence]
Brain: [entrega solucao completa]
```

---

## Pipeline Autonomo Obrigatorio

```
┌──────────────────────────────────────────────────────────────────────┐
│  INPUT NATURAL DO USUARIO                                             │
│  "Quero um site com scrolling cinematico e 3D"                        │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│  1. BRAIN ANALISA INTENCAO                                            │
│     - Detecta: site completo + cinematic scrolling + 3D               │
│     - Extrai: experiencia imersiva, movimento, profundidade           │
│     - Nao pergunta quais tecnologias usar                             │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│  2. BRAIN CONSULTA TODAS AS 28 SKILLS                                 │
│     - Le skills-compact/*.md                                          │
│     - Le agentes-training/*.txt                                       │
│     - Mapeia keywords, patterns e dependencias                        │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│  3. BRAIN ATIVA SKILLS RELEVANTES AUTOMATICAMENTE                     │
│     Primary: r3f-threejs-drei                                         │
│     Motion: gsap-scrolltrigger + lenis + scrollsmoother               │
│     Visual: lygia + webgpu-gpgpu + theatrejs                          │
│     Required: accessibility-a11y + performance-budget                 │
│     Gate: asset-gate + quality-gate                                   │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│  4. BRAIN SELECIONA PATTERNS                                          │
│     - Smooth scroll inercial                                          │
│     - Pinned sections cinematicas                                     │
│     - Parallax multicamada                                            │
│     - 3D scene interativa                                              │
│     - Particulas GPU                                                   │
│     - Shaders e transicoes                                             │
│     - Reduced motion fallback                                         │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│  5. BRAIN DELEGA AGENTS                                               │
│     - ArchitectAgent: arquitetura e stack                             │
│     - 3DAgent: cena Three.js/R3F                                      │
│     - AnimationAgent: GSAP/scroll/parallax                            │
│     - ShaderAgent: Lygia/WebGPU                                       │
│     - AssetAgent: requisitos de assets                                │
│     - A11yAgent: acessibilidade                                       │
│     - PerfAgent: budget e otimizacao                                  │
│     - QualityAgent: validacao                                         │
│     - EvidenceAgent: metricas e demonstracao                          │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│  6. BRAIN ENTREGA RESULTADO                                           │
│     - Projeto completo                                                │
│     - Codigo pronto para rodar                                        │
│     - Instrucoes de assets                                            │
│     - Quality report                                                  │
│     - Evidence packet                                                 │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Matriz de Ativacao Autonoma

### Intencao: Site Cinematico com Scroll e 3D

**Input do usuario:**
```
"Quero um site com scrolling cinematico e 3D"
```

**Skills ativadas automaticamente:**

```yaml
intent: cinematic_3d_website
confidence_target: 0.95

primary_skills:
  - r3f-threejs-drei: Cena 3D, geometria, camera, lights
  - gsap-scrolltrigger: Animacoes sincronizadas com scroll
  - lenis: Smooth scroll inercial

motion_skills:
  - scrollsmoother: Smooth scroll avancado e efeitos
  - observer: Reveals por viewport
  - flip: Transicoes de layout
  - motion-framer: Microinteracoes de UI

visual_skills:
  - lygia: Shaders GLSL modulares
  - webgpu-gpgpu: Particulas e simulacoes GPU
  - webgpu-wgsl-tsl: Shaders WebGPU
  - theatrejs: Timelines cinematicas

optional_skills:
  - spline-runtime: Quando houver cena Spline
  - rive: Quando houver elementos de UI stateful
  - lottiefiles: Quando houver icones/animacoes vetoriais
  - tonejs: Quando houver audio interativo

required_skills:
  - accessibility-a11y: WCAG AA, teclado, reduced motion
  - performance-budget: FPS, bundle, Web Vitals
  - asset-gate: Assets corretos
  - quality-gate: Validacao final
```

**Patterns selecionados automaticamente:**

```yaml
scroll_patterns:
  - lenis_smooth_scroll
  - scrolltrigger_scrub
  - pinned_cinematic_sections
  - multilayer_parallax
  - horizontal_scroll_gallery
  - staggered_reveals

three_d_patterns:
  - r3f_canvas_with_fallback
  - scroll_driven_camera
  - cursor_reactive_objects
  - instanced_particles
  - shader_material_effects
  - adaptive_quality_tiers

accessibility_patterns:
  - prefers_reduced_motion
  - keyboard_navigation
  - semantic_fallback_content
  - canvas_aria_description
  - skip_link

performance_patterns:
  - lazy_load_3d_assets
  - dynamic_import_heavy_components
  - adaptive_dpr
  - frame_time_monitoring
  - webgl_context_loss_recovery
```

---

## Intencoes e Ativacoes

### Landing Page Premium

**Input:** "Quero uma landing page premium para meu SaaS"

```yaml
primary:
  - gsap-scrolltrigger
  - lenis
  - motion-framer
secondary:
  - flip
  - observer
  - lottiefiles
required:
  - accessibility-a11y
  - performance-budget
  - asset-gate
  - quality-gate
patterns:
  - hero_reveal
  - section_reveals
  - product_showcase
  - social_proof
  - magnetic_cta
  - reduced_motion
```

### Experiencia 3D Interativa

**Input:** "Quero uma experiencia 3D interativa"

```yaml
primary:
  - r3f-threejs-drei
  - webgpu-gpgpu
  - lygia
secondary:
  - rapier
  - theatrejs
  - tonejs
  - spline-runtime
required:
  - accessibility-a11y
  - performance-budget
  - asset-gate
  - quality-gate
patterns:
  - interactive_camera
  - pointer_reactivity
  - gpu_particles
  - physics_objects
  - shader_effects
  - low_end_fallback
```

### Site Editorial com Motion

**Input:** "Quero um site editorial com muito motion"

```yaml
primary:
  - gsap-scrolltrigger
  - lenis
  - motion-framer
secondary:
  - scrollsmoother
  - flip
  - observer
  - animejs
required:
  - accessibility-a11y
  - performance-budget
  - quality-gate
patterns:
  - typography_reveals
  - image_parallax
  - editorial_grid
  - page_transitions
  - progressive_enhancement
```

### Arte Generativa

**Input:** "Quero arte generativa interativa"

```yaml
primary:
  - p5js
  - webgpu-gpgpu
  - lygia
secondary:
  - ogl
  - pixi
  - tonejs
  - rapier
required:
  - performance-budget
  - accessibility-a11y
  - quality-gate
patterns:
  - generative_canvas
  - pointer_input
  - audio_reactive
  - gpu_simulation
  - export_controls
```

### Transicoes de Pagina

**Input:** "Quero transicoes suaves entre paginas"

```yaml
primary:
  - barba
  - swup
  - gsap-scrolltrigger
secondary:
  - flip
  - motion-framer
  - lenis
required:
  - accessibility-a11y
  - performance-budget
  - quality-gate
patterns:
  - route_transition
  - shared_element_transition
  - page_exit_enter
  - scroll_restoration
  - focus_management
```

---

## Regras de Decisao Autonoma

### Regra 1: Resultado, nao Tecnologia

```yaml
user_says: "Quero uma experiencia imersiva"
brain_decides:
  - Se 3D: r3f-threejs-drei + lygia + webgpu-gpgpu
  - Se scroll: gsap-scrolltrigger + lenis
  - Se audio: tonejs
  - Sempre: accessibility + performance + quality
```

### Regra 2: Ativacao Proativa

O Brain deve ativar skills adicionais quando detectar oportunidade:

```yaml
detected: "scrolling cinematico"
auto_add:
  - gsap-scrolltrigger
  - lenis
  - scrollsmoother
  - lygia (para efeitos visuais)
  - accessibility-a11y
  - performance-budget

detected: "3D"
auto_add:
  - r3f-threejs-drei
  - webgpu-gpgpu
  - lygia
  - performance-budget
  - accessibility-a11y

detected: "premium"
auto_add:
  - motion-framer
  - flip
  - quality-gate
  - asset-gate
```

### Regra 3: Nao Perguntar por Stack

**O Brain NUNCA deve perguntar:**
- "Voce quer usar GSAP ou Framer Motion?"
- "Voce prefere Three.js ou Spline?"
- "Voce quer parallax?"
- "Qual biblioteca de scroll?"

**O Brain DEVE decidir baseado em:**
- Intencao do usuario
- Complexidade do projeto
- Performance budget
- Compatibilidade de dispositivo
- Padroes em `agentes-training/`
- Skills disponiveis

### Regra 4: Progressive Enhancement

```yaml
base_layer:
  - HTML semantico
  - CSS responsivo
  - Conteudo acessivel

enhancement_layer:
  - GSAP animations
  - Lenis smooth scroll
  - R3F 3D
  - WebGPU particles

fallback_layer:
  - reduced-motion: Animacoes minimas
  - no-webgl: Imagem/video fallback
  - low-end-device: Qualidade reduzida
  - no-js: Conteudo essencial visivel
```

### Regra 5: Quality nao e Opcional

Toda entrega deve incluir automaticamente:

```yaml
required_deliverables:
  - codigo_funcional
  - asset_instructions
  - accessibility_check
  - performance_budget
  - quality_report
  - evidence_packet
```

---

## Contrato de Comportamento do Brain

```yaml
brain_behavior:
  mode: autonomous_system
  user_role: describes_outcomes
  brain_role: plans_and_executes_technical_solution

on_every_request:
  - load: all skills-compact/*.md
  - load: relevant agentes-training/*.txt
  - analyze: user intent, desired experience, constraints
  - infer: visual language, interactions, technologies, patterns
  - select: all relevant skills automatically
  - activate: required quality and accessibility skills always
  - plan: implementation architecture
  - execute: specialized agent workflows
  - validate: quality, performance, accessibility
  - deliver: complete project package

never:
  - ask user to select technical libraries
  - require user to name a skill
  - skip accessibility or performance
  - deliver only partial snippets when full project is needed
  - behave as passive chatbot
```

---

## Exemplo Completo

### Usuario diz

```
"Quero um site para uma marca de carros eletricos. Deve ser futurista,
com scroll cinematico, um carro 3D interativo e alta conversao."
```

### Brain executa autonomamente

```yaml
intent_analysis:
  primary_intent: premium_cinematic_3d_landing
  domain: automotive_electric
  desired_feeling: futuristic, immersive, premium
  requirements_inferred:
    - cinematic scroll storytelling
    - interactive 3D product configurator
    - conversion-oriented CTA
    - high-end visual language

skills_activated:
  core:
    - r3f-threejs-drei
    - gsap-scrolltrigger
    - lenis
  visual:
    - lygia
    - webgpu-gpgpu
    - theatrejs
  interaction:
    - motion-framer
    - observer
    - flip
  quality:
    - accessibility-a11y
    - performance-budget
    - asset-gate
    - quality-gate

patterns_selected:
  - scroll_driven_camera_path
  - 3d_car_orbit_controls
  - shader_based_metal_paint
  - gpu_particle_atmosphere
  - pinned_storytelling_sections
  - parallax_landscape_layers
  - magnetic_conversion_cta
  - adaptive_quality_tiers
  - reduced_motion_fallback
  - static_product_image_fallback

agents_delegated:
  - ArchitectAgent
  - ThreeDSceneAgent
  - ScrollAnimationAgent
  - ShaderAgent
  - ConversionUXAgent
  - AssetAgent
  - A11yAgent
  - PerformanceAgent
  - QualityAgent
  - EvidenceAgent

deliverables:
  - Next.js project structure
  - Interactive 3D car scene
  - Cinematic scroll timeline
  - Responsive mobile fallback
  - Asset specifications
  - Lighthouse and A11y evidence
```

---

## Rollback

Se uma escolha automatica falhar:

1. Desativar apenas a skill que falhou
2. Aplicar fallback compativel
3. Manter conteudo acessivel e funcional
4. Registrar a decisao e o fallback
5. Nunca bloquear a entrega por uma melhoria visual opcional

---

**FIM DO AUTONOMOUS ENGINE**
