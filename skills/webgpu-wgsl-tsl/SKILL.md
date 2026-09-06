---
name: webgpu-wgsl-tsl
description: WebGPU + WGSL + TSL (Three Shading Language)
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - webgpu
    - wgsl
    - tsl
    - three shading language
    - compute shader
  routes:
    - spatial
depends_on:
  - cerebro-orquestrador
  - webgpu-gpgpu
  - r3f-threejs-drei
outputs:
  - webgpu_plan
  - wgsl_shaders
  - tsl_nodes
  - integration_code
---

# WebGPU WGSL TSL

## Stack

- WebGPU API nativa
- Three.js WebGPU renderer
- TSL (Three Shading Language)
- WGSL shaders

## Enxame de Agentes

1. **Compute Architect** - Planeja computacao GPU
2. **WGSL Engineer** - Escreve shaders WGSL
3. **TSL Designer** - Configura nodes TSL
4. **Integration Engineer** - Gera codigo Three.js

## WGSL Compute Shader

```wgsl
// compute.wgsl
struct Params {
  deltaTime: f32,
  time: f32,
  particleCount: u32,
}

@group(0) @binding(0) var<storage, read_write> positions: array<vec3<f32>>;
@group(0) @binding(1) var<storage, read_write> velocities: array<vec3<f32>>;
@group(0) @binding(2) var<uniform> params: Params;

@compute @workgroup_size(64)
fn main(@builtin(global_invocation_id) id: vec3<u32>) {
  let idx = id.x;
  if (idx >= params.particleCount) { return; }
  
  var pos = positions[idx];
  var vel = velocities[idx];
  
  // Gravidade
  vel.y += -9.8 * params.deltaTime;
  pos += vel * params.deltaTime;
  
  // Bounce
  if (pos.y < 0.0) {
    pos.y = 0.0;
    vel.y *= -0.5;
  }
  
  positions[idx] = pos;
  velocities[idx] = vel;
}
```

## TSL (Three Shading Language)

```ts
import { 
  color, 
  float, 
  vec3, 
  timerLocal, 
  positionLocal, 
  uv,
  sin,
  cos,
} from 'three/tsl'

// Node de cor dinamica
const time = timerLocal(0.1)
const colorNode = vec3(
  sin(time.add(positionLocal.x)),
  cos(time.add(positionLocal.y)),
  sin(time.add(positionLocal.z)),
)

// Aplicar ao material
material.colorNode = colorNode
```

## Three.js WebGPU Renderer

```ts
import * as THREE from 'three'
import { WebGPURenderer } from 'three/webgpu'

const renderer = new WebGPURenderer({ antialias: true })
renderer.setPixelRatio(Math.min(2, window.devicePixelRatio))
renderer.setSize(window.innerWidth, window.innerHeight)
document.body.appendChild(renderer.domElement)

const scene = new THREE.Scene()
const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000)
camera.position.z = 5

// Geometria com TSL
const geometry = new THREE.PlaneGeometry(2, 2)
const material = new THREE.MeshBasicNodeMaterial({
  colorNode: vec3(sin(timerLocal(0.1)), cos(timerLocal(0.1)), 0.5),
})

const mesh = new THREE.Mesh(geometry, material)
scene.add(mesh)

function animate() {
  requestAnimationFrame(animate)
  renderer.render(scene, camera)
}
animate()
```

## Output

```yaml
webgpu_plan:
  renderer: WebGPURenderer
  compute_shader: WGSL
  tsl_nodes: [timerLocal, sin, cos, positionLocal]
  particle_count: 50000
  workgroup_size: 64
  fallback: webgl2
  integration: threejs
```
