---
name: rive
description: Rive animations + state machines
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - rive
    - animation
    - state machine
    - microinteraction
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
outputs:
  - rive_integration
  - state_machine_config
  - fallback_gif
---

# Rive Animations

## Stack

- @rive-app/react-canvas
- Rive Web Runtime
- Fallback GIF/APNG

## Enxame de Agentes

1. **Animation Analyst** - Avalia se Rive e adequado
2. **State Machine Designer** - Configura inputs e estados
3. **Integration Engineer** - Gera codigo React
4. **Fallback Designer** - Cria GIF equivalente

## Integracao Padrao

```tsx
'use client'
import { useRive, Layout, Fit } from '@rive-app/react-canvas'

export function AnimatedIcon() {
  const { RiveComponent } = useRive({
    src: '/animations/icon.riv',
    stateMachines: 'State Machine 1',
    artboard: 'Artboard',
    layout: new Layout({ fit: Fit.Contain }),
  })

  return <RiveComponent style={{ width: 64, height: 64 }} />
}
```

## State Machine

```ts
// Trigger animation
const { rive, RiveComponent } = useRive({
  src: '/button.riv',
  stateMachines: 'State Machine 1',
  onStateChange: (event) => {
    console.log('State:', event.data)
  },
})

// Fire input
rive?.fireState('hover')
rive?.fireState('press')
```

## Fallback

```html
<img src="/animations/icon.gif" alt="Animacao do icone" width="64" height="64" />
```

## Performance Checklist

- [ ] Arquivo .riv otimizado (< 200kB ideal)
- [ ] Lazy load em animacoes fora do viewport
- [ ] Fallback GIF para browsers sem suporte
- [ ] Testar em mobile com CPU limitada
