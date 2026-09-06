---
name: performance-budget
description: Frame budget, memory, draw calls, texture memory, bundle size
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - performance
    - budget
    - fps
    - memory
    - bundle
    - lighthouse
  routes:
    - quality
depends_on:
  - cerebro-orquestrador
outputs:
  - performance_budget
  - frame_analysis
  - memory_report
  - bundle_report
  - recommendations
---

# Performance Budget

## Stack

- Lighthouse CI
- WebPageTest
- Chrome DevTools Performance
- Three.js Stats (para 3D)

## Enxame de Agentes

1. **Budget Architect** - Define budgets por tipo de pagina
2. **Frame Analyst** - Analisa frame time, long tasks, jank
3. **Memory Analyst** - Verifica memory usage, leaks
4. **Bundle Analyst** - Analisa bundle size, code split
5. **3D Performance Analyst** - Draw calls, texture memory, GPU

## Budgets Padrao

### Landing Page

```yaml
performance_budget:
  lighthouse:
    performance_score: 90
    fcp: 1.5s
    lcp: 2.5s
    tti: 3.5s
    tbt: 200ms
    cls: 0.1
  bundle:
    js_kb: 150
    css_kb: 50
    font_kb: 120
    image_kb: 500
  runtime:
    frame_time_p95_ms: 16
    long_tasks_max: 2
    memory_mb_max: 128
```

### Hero 3D

```yaml
performance_budget:
  lighthouse:
    performance_score: 80
    fcp: 2.0s
    lcp: 3.0s
  bundle:
    js_kb: 250
    css_kb: 50
  runtime:
    frame_time_p95_ms: 16
    draw_calls_max: 100
    texture_memory_mb: 64
    memory_mb_max: 256
```

## Frame Analysis

```ts
// Medir frame time
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.entryType === 'longtask') {
      console.log('Long task:', entry.duration, 'ms')
    }
  }
})
observer.observe({ entryTypes: ['longtask'] })
```

## Memory Analysis

```ts
// Medir memory (Chrome only)
if (performance.memory) {
  const memory = performance.memory
  console.log('Used JS heap:', memory.usedJSHeapSize / 1048576, 'MB')
}
```

## 3D Performance

```ts
// Three.js stats
import { Stats } from 'three/examples/jsm/libs/stats.module.js'

const stats = new Stats()
document.body.appendChild(stats.dom)

function animate() {
  requestAnimationFrame(animate)
  stats.update()
}
```

## Output

```yaml
performance_report:
  lighthouse_score: 87
  fcp: 1.8s
  lcp: 2.9s
  tbt: 180ms
  bundle:
    js_kb: 142
    css_kb: 48
  frame_time_p95_ms: 14
  long_tasks: 1
  memory_mb: 98
  accepted: true
  recommendations:
    - "Lazy load imagens abaixo do fold"
    - "Code split vendor chunks"
```
