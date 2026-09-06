# theatrejs

**Skill compactada — conteudo completo**
Fonte: `skills/theatrejs/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Theatre.js

## Manifesto

Animacoes cinematicas e timeline-based para Three.js e React Three Fiber com editor visual integrado.

## Stack

- @theatre/core
- @theatre/react
- three / @react-three/fiber

## Keywords

theatre, animation, timeline, cinematic, threejs, r3f, keyframe, sequencer

## Visao Geral

Theatre.js permite:
1. Criar animacoes complexas com timeline
2. Editor visual integrado no browser
3. Keyframes e curves interpoladas
4. Integracao nativa com Three.js/R3F

## Como Usar (R3F)

```tsx
import { useSetupTheatre } from '@theatre/react';
import { studio } from '@theatre/core';

function Scene() {
  const objectRef = useRef();
  
  useSetupTheatre(() => {
    const sheet = studio.sheet(objectRef.current);
    
    sheet.prop('position', {
      x: { value: 0, scrub: true },
      y: { value: 0, scrub: true },
      z: { value: 0, scrub: true },
    });
  });
  
  return <mesh ref={objectRef} />;
}
```

## Timeline e Keyframes

```js
import { sequence } from '@theatre/core';

const seq = studio.sequence;

// Criar keyframes
seq.position.x.keyframe(0, 0);   // frame 0, x=0
seq.position.x.keyframe(30, 5);  // frame 30, x=5
seq.position.x.keyframe(60, 0);  // frame 60, x=0

// Playback
seq.position.x.play();
seq.position.x.scrub(0.5); // 50% da timeline
```

## Editor Visual

Theatre.js inclui:
- Timeline editor
- Curve editor (Bezier, linear, step)
- Property inspector
- Playback controls

## Metricas de Sucesso

- Timeline scrub suave
- Keyframes precisos
- Curves interpoladas corretamente
- Editor integrado funcional

