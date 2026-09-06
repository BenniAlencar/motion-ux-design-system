---
name: swup
description: Swup para transicoes de pagina modernas
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - swup
    - page transition
    - navigation
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
outputs:
  - swup_config
  - transition_plan
  - integration_code
---

# Swup

## Stack

- swup
- Plugins: AnimationPlugin, BodyClassPlugin, etc
- GSAP para animacoes

## Enxame de Agentes

1. **Transition Analyst** - Analisa transicoes
2. **Plugin Configurer** - Configura plugins
3. **Animation Designer** - Desenha transicoes
4. **Integration Engineer** - Gera codigo

## Configuracao Basica

```ts
import Swup from 'swup'
import { AnimationPlugin } from 'swup/AnimationPlugin'
import { BodyClassPlugin } from 'swup/BodyClassPlugin'

const swup = new Swup({
  plugins: [
    AnimationPlugin(),
    BodyClassPlugin(),
  ],
  animationSelector: '[data-swup]',
})

swup.on('transition:start', () => {
  document.body.classList.add('transitioning')
})

swup.on('transition:end', () => {
  document.body.classList.remove('transitioning')
})
```

## CSS Transitions

```css
[data-swup] {
  transition: opacity 0.3s ease;
}

html.is-animating [data-swup] {
  opacity: 0;
}
```

## GSAP Integration

```ts
import Swup from 'swup'
import gsap from 'gsap'

const swup = new Swup()

swup.hooks.on('transition:start', async (visit) => {
  await gsap.to(visit.to.containers, { opacity: 0, duration: 0.3 })
})

swup.hooks.on('transition:end', async (visit) => {
  await gsap.from(visit.to.containers, { opacity: 0, duration: 0.3 })
})
```

## Output

```yaml
swup_plan:
  plugins:
    - AnimationPlugin
    - BodyClassPlugin
  css_transitions: true
  gsap_integration: true
  transition_duration: 0.3
  integration: vanilla
```
