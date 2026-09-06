---
name: lygia-agents
version: 1.0.0
---

# Lygia - Enxame de Agentes

## 1. Shader Architect

**Responsabilidade:** Selecionar funcoes Lygia e planejar shader.

**Output:**
```yaml
shader_plan:
  effect_type: halo_breath
  lygia_functions:
    - lygia/sdf/circleSDF
    - lygia/generative/fbm
    - lygia/color/palette
  uniforms_needed:
    - uTime: float
    - uIdle: float
    - uPointer: vec2
  complexity: medium
  mobile_safe: true
```

## 2. GLSL Engineer

**Responsabilidade:** Escrever shader com Lygia.

**Output:**
```glsl
#include "lygia/sdf/circleSDF.glsl"
#include "lygia/generative/fbm.glsl"
#include "lygia/color/palette.glsl"

varying vec2 vUv;
uniform float uTime;
uniform float uIdle;
uniform vec2 uPointer;

void main() {
  vec2 st = vUv * 2.0 - 1.0;
  st += (uPointer - 0.5) * 0.2;
  
  // Respiracao com idle
  float breath = 1.0 + sin(uTime * 0.5 + uIdle * 0.2) * (0.05 + uIdle * 0.02);
  
  float d = circleSDF(st * breath);
  float n = fbm(st * 2.0 + uTime * 0.05) * 0.15;
  d += n;
  
  vec3 col = palette(d * 2.0 + uTime * 0.1,
    vec3(0.5, 0.5, 0.5), vec3(0.5, 0.5, 0.5),
    vec3(1.0, 1.0, 1.0), vec3(0.0, 0.33, 0.67));
  
  float alpha = 1.0 - smoothstep(0.0, 1.2, d);
  gl_FragColor = vec4(col, alpha * 0.6);
}
```

## 3. Integration Engineer

**Responsabilidade:** Integrar com Three.js/R3F.

**Output:**
```tsx
import { shaderMaterial } from '@react-three/drei'

const HaloMaterial = shaderMaterial(
  { uTime: 0, uIdle: 0, uPointer: [0.5, 0.5] },
  `varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`,
  `#include "lygia/sdf/circleSDF.glsl"
   #include "lygia/generative/fbm.glsl"
   #include "lygia/color/palette.glsl"
   varying vec2 vUv;
   uniform float uTime, uIdle;
   uniform vec2 uPointer;
   void main(){
     vec2 st = vUv * 2.0 - 1.0;
     st += (uPointer - 0.5) * 0.2;
     float breath = 1.0 + sin(uTime * 0.5 + uIdle * 0.2) * (0.05 + uIdle * 0.02);
     float d = circleSDF(st * breath);
     float n = fbm(st * 2.0 + uTime * 0.05) * 0.15;
     vec3 col = palette(d * 2.0 + uTime * 0.1, vec3(0.5), vec3(0.5), vec3(1.0), vec3(0.0,0.33,0.67));
     gl_FragColor = vec4(col, (1.0 - smoothstep(0.0, 1.2, d)) * 0.6);
   }`
)
```

## 4. Fallback Designer

**Responsabilidade:** Criar versao CSS.

**Output:**
```css
.halo {
  width: 60vw;
  height: 60vw;
  background: radial-gradient(circle at 50% 50%, #426bff 0%, transparent 70%);
  filter: blur(80px);
  opacity: 0.15;
  animation: breath 8s ease-in-out infinite alternate;
  position: absolute;
  z-index: -1;
}

@keyframes breath {
  0% { transform: scale(0.9); opacity: 0.1; }
  100% { transform: scale(1.1); opacity: 0.2; }
}

@media (prefers-reduced-motion: reduce) {
  .halo {
    animation: none;
    transform: scale(1);
  }
}
```

## 5. Performance Reviewer

**Responsabilidade:** Verificar GPU load.

**Checklist:**
- [ ] Evitar loops pesados no fragment shader
- [ ] Testar em mobile GPU (Adreno, Mali)
- [ ] Medir frame time p95 < 16ms
- [ ] Fallback CSS para browsers sem WebGL

**Output:**
```yaml
performance_review:
  mobile_fps_estimate: 55
  desktop_fps_estimate: 60
  fragment_complexity: medium
  lygia_functions_count: 3
  fallback_available: true
  recommendations:
    - "Usar fbm com 3 octaves max em mobile"
    - "Evitar palette dinamica complexa"
```
