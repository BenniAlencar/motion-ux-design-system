# webgpu-gpgpu

**Skill compactada — conteudo completo**
Fonte: `skills/webgpu-gpgpu/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# WebGPU + GPGPU

## Manifesto

Computacao GPU massivamente paralela no navegador usando WebGPU para simulacoes de particulas, fisica e efeitos visuais.

## Stack

- WebGPU API (nativo do navegador)
- WGSL (WebGPU Shading Language)
- TypeScript/JavaScript para setup
- Compute shaders para GPGPU

## Keywords

webgpu, gpgpu, compute-shader, wgsl, gpu-compute, particles, physics, simulation, parallel

## Visao Geral

WebGPU GPGPU permite:
1. Simulacoes de milhares de particulas
2. Fisica em tempo real
3. Processamento de imagem GPU-accelerated
4. Computacao cientifica no navegador

## Arquitetura

```
┌─────────────────────────────────────────┐
│            JavaScript/TS                │
│  - Setup WebGPU                         │
│  - Create buffers                       │
│  - Dispatch compute                     │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│            Compute Shader (WGSL)        │
│  - @compute @workgroup_size(64)         │
│  - Processa cada particula              │
│  - Escreve em buffer de saida           │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│            Render Pass                  │
│  - Le buffer de particulas              │
│  - Desenha com instancing               │
│  - Output para tela                     │
└─────────────────────────────────────────┘
```

## Exemplo Basico

```wgsl
@group(0) @binding(0)
var<storage, read_write> positions: array<vec3f>;

@compute @workgroup_size(64)
fn updateParticles(@builtin(global_invocation_id) id: vec3u) {
  let idx = id.x;
  var pos = positions[idx];
  
  // Fisica simples
  pos.z += 0.01;
  
  positions[idx] = pos;
}
```

```ts
const computePipeline = device.createComputePipeline({
  layout: 'auto',
  compute: {
    module: device.createShaderModule({ code: wgslCode }),
    entryPoint: 'updateParticles',
  },
});

const computePass = commandEncoder.beginComputePass();
computePass.setPipeline(computePipeline);
computePass.dispatchWorkgroups(particleCount / 64);
computePass.end();
```

## Metricas de Sucesso

- 10k+ particulas a 60fps
- Compute shader < 1ms
- Memory efficient (ping-pong buffers)
- Cross-browser (Chrome, Firefox, Safari)

================================================================================
## 📄 AGENTS.md
================================================================================

# Agents — WebGPU + GPGPU

## Enxame de Agents

### ComputeShaderAgent
**Responsabilidade:** Criar compute shaders WGSL.

**Input:**
```yaml
intent_type: generative
particle_count: 10000
physics_type: gravity
```

**Output:**
```wgsl
@compute @workgroup_size(64)
fn updateParticles(@builtin(global_invocation_id) id: vec3u) {
  // implementacao
}
```

### GPUSimulatorAgent
**Responsabilidade:** Setup WebGPU e dispatch compute.

### ParticleRendererAgent
**Responsabilidade:** Renderizar particulas com instancing.

================================================================================
## 📄 WORKFLOW.md
================================================================================

# Workflow — WebGPU + GPGPU

## Passos

1. **Setup WebGPU:** Request adapter, device, context
2. **Create Buffers:** Storage buffers para posicoes/velocidades
3. **Write Compute Shader:** WGSL para logica de simulacao
4. **Dispatch Compute:** Executar compute shader
5. **Render:** Desenhar particulas
6. **Loop:** requestAnimationFrame para animacao continua

## Exemplo Basico

```ts
async function init() {
  const adapter = await navigator.gpu.requestAdapter();
  const device = await adapter.requestDevice();
  
  // Create storage buffer
  const particleBuffer = device.createBuffer({
    size: particleCount * 12, // vec3f = 12 bytes
    usage: GPUBufferUsage.STORAGE | GPUBufferUsage.VERTEX,
  });
  
  // Create compute pipeline
  const computePipeline = device.createComputePipeline({
    layout: 'auto',
    compute: {
      module: device.createShaderModule({ code: wgslCode }),
      entryPoint: 'updateParticles',
    },
  });
  
  // Dispatch
  const commandEncoder = device.createCommandEncoder();
  const computePass = commandEncoder.beginComputePass();
  computePass.setPipeline(computePipeline);
  computePass.dispatchWorkgroups(particleCount / 64);
  computePass.end();
  
  device.queue.submit([commandEncoder.finish()]);
}
```

================================================================================
## 📄 INPUT_CONTRACT.yaml
================================================================================

intent_type: generative | hero_3d | simulation
particle_count: number (1000-100000)
physics_type: gravity | fluid | flocking | custom
compute_shader: string (WGSL)
render_mode: points | instanced-mesh | custom

delivery_state: prototype | ready

================================================================================
## 📄 OUTPUT_CONTRACT.yaml
================================================================================

code: string (ts + wgsl)
compute_shader: string (WGSL completo)
render_code: string (WebGPU render pass)
performance_metrics:
  fps: number
  compute_time_ms: number
  particle_count: number

asset_instructions: string (se necessario)
quality_report:
  lighthouse_performance: number
  frame_time_p95: number

delivery_state: prototype | ready

