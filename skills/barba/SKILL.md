---
name: barba
description: Barba.js para transicoes de pagina suaves
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - barba.js
    - barba
    - page transition
    - smooth navigation
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
outputs:
  - barba_config
  - transition_plan
  - integration_code
---

# Barba.js

## Stack

- @barba/core
- @barba/prefetch (opcional)
- GSAP para animacoes de transicao

## Enxame de Agentes

1. **Transition Analyst** - Analisa transicoes necessarias
2. **Config Engineer** - Configura Barba
3. **Animation Designer** - Desenha transicoes com GSAP
4. **Integration Engineer** - Gera codigo Next/vanilla

## Configuracao Basica

```ts
import barba from '@barba/core'
import gsap from 'gsap'

barba.init({
  debug: true,
  logLevel: 4,
  prefetchIgnore: '/admin',
  views: [{ namespace: 'home', container: 'main' }],
  transitions: [
    {
      name: 'default',
      async leave({ current }) {
        await gsap.to(current.container, { opacity: 0, duration: 0.5 })
      },
      async enter({ next }) {
        await gsap.from(next.container, { opacity: 0, duration: 0.5 })
      },
    },
  ],
})
```

## Transicao Custom

```ts
barba.init({
  transitions: [
    {
      name: 'fade-up',
      async leave({ current }) {
        await gsap.to(current.container, {
          opacity: 0,
          y: -50,
          duration: 0.5,
          ease: 'power2.out',
        })
      },
      async enter({ next }) {
        await gsap.from(next.container, {
          opacity: 0,
          y: 50,
          duration: 0.5,
          ease: 'power2.out',
        })
      },
    },
  ],
})
```

## Next.js com Barba

```tsx
// pages/_app.tsx
import { useEffect } from 'react'
import { useRouter } from 'next/router'
import barba from '@barba/core'

export default function App({ Component, pageProps }) {
  const router = useRouter()
  
  useEffect(() => {
    barba.init({
      links: 'a[href]:not([data-no-barba])',
      prevent: ({ href }) => href.startsWith('/api'),
    })
  }, [])
  
  return <Component {...pageProps} />
}
```

## Output

```yaml
barba_plan:
  transitions:
    - name: default
      type: fade
      duration: 0.5
    - name: fade-up
      type: fade_translate
      duration: 0.5
  prefetch: true
  integration: nextjs
  gsap_integration: true
```
