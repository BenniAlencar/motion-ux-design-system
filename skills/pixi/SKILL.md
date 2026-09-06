---
name: pixi
description: Pixi.js para rendering 2D WebGL de alta performance
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - pixi.js
    - pixi
    - webgl 2d
    - rendering 2d
  routes:
    - spatial
depends_on:
  - cerebro-orquestrador
outputs:
  - pixi_config
  - scene_plan
  - integration_code
---

# Pixi.js

## Stack

- pixi.js
- Plugins: particle, filters, etc

## Enxame de Agentes

1. **Scene Analyst** - Analisa cena 2D necessaria
2. **Renderer Configurer** - Configura WebGL
3. **Sprite Designer** - Configura sprites e containers
4. **Integration Engineer** - Gera codigo

## Configuracao Basica

```ts
import { Application, Sprite, Container } from 'pixi.js'

const app = new Application({
  width: window.innerWidth,
  height: window.innerHeight,
  backgroundColor: 0x1099bb,
  resolution: window.devicePixelRatio || 1,
  autoDensity: true,
  antialias: true,
})

document.body.appendChild(app.canvas)

// Sprite
const sprite = Sprite.from('/image.png')
sprite.x = 100
sprite.y = 100
sprite.scale.set(0.5)
app.stage.addChild(sprite)

// Container
const container = new Container()
container.addChild(sprite)
app.stage.addChild(container)
```

## Animation

```ts
import { Ticker } from 'pixi.js'

const ticker = new Ticker()
ticker.add((delta) => {
  sprite.rotation += 0.01 * delta
  sprite.x += 2 * delta
})
ticker.start()
```

## Filters

```ts
import { BlurFilter, ColorMatrixFilter } from 'pixi.js'

const blur = new BlurFilter()
sprite.filters = [blur]

const color = new ColorMatrixFilter()
color.hue(90, true)
sprite.filters = [color]
```

## Output

```yaml
pixi_plan:
  app_config:
    width: 1920
    height: 1080
    antialias: true
    resolution: 2
  sprites: 5
  containers: 3
  filters: [BlurFilter, ColorMatrixFilter]
  animation: ticker_based
  integration: vanilla
```
