# spline-runtime

**Skill compactada — conteudo completo**
Fonte: `skills/spline-runtime/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Spline Runtime

## Manifesto

Integracao de cenas 3D criadas no Spline (spline.design) com interatividade em tempo real via Spline Runtime.

## Stack

- @splinetool/runtime (npm)
- React/Vue/Three.js (opcional)
- Spline Viewer component

## Keywords

spline, 3d, runtime, interactive, spline-design, webgl, scene

## Visao Geral

Spline Runtime permite:
1. Carregar cenas 3D do Spline
2. Interagir com objetos via codigo
3. Animar propriedades em tempo real
4. Integrar com React/Three.js

## Como Usar

```ts
import Spline from '@splinetool/react';

function App() {
  return (
    <Spline
      scene="https://prod.spline.design/scene-url"
      onSplineReady={(spline) => {
        // Acessar objetos da cena
        const object = spline.findObjectByName('Cube');
        object.position.x = 5;
      }}
    />
  );
}
```

## API Runtime

```ts
spline.findObjectByName('ObjectName');
spline.findMaterialByName('MaterialName');

// Modificar propriedades
object.position = { x: 0, y: 0, z: 0 };
object.rotation = { x: 0, y: Math.PI, z: 0 };
object.scale = { x: 1, y: 1, z: 1 };
object.visible = true;

// Animacoes
spline.setVariable('hover', true);
spline.setVariable('color', '#ff0000');
```

## Metricas de Sucesso

- Carregamento < 3s
- Interacao em tempo real
- 60fps em dispositivos modernos
- Fallback graceful para dispositivos fracos

