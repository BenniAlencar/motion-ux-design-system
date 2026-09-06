# rapier

**Skill compactada — conteudo completo**
Fonte: `skills/rapier/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Rapier

## Manifesto

Motor de fisica 3D/2D em Rust compilado para WebAssembly para simulacoes de fisica realistas no navegador.

## Stack

- @dimforge/rapier3d ou rapier2d
- WebAssembly
- Three.js/OGL (renderizacao)

## Keywords

rapier, physics, rigid-body, collision, simulation, wasm, rust

## Visao Geral

Rapier permite:
1. Simulacoes de fisica 3D/2D
2. Rigid bodies e colisoes
3. Gravidade e forcas
4. Performance WebAssembly

## Como Usar

```js
import RAPIER from 'rapier';

await RAPIER.init();

const gravity = { x: 0.0, y: -9.81, z: 0.0 };
const world = new RAPIER.World(gravity);

// Criar rigid body
const rigidBodyDesc = RAPIER.RigidBodyDesc.dynamic()
  .setTranslation(0.0, 5.0, 0.0);
const rigidBody = world.createRigidBody(rigidBodyDesc);

// Adicionar collider
const colliderDesc = RAPIER.ColliderDesc.ball(0.5);
world.createCollider(colliderDesc, rigidBody);

// Step da simulacao
world.step();

// Ler posicao
const position = rigidBody.translation();
console.log(position);
```

## Metricas de Sucesso

- Fisica simulando corretamente
- Colisoes detectadas
- Performance > 60fps
- WebAssembly carregando

