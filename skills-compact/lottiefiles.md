# lottiefiles

**Skill compactada — conteudo completo**
Fonte: `skills/lottiefiles/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# LottieFiles

## Manifesto

Animacoes vetoriais leves e escalaveis usando formato Lottie (JSON) para microinteracoes e animacoes complexas.

## Stack

- @lottiefiles/react (React)
- lottie-web (vanilla JS)
- After Effects + Bodymovin (criacao)

## Keywords

lottie, animation, json, vector, after-effects, microinteraction, svg

## Visao Geral

LottieFiles permite:
1. Exportar animacoes do After Effects
2. Renderizar como SVG/Canvas
3. Controlar via codigo (play, pause, seek)
4. Interagir com scroll/click

## Como Usar (React)

```tsx
import { Player } from '@lottiefiles/react';

function App() {
  return (
    <Player
      src="https://lottie.host/animation.json"
      style={{ height: '200px', width: '200px' }}
      loop
      autoplay
    />
  );
}
```

## Como Usar (Vanilla)

```js
import { loadAnimation } from 'lottie-web';

const animation = loadAnimation({
  container: document.getElementById('lottie'),
  src: 'animation.json',
  renderer: 'svg',
  loop: true,
  autoplay: true,
});

// Controle
animation.play();
animation.pause();
animation.setSpeed(2);
animation.goToAndStop(30, true); // frame 30
```

## Integracao com Scroll

```js
const animation = loadAnimation({...});

window.addEventListener('scroll', () => {
  const scrollPercent = window.scrollY / document.body.scrollHeight;
  const frame = Math.floor(scrollPercent * animation.totalFrames);
  animation.goToAndStop(frame, true);
});
```

## Metricas de Sucesso

- Arquivo JSON < 500KB
- Renderizacao SVG/Canvas performatica
- Controle preciso de playback
- Suporte a interacoes (hover, click, scroll)

