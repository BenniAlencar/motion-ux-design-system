---
name: curtains
description: Curtains.js para efeitos WebGL em elementos DOM
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - curtains.js
    - curtains
    - webgl dom
    - plane effects
  routes:
    - spatial
depends_on:
  - cerebro-orquestrador
outputs:
  - curtains_config
  - planes_plan
  - integration_code
---

# Curtains.js

## Stack

- curtains
- Shaders custom GLSL

## Enxame de Agentes

1. **Scene Analyst** - Analisa efeitos necessarios
2. **Renderer Configurer** - Configura Curtains
3. **Plane Designer** - Configura planes
4. **Shader Engineer** - Escreve shaders
5. **Integration Engineer** - Gera codigo

## Configuracao Basica

```ts
import { Curtains } from 'curtainsjs'

const curtains = new Curtains({
  container: 'canvas-container',
  pixelRatio: Math.min(2, window.devicePixelRatio),
  watchScroll: true,
})

const plane = curtains.addPlane('plane-element', {
  vertexShaderID: 'plane-vs',
  fragmentShaderID: 'plane-fs',
  uniforms: {
    time: {
      name: 'uTime',
      value: 0,
    },
  },
})

plane.onRender(() => {
  plane.uniforms.time.value++
})
```

## Shaders

```glsl
// Vertex shader
precision mediump float;
attribute vec3 aVertexPosition;
attribute vec2 aTextureCoord;
uniform mat4 uMVMatrix;
uniform mat4 uPMatrix;
varying vec2 vTextureCoord;

void main() {
  vTextureCoord = aTextureCoord;
  gl_Position = uPMatrix * uMVMatrix * vec4(aVertexPosition, 1.0);
}
```

```glsl
// Fragment shader
precision mediump float;
varying vec2 vTextureCoord;
uniform float uTime;

void main() {
  vec2 uv = vTextureCoord;
  uv.x += sin(uv.y * 10.0 + uTime) * 0.01;
  gl_FragColor = vec4(uv, 0.5, 1.0);
}
```

## Output

```yaml
curtains_plan:
  renderer_config:
    pixelRatio: 2
    watchScroll: true
  planes: 3
  shaders: custom
  uniforms: [time, scroll, mouse]
  integration: vanilla
```
