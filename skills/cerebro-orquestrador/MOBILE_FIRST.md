# Mobile-First & Responsive Engine

**Status:** Obrigatorio  
**Aplicacao:** TODA solicitacao, TODA skill, TODO projeto  
**Regra:** Nenhuma entrega esta completa se nao funcionar perfeitamente em desktop E mobile.

---

## Principio Fundamental

> Desktop e mobile sao experiencias diferentes, nao apenas tamanhos diferentes. O Brain deve projetar, implementar e validar ambas autonomamente.

**Errado:**
```
Criar site desktop e depois "tentar" adaptar para mobile.
```

**Correto:**
```
1. Projetar mobile-first
2. Construir base responsiva
3. Escalar para tablet
4. Expandir para desktop
5. Adaptar 3D/motion para capacidade do dispositivo
6. Validar em todos os breakpoints
```

---

## Breakpoints Obrigatorios

```yaml
breakpoints:
  mobile_small:
    width: 320-374px
    target: iPhone SE, Android pequenos
    priority: critica

  mobile:
    width: 375-767px
    target: iPhone, Android
    priority: critica

  tablet:
    width: 768-1023px
    target: iPad, tablets Android
    priority: alta

  desktop:
    width: 1024-1439px
    target: Laptops, monitores
    priority: alta

  desktop_large:
    width: 1440px+
    target: Monitores grandes
    priority: media
```

---

## Pipeline Mobile-First

```
┌────────────────────────────────────────────────────────────────────┐
│  1. ANALISAR CAPACIDADE DO DISPOSITIVO                              │
│  - Viewport width/height                                            │
│  - Touch vs mouse                                                   │
│  - GPU/WebGL/WebGPU support                                         │
│  - prefers-reduced-motion                                           │
│  - Network speed (quando disponivel)                                │
│  - Device memory (quando disponivel)                                │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  2. CRIAR BASE MOBILE-FIRST                                        │
│  - Conteudo essencial visivel                                       │
│  - HTML semantico                                                   │
│  - Touch targets >= 44x44px                                         │
│  - Font size >= 16px                                                │
│  - Sem hover-only interactions                                      │
│  - Imagens responsivas                                              │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  3. ADICIONAR ENHANCEMENTS POR BREAKPOINT                          │
│  - Tablet: grid expandido, motion moderado                          │
│  - Desktop: parallax, hover, layouts amplos                         │
│  - Desktop high-end: 3D completo, particulas, shaders              │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  4. ADAPTAR MOTION E 3D                                            │
│  - Mobile: motion leve, 3D simplificado ou static fallback          │
│  - Tablet: qualidade media, interacao touch                         │
│  - Desktop: experiencia completa, mouse interactions                │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  5. VALIDAR TODOS OS BREAKPOINTS                                   │
│  - 320px, 375px, 768px, 1024px, 1440px                             │
│  - Portrait + landscape                                             │
│  - Touch + mouse                                                    │
│  - Reduced motion + full motion                                     │
└────────────────────────────────────────────────────────────────────┘
```

---

## Regras de Layout

### Mobile-First CSS

```css
/* Base: Mobile (320px+) */
.hero {
  min-height: 100svh;
  padding: 24px 16px;
  display: grid;
  gap: 24px;
}

.hero__title {
  font-size: clamp(2rem, 10vw, 4rem);
  line-height: 0.95;
}

/* Tablet (768px+) */
@media (min-width: 768px) {
  .hero {
    padding: 48px 32px;
    grid-template-columns: 1fr 1fr;
    align-items: center;
  }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
  .hero {
    min-height: 100vh;
    padding: 80px clamp(32px, 8vw, 160px);
  }
}
```

### Tipografia Fluida

```css
:root {
  --step--1: clamp(0.875rem, 0.83rem + 0.22vw, 1rem);
  --step-0: clamp(1rem, 0.91rem + 0.43vw, 1.25rem);
  --step-1: clamp(1.25rem, 1.07rem + 0.87vw, 1.75rem);
  --step-2: clamp(1.563rem, 1.23rem + 1.63vw, 2.5rem);
  --step-3: clamp(1.953rem, 1.37rem + 2.91vw, 3.625rem);
  --step-4: clamp(2.441rem, 1.43rem + 5.05vw, 5.344rem);
}
```

### Imagens Responsivas

```tsx
<picture>
  <source
    media="(max-width: 767px)"
    srcSet="/hero-mobile.avif"
    type="image/avif"
  />
  <source
    media="(max-width: 1023px)"
    srcSet="/hero-tablet.avif"
    type="image/avif"
  />
  <img
    src="/hero-desktop.avif"
    alt="Descricao da imagem"
    width="1920"
    height="1080"
    loading="eager"
    fetchPriority="high"
  />
</picture>
```

---

## Adaptacao de Motion

### Desktop: Experiencia Completa

```yaml
desktop:
  scroll:
    smooth: lenis
    effects: [parallax, pin, scrub, horizontal-scroll]
  animation:
    duration: normal
    complexity: high
  3d:
    quality: high
    particles: 10000
    shadows: true
    postprocessing: true
  interaction:
    input: mouse + keyboard
    hover: enabled
```

### Mobile: Experiencia Otimizada

```yaml
mobile:
  scroll:
    smooth: native_or_lenis_light
    effects: [simple-reveal]
    disable: [horizontal-scroll, heavy-parallax, long-pin]
  animation:
    duration: reduced
    complexity: low
  3d:
    quality: low_or_static_fallback
    particles: 500-2000
    shadows: false
    postprocessing: false
  interaction:
    input: touch + keyboard
    hover: never_required
    targets: minimum_44px
```

### Implementacao com Device Detection

```tsx
const isMobile = window.matchMedia('(max-width: 767px)').matches;
const prefersReducedMotion = window.matchMedia(
  '(prefers-reduced-motion: reduce)'
).matches;
const hasWebGL = !!document.createElement('canvas').getContext('webgl2');

const quality = isMobile ? 'low' : 'high';
const particleCount = isMobile ? 1000 : 10000;
const enableParallax = !isMobile && !prefersReducedMotion;
const enable3D = hasWebGL && !prefersReducedMotion;

if (prefersReducedMotion) {
  // Mostrar conteudo sem animacao
} else if (isMobile) {
  // Usar motion leve e fallback 3D
} else {
  // Usar experiencia cinematica completa
}
```

---

## Adaptacao de 3D

### Quality Tiers

```yaml
quality_tiers:
  tier_0_no_webgl:
    condition: WebGL indisponivel
    output: imagem ou video estatico
    particles: 0
    shaders: false

  tier_1_mobile_low:
    condition: mobile ou deviceMemory < 4GB
    output: 3D simplificado
    particles: 500-2000
    dpr: 1
    shadows: false
    postprocessing: false
    textures: compressed

  tier_2_tablet_medium:
    condition: tablet ou deviceMemory 4-8GB
    output: 3D medio
    particles: 2000-5000
    dpr: 1-1.5
    shadows: basic
    postprocessing: limited

  tier_3_desktop_high:
    condition: desktop + GPU adequada
    output: 3D completo
    particles: 5000-15000
    dpr: 1-2
    shadows: true
    postprocessing: enabled
```

### R3F Responsivo

```tsx
import { Canvas } from '@react-three/fiber';
import { useDetectGPU, AdaptiveDpr, AdaptiveEvents } from '@react-three/drei';

function ResponsiveScene() {
  const gpu = useDetectGPU();
  const isMobile = useMediaQuery('(max-width: 767px)');
  const tier = gpu.tier;

  if (tier < 1) {
    return <img src="/scene-fallback.avif" alt="Descricao da cena" />;
  }

  return (
    <Canvas
      dpr={isMobile ? 1 : [1, 2]}
      gl={{ antialias: !isMobile, powerPreference: 'high-performance' }}
      camera={{ position: [0, 0, isMobile ? 8 : 5], fov: isMobile ? 55 : 45 }}
    >
      <AdaptiveDpr pixelated />
      <AdaptiveEvents />
      <Scene particleCount={isMobile ? 1000 : 10000} />
    </Canvas>
  );
}
```

---

## Touch e Interacao

### Regras Obrigatorias

```yaml
touch_requirements:
  minimum_target_size: 44x44px
  minimum_spacing: 8px
  no_hover_only_features: true
  support_swipe: quando aplicavel
  support_pinch_zoom: nao bloquear sem motivo
  prevent_accidental_tap: true
  keyboard_accessible: true
```

### CSS para Touch

```css
/* Touch targets */
button,
a,
input,
select,
textarea,
[role="button"] {
  min-width: 44px;
  min-height: 44px;
}

/* Remover delay de toque */
button,
a {
  touch-action: manipulation;
}

/* Hover apenas em dispositivos que suportam hover */
@media (hover: hover) and (pointer: fine) {
  .card:hover {
    transform: translateY(-4px);
  }
}

/* Touch feedback */
@media (hover: none) and (pointer: coarse) {
  .card:active {
    transform: scale(0.98);
  }
}
```

---

## Validacao Obrigatoria

### Matriz de Teste

```yaml
test_matrix:
  viewports:
    - 320x568: iPhone SE
    - 375x667: iPhone padrão
    - 390x844: iPhone moderno
    - 768x1024: iPad portrait
    - 1024x768: iPad landscape
    - 1280x720: Laptop
    - 1440x900: Desktop
    - 1920x1080: Desktop large

  capabilities:
    - touch_only
    - mouse_keyboard
    - prefers_reduced_motion
    - no_webgl
    - slow_network
    - low_memory

  checks:
    - no_horizontal_overflow
    - all_content_visible
    - touch_targets_44px
    - keyboard_navigation
    - readable_typography
    - images_responsive
    - 3d_fallback_works
    - motion_adapts
    - fps_target_met
```

### Quality Gate Mobile/Desktop

```yaml
responsive_quality_gate:
  mobile:
    lighthouse_performance: '>= 80'
    lighthouse_accessibility: '>= 90'
    lcp: '< 2.5s'
    cls: '< 0.1'
    touch_targets: '>= 44px'
    horizontal_overflow: false
    3d_fallback: required

  desktop:
    lighthouse_performance: '>= 90'
    lighthouse_accessibility: '>= 90'
    fps: '>= 60'
    frame_time_p95: '< 16ms'
    keyboard_navigation: pass
    3d_quality: adaptive
```

---

## Contrato de Entrega Responsiva

Toda entrega do Brain deve incluir:

```yaml
responsive_delivery:
  required:
    - mobile_first_layout
    - tablet_layout
    - desktop_layout
    - touch_interactions
    - keyboard_interactions
    - responsive_images
    - adaptive_3d_quality
    - reduced_motion_mode
    - no_webgl_fallback
    - mobile_performance_report
    - desktop_performance_report
    - screenshots_mobile
    - screenshots_desktop

  forbidden:
    - desktop_only_design
    - hover_only_interactions
    - fixed_width_layouts
    - unoptimized_mobile_3d
    - blocking_pinch_zoom
    - missing_reduced_motion
```

---

## Exemplo: Site Cinematico 3D

**Usuario:**
```
"Quero um site cinematografico com 3D para minha marca"
```

**Brain decide automaticamente:**

```yaml
mobile_implementation:
  layout: single_column
  navigation: hamburger_menu
  typography: fluid_clamp
  scroll: native_or_light_lenis
  animations: simple_fade_reveals
  parallax: disabled_or_subtle
  3d: low_poly_or_static_image
  particles: 1000
  video: poster_then_lazy_load
  images: avif_webp_responsive
  touch: swipe_and_tap
  target_performance: lighthouse_80_plus

desktop_implementation:
  layout: cinematic_full_viewport
  navigation: expanded
  typography: fluid_clamp
  scroll: lenis_plus_scrolltrigger
  animations: pinned_sections_parallax_scrub
  parallax: multilayer
  3d: high_quality_r3f
  particles: 10000
  shaders: enabled
  interactions: mouse_parallax_hover
  target_performance: lighthouse_90_plus_fps_60

fallback_implementation:
  reduced_motion: static_content_no_scroll_animation
  no_webgl: optimized_hero_image_or_video
  low_end_device: reduced_particles_and_dpr
  no_javascript: semantic_html_all_content_visible
```

---

**FIM DO MOBILE-FIRST ENGINE**
