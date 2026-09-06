---
name: webgpu-gpgpu
description: WebGPU + GPGPU + compute shaders para particulas e simulacoes
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - webgpu
    - gpgpu
    - compute shader
    - particulas
    - simulacao
  routes:
    - spatial
    - performance
depends_on:
  - cerebro-orquestrador
  - r3f-threejs-drei
outputs:
  - gpgpu_plan
  - compute_shader
  - webgl2_fallback
  - performance_report
---

# WebGPU GPGPU

## Stack

- WebGPU API nativa
- Three.js WebGPU renderer (quando disponivel)
- GPUComputationRenderer para WebGL2 fallback
- Fallback Canvas 2D ou CSS

## Enxame de Agentes

1. **Compute Architect** - Planeja computacao GPU e estrutura de dados
2. **Shader Engineer** - Escreve compute shaders WGSL/GLSL
3. **Fallback Engineer** - Cria versao WebGL2/Canvas
4. **Performance Reviewer** - Verifica memory, FPS, workgroup
5. **Capability Probe** - Detecta WebGPU suporte e fallback

## Processo Obrigatorio

1. Probe WebGPU capability
2. Defina estrutura de dados (positions, velocities, attributes)
3. Escreva compute shader WGSL
4. Implemente fallback WebGL2 com GPUComputationRenderer
5. Implemente fallback Canvas 2D para mobile fraco
6. Teste memory budget e FPS
7. Entregue performance_report.yaml

## Capability Probe

```ts
async function probeWebGPU(): Promise<{ available: boolean; reason?: string }> {
  if (!navigator.gpu) return { available: false, reason: 'no_navigator_gpu' }
  try {
    const adapter = await navigator.gpu.requestAdapter()
    if (!adapter) return { available: false, reason: 'no_adapter' }
    return { available: true }
  } catch (e) {
    return { available: false, reason: 'request_failed' }
  }
}
```

## Renderer Ladder

| Tier | Tecnologia | Caso de Uso |
|------|------------|-------------|
| A | CSS transforms | < 100 elementos |
| B | Canvas 2D | 100-1000 particulas |
| C | WebGL2 + GPUComputation | 1k-50k particulas |
| D | WebGPU + compute | 50k-500k particulas |

## Performance Budget

- Memory: 64MB max mobile, 256MB desktop
- FPS: 60 target, 30 minimo aceitavel
- Workgroup: 64 ou 128 threads
- Draw calls: < 100 mobile, < 300 desktop

## Contratos

Ver INPUT_CONTRACT.yaml e OUTPUT_CONTRACT.yaml para schema.
