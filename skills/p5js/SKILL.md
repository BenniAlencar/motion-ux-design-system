---
name: p5js
description: p5.js para arte generativa e creative coding
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - p5.js
    - p5js
    - generative art
    - creative coding
  routes:
    - spatial
depends_on:
  - cerebro-orquestrador
outputs:
  - generative_plan
  - sketch_config
  - integration_code
---

# p5.js

## Stack

- p5
- Canvas 2D

## Enxame de Agentes

1. **Generative Analyst** - Analisa arte generativa necessaria
2. **Sketch Designer** - Configura sketch p5
3. **Interaction Designer** - Configura interacoes
4. **Integration Engineer** - Gera codigo React/vanilla

## Sketch Basico

```ts
import p5 from 'p5'

new p5((p) => {
  p.setup = () => {
    p.createCanvas(window.innerWidth, window.innerHeight)
    p.background(0)
  }
  
  p.draw = () => {
    p.background(0, 10)
    p.fill(255)
    p.ellipse(p.mouseX, p.mouseY, 50, 50)
  }
})
```

## Particulas

```ts
const particles: Array<{ x: number; y: number; vx: number; vy: number }> = []

new p5((p) => {
  p.setup = () => {
    p.createCanvas(window.innerWidth, window.innerHeight)
    for (let i = 0; i < 100; i++) {
      particles.push({
        x: p.random(p.width),
        y: p.random(p.height),
        vx: p.random(-2, 2),
        vy: p.random(-2, 2),
      })
    }
  }
  
  p.draw = () => {
    p.background(0, 10)
    p.fill(255)
    
    particles.forEach((pt) => {
      pt.x += pt.vx
      pt.y += pt.vy
      
      if (pt.x < 0 || pt.x > p.width) pt.vx *= -1
      if (pt.y < 0 || pt.y > p.height) pt.vy *= -1
      
      p.ellipse(pt.x, pt.y, 10, 10)
    })
  }
})
```

## React com p5

```tsx
import { useEffect, useRef } from 'react'
import p5 from 'p5'

export function GenerativeCanvas() {
  const canvasRef = useRef<HTMLDivElement>(null)
  
  useEffect(() => {
    if (!canvasRef.current) return
    
    const sketch = (p: p5) => {
      p.setup = () => p.createCanvas(canvasRef.current!.clientWidth, 400)
      p.draw = () => {
        p.background(240)
        p.fill(0)
        p.ellipse(p.mouseX, p.mouseY, 50, 50)
      }
    }
    
    new p5(sketch, canvasRef.current)
  }, [])
  
  return <div ref={canvasRef} />
}
```

## Output

```yaml
p5_plan:
  sketch_config:
    width: window.innerWidth
    height: window.innerHeight
    background: 0
  elements:
    - type: particles
      count: 100
  interactions: mouse_follow
  integration: react
```
