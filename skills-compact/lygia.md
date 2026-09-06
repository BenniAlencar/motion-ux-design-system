# lygia

**Skill compactada — conteudo completo**
Fonte: `skills/lygia/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Lygia

## Manifesto

Shaders GLSL modulares e reutilizaveis para efeitos visuais em tempo real no navegador.

## Stack

- lygia (npm)
- WebGL/WebGPU
- GLSL shaders

## Keywords

lygia, glsl, shader, visual-effects, modular, reusable, gpu

## Visao Geral

Lygia permite:
1. Shaders GLSL modulares
2. Efeitos visuais reutilizaveis
3. Composicao de shaders
4. Performance GPU

## Como Usar

```glsl
// Importar modulo Lygia
#include "lygia/math/random.glsl"
#include "lygia/color/palette.glsl"

void main() {
  vec2 uv = gl_FragCoord.xy / resolution;
  vec3 color = palette(random(uv) * 10.0);
  gl_FragColor = vec4(color, 1.0);
}
```

## Composicao

```glsl
#include "lygia/filter/blur.glsl"
#include "lygia/filter/noise.glsl"

void main() {
  vec4 color = texture(uTexture, uv);
  color = blur(color, 0.5);
  color = noise(color, 0.1);
  gl_FragColor = color;
}
```

## Metricas de Sucesso

- Shaders compilando corretamente
- Efeitos visuais funcionando
- Performance GPU otimizada
- Modularidade reutilizavel

