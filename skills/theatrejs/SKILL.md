---
name: theatrejs
description: Theatre.js para animacoes e timelines visuais
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - theatre.js
    - theatrejs
    - timeline visual
    - animacao visual
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
outputs:
  - theatre_config
  - timeline_plan
  - integration_code
---

# Theatre.js

## Stack

- @theatre/core
- @theatre/react (opcional)
- Integracao com Three.js, GSAP, etc

## Enxame de Agentes

1. **Timeline Analyst** - Analisa animacoes necessarias
2. **Sheet Designer** - Configura sheets e objects
3. **Timeline Builder** - Cria timelines visuais
4. **Integration Engineer** - Gera codigo React/Three

## Configuracao Basica

```ts
import { sheet, config } from '@theatre/core'

const heroSheet = sheet('Hero', { position: { x: 0, y: 0, z: 0 }, opacity: 1 })

// Em um componente React
import { useEditableSheet } from '@theatre/react'

function Hero() {
  const sheet = useEditableSheet(heroSheet)
  return (
    <div style={{ opacity: sheet.val.opacity }}>
      {sheet.val.position.x}
    </div>
  )
}
```

## Timeline

```ts
import { timeline } from '@theatre/core'

const tl = timeline({ duration: 5 })

// Keyframes
heroSheet.position.x = tl.at(0, 0).at(2, 100).at(4, 50)
heroSheet.opacity = tl.at(0, 1).at(2, 0.5).at(4, 1)

// Play
tl.play()
```

## Integracao Three.js

```ts
import { useThree } from '@theatre/react-three'

function AnimatedMesh() {
  const mesh = useThree()
  const sheet = sheet('Mesh', { rotation: { x: 0, y: 0, z: 0 } })
  
  useFrame(() => {
    mesh.current.rotation.x = sheet.val.rotation.x
    mesh.current.rotation.y = sheet.val.rotation.y
  })
  
  return <mesh ref={mesh} />
}
```

## Output

```yaml
theatre_plan:
  sheets:
    - name: Hero
      props: [position, opacity]
    - name: Mesh
      props: [rotation]
  timeline_duration: 5
  integration: react-three
  editable: true
```
