---
name: lygia
description: Lygia GLSL shader library para SDF, noise, palette e efeitos
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - lygia
    - shader
    - glsl
    - sdf
    - noise
    - palette
  routes:
    - spatial
depends_on:
  - cerebro-orquestrador
  - r3f-threejs-drei
outputs:
  - shader_code
  - lygia_imports
  - fallback_css
  - performance_report
---

# Lygia Shaders

## Stack

- Lygia GLSL library (https://lygia.xyz)
- Three.js shaderMaterial
- R3F shaderMaterial hook
- Fallback CSS/Canvas

## Enxame de Agentes

1. **Shader Architect** - Seleciona funcoes Lygia adequadas
2. **GLSL Engineer** - Escreve shaders com imports Lygia
3. **Integration Engineer** - Integra com Three.js/R3F
4. **Fallback Designer** - Cria versao CSS/Canvas
5. **Performance Reviewer** - Verifica GPU load mobile

## Lygia Imports Comuns

```glsl
// SDF (Signed Distance Functions)
#include "lygia/sdf/circleSDF.glsl"
#include "lygia/sdf/boxSDF.glsl"
#include "lygia/sdf/roundedBoxSDF.glsl"

// Generative
#include "lygia/generative/fbm.glsl"
#include "lygia/generative/cnoise.glsl"
#include "lygia/generative/truchet.glsl"

// Color
#include "lygia/color/palette.glsl"
#include "lygia/color/grade.glsl"

// Math
#include "lygia/math/saturate.glsl"
#include "lygia/math/fract.glsl"
```

## Processo Obrigatorio

1. Selecionar funcoes Lygia necessarias
2. Escrever fragment shader com imports
3. Integrar com Three.js/R3F
4. Criar fallback CSS para browsers sem WebGL
5. Testar em mobile GPU limitada
6. Entregue performance_report

## Contratos

Ver INPUT_CONTRACT.yaml e OUTPUT_CONTRACT.yaml.
