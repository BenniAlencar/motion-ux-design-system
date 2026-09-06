# webgpu-wgsl-tsl

**Skill compactada — conteudo completo**
Fonte: `skills/webgpu-wgsl-tsl/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# WebGPU WGSL/TSL

## Manifesto

Shaders WebGPU usando WGSL (WebGPU Shading Language) e TSL (TypeScript Shading Language) para efeitos visuais avancados.

## Stack

- WebGPU API
- WGSL (nativo)
- TSL (TypeScript-based)

## Keywords

webgpu, wgsl, tsl, shader, gpu, graphics, compute, visual-effects

## Visao Geral

WGSL/TSL permite:
1. Shaders GPU modernos
2. Compute shaders para GPGPU
3. Render pipeline avancado
4. Efeitos visuais complexos

## WGSL Basico

```wgsl
@vertex
fn vs_main(@builtin(vertex_index) vertexIndex: u32) -> @builtin(position) vec4f {
  var positions = array<vec2f, 3>(
    vec2f(-0.5, -0.5),
    vec2f( 0.5, -0.5),
    vec2f( 0.0,  0.5)
  );
  let pos = positions[vertexIndex];
  return vec4f(pos, 0.0, 1.0);
}

@fragment
fn fs_main() -> @location(0) vec4f {
  return vec4f(1.0, 0.0, 0.0, 1.0);
}
```

## TSL Exemplo

```ts
import { tslFn, vec4, float } from 'webgpu-tsl';

const main = tslFn(() => {
  return vec4(float(1), float(0), float(0), float(1));
});

const shader = main.compile();
```

## Metricas de Sucesso

- Shaders compilando
- GPU renderizando
- Compute funcionando
- Cross-browser suportado

