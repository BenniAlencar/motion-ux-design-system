# swup

**Skill compactada — conteudo completo**
Fonte: `skills/swup/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Swup

## Manifesto

Transicoes de pagina modernas e modulares usando Swup para navegacao SPA-like com plugins extensivos.

## Stack

- swup (npm)
- Plugins Swup (opcional)
- GSAP/Motion (animacoes)

## Keywords

swup, page-transition, spa, navigation, modular, plugin, history, route

## Visao Geral

Swup permite:
1. Navegacao sem reload
2. Sistema de plugins extensivel
3. Transicoes customizaveis
4. Analytics, preload, cache integrados

## Como Usar

```js
import Swup from 'swup';

const swup = new Swup({
  containers: ['#swup'],
  plugins: [],
  animateHistoryBrowsing: true,
});
```

## Animacoes com GSAP

```js
import Swup from 'swup';
import GSAPPlugin from 'swup-gsap-plugin';

const swup = new Swup({
  containers: ['#swup'],
  plugins: [new GSAPPlugin()],
});

swup.hooks.on('animation:out:start', () => {
  gsap.to('.page', { opacity: 0, duration: 0.5 });
});

swup.hooks.on('animation:in:start', () => {
  gsap.from('.page', { opacity: 0, duration: 0.5 });
});
```

## Plugins Populares

```js
import Swup from 'swup';
import PreloadPlugin from 'swup-preload-plugin';
import FormsPlugin from 'swup-forms-plugin';
import ProgressPlugin from 'swup-progress-plugin';
import FadeTheme from 'swup-fade-theme';

const swup = new Swup({
  plugins: [
    new PreloadPlugin(),
    new FormsPlugin(),
    new ProgressPlugin(),
    new FadeTheme(),
  ],
});
```

## Hooks Disponiveis

- `animation:out:start`
- `animation:out:end`
- `animation:in:start`
- `animation:in:end`
- `content:replace`
- `page:view`
- `link:clicked`
- `popState`

## Metricas de Sucesso

- Transicoes suaves
- Preload funcionando
- Forms submetendo sem reload
- Progress bar de carregamento
- Analytics trackando views

