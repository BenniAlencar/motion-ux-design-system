# ogl

**Skill compactada — conteudo completo**
Fonte: `skills/ogl/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# OGL

## Manifesto

Biblioteca WebGL minimalista e leve para graficos 3D com foco em simplicidade e performance.

## Stack

- ogl (npm)
- WebGL 2.0
- ES modules

## Keywords

ogl, webgl, 3d, graphics, minimal, lightweight, shader

## Visao Geral

OGL permite:
1. Graficos 3D com WebGL
2. Shaders customizados
3. Geometrias e materiais
4. Camera e controles

## Como Usar

```js
import { Renderer, Camera, Scene, Mesh, Program, Geometry } from 'ogl';

const renderer = new Renderer({ dpr: 2 });
const gl = renderer.gl;
document.body.appendChild(gl.canvas);

const camera = new Camera(gl, { fov: 45 });
camera.position.z = 5;

const scene = new Scene();

const geometry = new Geometry(gl, {
  position: { size: 3, data: new Float32Array([-1,-1,0, 1,-1,0, 0,1,0]) },
});

const program = new Program(gl, {
  vertex: `attribute vec3 position; void main() { gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`,
  fragment: `precision highp float; void main() { gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); }`,
});

const mesh = new Mesh(gl, { geometry, program });
scene.addChild(mesh);

function update() {
  requestAnimationFrame(update);
  renderer.render({ scene, camera });
}
update();
```

## Metricas de Sucesso

- 60fps em dispositivos modernos
- Shaders renderizando corretamente
- Geometrias visiveis
- Camera controlavel

