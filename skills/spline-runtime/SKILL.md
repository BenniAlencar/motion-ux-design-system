---
name: spline-runtime
description: Spline 3D + Runtime Viewer
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - spline
    - 3d
    - spline-3d
    - runtime
  routes:
    - spatial
depends_on:
  - cerebro-orquestrador
  - r3f-threejs-drei
outputs:
  - spline_integration
  - fallback_poster
  - performance_report
---

# Spline Runtime Viewer

## Stack

- @splinetool/runtime
- @splinetool/react
- Fallback HTML/CSS

## Enxame de Agentes

1. **Scene Analyst** - Avalia se Spline e adequado
2. **Asset Director** - Confere URL do Spline, direitos
3. **Integration Engineer** - Gera codigo React/Next
4. **Performance Reviewer** - Verifica load time, memory
5. **Fallback Designer** - Cria poster HTML equivalente

## Integracao Padrao

```tsx
'use client'
import { Spline } from '@splinetool/react'
import { Suspense } from 'react'

export function HeroSpline({ url }: { url: string }) {
  return (
    <div className="spline_container" style={{ position: 'relative', width: '100%', height: '60vh' }}>
      <Suspense fallback={<div className="spline_poster" />}> 
        <Spline scene={url} />
      </Suspense>
      {/* Fallback estatico */}
      <div className="spline_poster" aria-hidden="true" />
    </div>
  )
}
```

## Fallback Poster

```html
<div class="spline_poster">
  <img src="/hero-poster.jpg" alt="Descricao poetica da cena 3D" />
  <p class="sr-only">Animacao 3D interativa disponivel em browsers com WebGL</p>
</div>
```

## Performance Checklist

- [ ] URL do Spline otimizada (export com compressao)
- [ ] Lazy load com Suspense
- [ ] Poster estatico para SEO e a11y
- [ ] Testar load time em 3G
- [ ] Memory leak test (dispose no cleanup)
