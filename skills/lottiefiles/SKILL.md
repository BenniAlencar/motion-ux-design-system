---
name: lottiefiles
description: Lottie JSON + bodymovin
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - lottie
    - lottiefiles
    - json animation
    - after effects
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
outputs:
  - lottie_integration
  - fallback_gif
  - performance_report
---

# LottieFiles

## Stack

- @lottiefiles/react
- Lottie Web Player
- Fallback GIF/APNG

## Enxame de Agentes

1. **Animation Analyst** - Avalia se Lottie e adequado
2. **Asset Director** - Confere JSON, direitos, otimizacao
3. **Integration Engineer** - Gera codigo React
4. **Performance Reviewer** - Verifica tamanho, FPS
5. **Fallback Designer** - Cria GIF equivalente

## Integracao Padrao

```tsx
'use client'
import { Animation } from '@lottiefiles/react'

export function LottieHero() {
  return (
    <Animation
      src="/animations/hero.json"
      loop
      autoplay
      style={{ width: 400, height: 400 }}
      renderer="svg"
    />
  )
}
```

## Otimizacao

```tsx
// Lazy load
import { Player } from '@lottiefiles/react'
import { Suspense } from 'react'

export function LazyLottie() {
  return (
    <Suspense fallback={<div />}> 
      <Player src="/animations/hero.json" autoplay loop />
    </Suspense>
  )
}
```

## Fallback

```html
<img src="/animations/hero.gif" alt="Animacao Lottie" width="400" height="400" loading="lazy" />
```

## Performance Checklist

- [ ] JSON otimizado (< 500kB ideal, < 1MB max)
- [ ] Remover layers desnecessarios no After Effects
- [ ] Usar SVG renderer para nitidez
- [ ] Lazy load fora do viewport
- [ ] Fallback GIF para browsers antigos
