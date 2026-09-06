---
name: ogl
description: OGL para WebGL leve e performatico
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - ogl
    - webgl
    - lightweight webgl
  routes:
    - spatial
depends_on:
  - cerebro-orquestrador
outputs:
  - ogl_config
  - scene_plan
  - integration_code
---

# OGL

## Stack

- ogl
- Shaders custom GLSL

## Enxame de Agentes

1. **Scene Analyst** - Analisa cena 3D necessaria
2. **Renderer Configurer** - Configura WebGL
3. **Shader Engineer** - Escreve shaders
4. **Integration Engineer** - Gera codigo

## Configuracao Basica

```ts
import { Renderer, Camera, Transform, Plane, Program, Texture, Mesh } from 'ogl'

const renderer = new Renderer({ dpr: Math.min(2, window.devicePixelRatio) })
const gl = renderer.gl
document.body.appendChild(gl.canvas)

const camera = new Camera(gl)
camera.position.set(0, 0, 5)

const geometry = new Plane(gl)

const program = new Program(gl, {
  vertex: `attribute vec3 position; void main(){ gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`,
  fragment: `precision highp float; uniform vec3 color; void main(){ gl_FragColor = vec4(color,1.0); }`,
  uniforms: { color: { value: [0.4, 0.6, 1.0] } },
})

const mesh = new Mesh(gl, { geometry, program })

function update() {
  requestAnimationFrame(update)
  mesh.rotation.y -= 0.01
  mesh.rotation.x += 0.01
  renderer.render({ scene: mesh, camera })
}
update()
```

## Textures

```ts
const texture = new Texture(gl, {
  image: new Image(),
  generateMipmaps: false,
})
texture.image.src = '/image.jpg'

program.uniforms.tMap = { value: texture }
```

## Output

```yaml
ogl_plan:
  renderer_config:
    dpr: 2
    antialias: true
  camera:
    fov: 45
    near: 0.1
    far: 100
  geometry: Plane
  shaders: custom
  textures: 1
  integration: vanilla
```
