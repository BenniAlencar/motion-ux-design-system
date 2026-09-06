# r3f-threejs-drei

**Skill compactada — conteudo completo**
Fonte: `skills/r3f-threejs-drei/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# R3F + Three.js + Drei

## Manifesto

Three.js com React Three Fiber e Drei para criar experiencias 3D declarativas, performaticas e faceis de manter.

## Stack

- three (npm)
- @react-three/fiber
- @react-three/drei
- React

## Keywords

threejs, r3f, drei, react-three-fiber, 3d, webgl, shader, particle

## Visao Geral

R3F + Drei permite:
1. Three.js declarativo com React
2. Helpers e utilitarios prontos
3. Shaders customizados
4. Particulas e efeitos

## Como Usar

```tsx
import { Canvas } from '@react-three/fiber';
import { OrbitControls, PerspectiveCamera } from '@react-three/drei';

function App() {
  return (
    <Canvas>
      <PerspectiveCamera makeDefault position={[0, 0, 5]} />
      <OrbitControls />
      <mesh>
        <boxGeometry />
        <meshStandardMaterial color="hotpink" />
      </mesh>
    </Canvas>
  );
}
```

## Custom Component

```tsx
import { useFrame } from '@react-three/fiber';
import { useRef } from 'react';

function RotatingBox() {
  const meshRef = useRef();
  
  useFrame((state, delta) => {
    meshRef.current.rotation.y += delta;
  });
  
  return (
    <mesh ref={meshRef}>
      <boxGeometry />
      <meshStandardMaterial color="orange" />
    </mesh>
  );
}
```

## Shaders

```tsx
import { shaderMaterial } from '@react-three/drei';
import * as THREE from 'three';

const CustomMaterial = shaderMaterial(
  {
    time: 0,
    color: new THREE.Color(0x00ff00),
  },
  `varying vec2 vUv;
   void main() {
     vUv = uv;
     gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
   }`,
  `varying vec2 vUv;
   uniform float time;
   uniform vec3 color;
   void main() {
     gl_FragColor = vec4(color * sin(vUv.x * time), 1.0);
   }`
);
```

## Particulas

```tsx
function Particles({ count = 1000 }) {
  const points = useRef();
  
  const positions = new Float32Array(count * 3);
  for (let i = 0; i < count * 3; i++) {
    positions[i] = (Math.random() - 0.5) * 10;
  }
  
  useFrame((state) => {
    points.current.rotation.y = state.clock.elapsedTime * 0.1;
  });
  
  return (
    <points ref={points}>
      <bufferGeometry>
        <bufferAttribute
          attach="attributes-position"
          count={count}
          array={positions}
          itemSize={3}
        />
      </bufferGeometry>
      <pointsMaterial size={0.1} color="white" />
    </points>
  );
}
```

## Metricas de Sucesso

- 60fps constante
- Shaders renderizando
- Particulas animadas
- Controles funcionando

