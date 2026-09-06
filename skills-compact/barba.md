# barba

**Skill compactada — conteudo completo**
Fonte: `skills/barba/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Barba.js

## Manifesto

Transicoes de pagina smooth e SPA-like usando Barba.js para navegacao sem reload completo.

## Stack

- @barba/core (npm)
- GSAP (opcional, para animacoes)
- Webpack/Vite (build)

## Keywords

barba, page-transition, spa, navigation, smooth, route, history

## Visao Geral

Barba.js permite:
1. Navegacao sem reload completo
2. Transicoes de pagina animadas
3. Manter estado entre paginas
4. SEO-friendly (history API)

## Como Usar

```js
import barba from '@barba/core';

barba.init({
  transitions: [
    {
      name: 'default',
      async leave(data) {
        // Animacao de saida
        await gsap.to(data.current.container, {
          opacity: 0,
          duration: 0.5,
        });
      },
      async enter(data) {
        // Animacao de entrada
        await gsap.from(data.next.container, {
          opacity: 0,
          duration: 0.5,
        });
      },
    },
  ],
});
```

## Transicoes Customizadas

```js
barba.init({
  transitions: [
    {
      name: 'fade',
      async leave(data) {
        await gsap.to(data.current.container, { opacity: 0 });
      },
      async enter(data) {
        await gsap.from(data.next.container, { opacity: 0 });
      },
    },
    {
      name: 'slide-left',
      to: { namespace: ['about'] },
      async leave(data) {
        await gsap.to(data.current.container, { x: '-100%' });
      },
      async enter(data) {
        gsap.set(data.next.container, { x: '100%' });
        await gsap.to(data.next.container, { x: '0%' });
      },
    },
  ],
});
```

## Hooks

```js
barba.init({
  hooks: {
    async beforeEnter(data) {
      console.log('Before enter:', data.next.url.href);
    },
    async afterEnter(data) {
      console.log('After enter:', data.next.url.href);
    },
    async beforeLeave(data) {
      console.log('Before leave:', data.current.url.href);
    },
  },
});
```

## Metricas de Sucesso

- Transicoes suaves a 60fps
- Navegacao sem reload visivel
- History API funcionando corretamente
- SEO preservado (meta tags, title)

