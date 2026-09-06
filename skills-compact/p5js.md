# p5js

**Skill compactada — conteudo completo**
Fonte: `skills/p5js/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# P5.js

## Manifesto

Biblioteca de creative coding para arte generativa, visualizacoes e prototipagem rapida de ideias criativas.

## Stack

- p5 (npm ou CDN)
- Canvas API
- WebGL mode (opcional)

## Keywords

p5js, creative-coding, generative-art, canvas, visualization, prototyping

## Visao Geral

P5.js permite:
1. Arte generativa e visualizacoes
2. Prototipagem rapida
3. Interacao com mouse/keyboard
4. Audio e video processing

## Como Usar

```js
import p5 from 'p5';

new p5((sketch) => {
  sketch.setup = () => {
    sketch.createCanvas(800, 600);
  };

  sketch.draw = () => {
    sketch.background(220);
    sketch.fill(255, 0, 0);
    sketch.ellipse(sketch.mouseX, sketch.mouseY, 50, 50);
  };
});
```

## Arte Generativa

```js
sketch.draw = () => {
  sketch.noStroke();
  for (let i = 0; i < 100; i++) {
    sketch.fill(sketch.random(255), sketch.random(255), sketch.random(255));
    sketch.ellipse(sketch.random(sketch.width), sketch.random(sketch.height), 50, 50);
  }
};
```

## Interacao

```js
sketch.mousePressed = () => {
  sketch.background(sketch.random(255));
};

sketch.keyPressed = () => {
  if (sketch.key === 's') {
    sketch.saveCanvas('my-art', 'png');
  }
};
```

## Metricas de Sucesso

- Canvas renderizando a 60fps
- Arte generativa funcionando
- Interacao respondendo
- Save/export funcionando

