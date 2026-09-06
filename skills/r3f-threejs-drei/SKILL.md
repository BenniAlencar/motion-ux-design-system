---
name: r3f-threejs-drei
description: Three.js + React Three Fiber + Drei + Shaders
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - r3f
    - three.js
    - drei
    - shader
    - 3d
    - webgl
  routes:
    - spatial
    - motion
depends_on:
  - cerebro-orquestrador
  - webgpu-gpgpu
  - lygia
outputs:
  - scene_plan
  - shader_code
  - renderer_ladder
  - fallback_poster
---

# R3F Three.js Drei

## Stack

- Three.js 0.160+
- @react-three/fiber 8+
- @react-three/drei 9+
- Lygia shaders
- WebGPU (com fallback WebGL2)

## Enxame de Agentes

1. **Scene Architect** - Decide se 3D e necessario e qual narrativa
2. **Asset Director** - Confere GLB, HDR, textura, direitos
3. **Renderer Strategist** - Seleciona HTML/CSS, Canvas, WebGL2, WebGPU
4. **R3F Implementer** - Gera codigo da cena e integracao React
5. **GPU Budget Reviewer** - Avalia DPR, geometria, texturas, sombras
6. **Accessibility Reviewer** - Confere reduced motion, poster, descricao

## Renderer Ladder

| Tier | Tecnologia | Uso |
|------|------------|-----|
| A | HTML/CSS/SVG | Fallback sempre disponivel |
| B | Canvas 2D | Generativo leve, particulas 2D |
| C | WebGL2 + Lygia | 3D completo com shaders |
| D | WebGPU + GPGPU | 50k particulas, compute |
| E | Poster + HTML | Foto + descricao poetica |

## Capability Probe

```ts
function probeCapability() {
  return {
    webgpu: !!navigator.gpu,
    webgl2: !!document.createElement('canvas').getContext('webgl2'),
    dpr: Math.min(window.devicePixelRatio, 2),
    memory: navigator.deviceMemory || 4,
    cores: navigator.hardwareConcurrency || 4,
    reducedMotion: matchMedia('(prefers-reduced-motion: reduce)').matches,
  }
}
```

## Codigo Base

```tsx
'use client'
import { Canvas } from '@react-three/fiber'
import { shaderMaterial, PerspectiveCamera } from '@react-three/drei'
import { Suspense } from 'react'

const HeroMaterial = shaderMaterial(
  { uTime: 0, uPointer: [0.5, 0.5] },
  `varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`,
  `
  #include "lygia/sdf/circleSDF.glsl"
  #include "lygia/color/palette.glsl"
  varying vec2 vUv;
  uniform float uTime;
  uniform vec2 uPointer;
  void main(){
    vec2 st = vUv * 2.0 - 1.0;
    float d = circleSDF(st);
    vec3 col = palette(d + uTime * 0.1, vec3(0.5), vec3(0.5), vec3(1.0), vec3(0.0,0.33,0.67));
    gl_FragColor = vec4(col, 1.0 - smoothstep(0.0, 1.0, d));
  }
  `
)

export function Hero3D() {
  return (
    <Canvas dpr={[1, 2]}>
      <PerspectiveCamera makeDefault position={[0, 0, 5]} />
      <Suspense fallback={null}>
        <mesh>
          <planeGeometry args={[2, 2]} />
          <HeroMaterial uTime={performance.now() * 0.001} />
        </mesh>
      </Suspense>
    </Canvas>
  )
}
```
