# pixi

**Skill compactada — conteudo completo**
Fonte: `skills/pixi/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Pixi.js

## Manifesto

Motor de renderizacao 2D WebGL acelerado por GPU para jogos, animacoes e visualizacoes interativas.

## Stack

- pixi.js (npm)
- WebGL renderer
- Canvas fallback

## Keywords

pixi, 2d, webgl, game, sprite, interactive, gpu-accelerated

## Visao Geral

Pixi.js permite:
1. Renderizacao 2D acelerada por GPU
2. Sprites e animacoes
3. Interacao (click, hover, drag)
4. Jogos 2D completos

## Como Usar

```js
import * as PIXI from 'pixi.js';

const app = new PIXI.Application({
  width: 800,
  height: 600,
  backgroundColor: 0x1099bb,
});
document.body.appendChild(app.view);

const sprite = PIXI.Sprite.from('image.png');
sprite.x = 400;
sprite.y = 300;
sprite.anchor.set(0.5);
app.stage.addChild(sprite);

// Animacao
app.ticker.add((delta) => {
  sprite.rotation += 0.01 * delta;
});
```

## Interacao

```js
sprite.eventMode = 'static';
sprite.cursor = 'pointer';

sprite.on('pointerdown', () => {
  sprite.scale.x *= 1.2;
  sprite.scale.y *= 1.2;
});
```

## Metricas de Sucesso

- 60fps constante
- Sprites renderizados corretamente
- Interacao funcionando
- Memory management eficiente

