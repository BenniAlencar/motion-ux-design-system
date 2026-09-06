---
name: webgpu-agents
version: 1.0.0
---

# WebGPU GPGPU - Enxame de Agentes

## 1. Compute Architect

**Responsabilidade:** Planejar estrutura de dados e pipeline GPU.

**Output:**
```yaml
gpgpu_plan:
  particle_count: 50000
  attributes:
    - name: position
      type: vec3<f32>
      size_bytes: 600000  # 50k * 3 * 4
    - name: velocity
      type: vec3<f32>
      size_bytes: 600000
    - name: color
      type: vec4<f32>
      size_bytes: 800000
  total_memory_mb: 2.0
  workgroup_size: 64
  compute_passes:
    - name: update_positions
      entry_point: update_positions
    - name: apply_forces
      entry_point: apply_forces
```

## 2. Shader Engineer

**Responsabilidade:** Escrever compute shaders WGSL.

**Output:**
```wgsl
// compute_shader.wgsl
struct Params {
  deltaTime: f32,
  time: f32,
  particleCount: u32,
}

@group(0) @binding(0) var<storage, read_write> positions: array<vec3<f32>>;
@group(0) @binding(1) var<storage, read_write> velocities: array<vec3<f32>>;
@group(0) @binding(2) var<uniform> params: Params;

@compute @workgroup_size(64)
fn update_positions(@builtin(global_invocation_id) id: vec3<u32>) {
  let idx = id.x;
  if (idx >= params.particleCount) { return; }
  
  var pos = positions[idx];
  var vel = velocities[idx];
  
  // Simulacao simples
  vel.y += -9.8 * params.deltaTime; // gravidade
  pos += vel * params.deltaTime;
  
  // Bounce no chao
  if (pos.y < 0.0) {
    pos.y = 0.0;
    vel.y *= -0.5;
  }
  
  positions[idx] = pos;
  velocities[idx] = vel;
}
```

## 3. Fallback Engineer

**Responsabilidade:** Criar versao WebGL2/Canvas.

**Output:**
```ts
// WebGL2 fallback com GPUComputationRenderer
import { GPUComputationRenderer } from 'three/addons/misc/GPUComputationRenderer.js'

const gpuCompute = new GPUComputationRenderer(256, 256, renderer) // 65536 particulas

const posVar = gpuCompute.addVariable('texturePosition', computeShader, dtPosition)
const velVar = gpuCompute.addVariable('textureVelocity', velocityShader, dtVelocity)

gpuCompute.init()

// No render loop:
gpuCompute.compute()
```

## 4. Performance Reviewer

**Responsabilidade:** Verificar memory, FPS, workgroup.

**Checklist:**
- [ ] Memory total < budget (64MB mobile, 256MB desktop)
- [ ] FPS >= 30 em mobile, >= 60 desktop
- [ ] Workgroup size 64 ou 128
- [ ] Texture format adequado (rgba16float vs rgba32float)
- [ ] Dispose correto de buffers e textures

**Output:**
```yaml
performance_review:
  memory_mb: 2.0
  mobile_fps_estimate: 45
  desktop_fps_estimate: 60
  workgroup_size: 64
  texture_format: rgba16float
  recommendations:
    - "Usar rgba16float para economizar memory"
    - "Reduzir particle_count para 25k em mobile"
```

## 5. Capability Probe

**Responsabilidade:** Detectar suporte WebGPU.

**Output:**
```yaml
capability_probe:
  webgpu_available: false
  webgl2_available: true
  fallback_tier: C  # WebGL2 + GPUComputation
  reason: "no_navigator_gpu"
  browser: "Chrome 120"
  os: "Windows 11"
```
