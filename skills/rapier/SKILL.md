---
name: rapier
description: Rapier physics engine para simulacoes 3D
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - rapier
    - physics
    - simulacao fisica
    - colisao
  routes:
    - spatial
depends_on:
  - cerebro-orquestrador
  - r3f-threejs-drei
outputs:
  - physics_plan
  - world_config
  - integration_code
---

# Rapier Physics

## Stack

- @react-three/rapier
- Three.js / R3F

## Enxame de Agentes

1. **Physics Analyst** - Analisa necessidades de fisica
2. **World Configurer** - Configura mundo fisico
3. **Body Designer** - Configura rigid bodies
4. **Integration Engineer** - Gera codigo R3F

## Configuracao Basica

```tsx
import { Physics, RigidBody } from '@react-three/rapier'

export function Scene() {
  return (
    <Physics gravity={[0, -9.81, 0]}>
      <RigidBody>
        <mesh>
          <boxGeometry />
          <meshStandardMaterial color="red" />
        </mesh>
      </RigidBody>
      
      <RigidBody type="fixed" position={[0, -2, 0]}>
        <mesh>
          <boxGeometry args={[10, 0.5, 10]} />
          <meshStandardMaterial color="gray" />
        </mesh>
      </RigidBody>
    </Physics>
  )
}
```

## Fisica com Pointer

```tsx
import { RigidBody, useRapier } from '@react-three/rapier'
import { useRef } from 'react'

export function InteractiveBall() {
  const body = useRef(null)
  const { rapier } = useRapier()
  
  const onPointerMove = (e) => {
    if (body.current) {
      body.current.applyImpulse({
        x: e.movementX * 0.01,
        y: e.movementY * 0.01,
        z: 0,
      })
    }
  }
  
  return (
    <RigidBody ref={body} onPointerMove={onPointerMove}>
      <mesh>
        <sphereGeometry />
        <meshStandardMaterial color="blue" />
      </mesh>
    </RigidBody>
  )
}
```

## Colisoes

```tsx
import { RigidBody, Collider } from '@react-three/rapier'

export function CollisionScene() {
  const onCollisionEnter = () => console.log('Colidiu!')
  
  return (
    <Physics>
      <RigidBody onCollisionEnter={onCollisionEnter}>
        <Collider shape="ball" args={[0.5]}>
          <mesh>
            <sphereGeometry args={[0.5]} />
            <meshStandardMaterial color="green" />
          </mesh>
        </Collider>
      </RigidBody>
    </Physics>
  )
}
```

## Output

```yaml
rapier_plan:
  world_config:
    gravity: [0, -9.81, 0]
  rigid_bodies:
    - type: dynamic
      shape: box
    - type: fixed
      shape: box
  interactions: pointer_impulse
  collisions: true
  integration: r3f
```
