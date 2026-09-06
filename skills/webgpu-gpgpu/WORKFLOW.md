---
name: webgpu-workflow
version: 1.0.0
---

# WebGPU GPGPU - Workflow

## Passo 1: Capability Probe

```ts
const capability = await probeWebGPU()
// { available: false, reason: 'no_navigator_gpu' }
```

## Passo 2: Selecionar Renderer Tier

```yaml
capability_probe:
  webgpu_available: false
  webgl2_available: true
  selected_tier: C  # WebGL2 + GPUComputation
```

## Passo 3: Compute Architect Plan

```yaml
gpgpu_plan:
  particle_count: 50000
  attributes:
    - position: vec3<f32>
    - velocity: vec3<f32>
    - color: vec4<f32>
  total_memory_mb: 2.0
  workgroup_size: 64
```

## Passo 4: Shader Engineer

Escrever compute shader WGSL (WebGPU) ou GLSL (WebGL2 fallback).

## Passo 5: Fallback Engineer

Implementar WebGL2 com GPUComputationRenderer se WebGPU indisponivel.

## Passo 6: Performance Reviewer

Verificar memory, FPS, workgroup size.

## Passo 7: Entrega

```yaml
run_snapshot:
  trace_id: trace_webgpu_001
  timestamp: 2026-09-05T22:50:00Z
  capability:
    webgpu: false
    webgl2: true
  selected_tier: C
  particle_count: 50000
  memory_mb: 2.0
  fps_estimate:
    mobile: 45
    desktop: 60
  accepted: true
```
