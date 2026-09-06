# performance-budget

**Skill compactada — conteudo completo**
Fonte: `skills/performance-budget/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Performance Budget

## Manifesto

Otimizacao de performance com limites de budget para garantir experiencias web rapidas e responsivas.

## Stack

- Lighthouse
- Web Vitals
- Bundle analyzers
- Performance monitoring

## Keywords

performance, budget, optimization, lighthouse, web-vitals, bundle-size, fps

## Visao Geral

Performance Budget garante:
1. Bundle size limitado
2. Lighthouse score alto
3. Web Vitals dentro do target
4. FPS constante

## Budgets Recomendados

| Metrica | Target | Como Medir |
|---------|--------|------------|
| Bundle JS | < 200KB | Webpack bundle analyzer |
| Bundle CSS | < 50KB | PurgeCSS |
| Lighthouse Performance | >= 90 | Lighthouse CI |
| FCP | < 1.5s | Web Vitals |
| LCP | < 2.5s | Web Vitals |
| CLS | < 0.1 | Web Vitals |
| FPS | >= 60 | Chrome DevTools |
| Frame Time p95 | < 16ms | Performance panel |

## Otimizacoes

```js
// Code splitting
const HeavyComponent = lazy(() => import('./HeavyComponent'));

// Image optimization
<img src="image.avif" alt="..." loading="lazy" />

// Font optimization
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preload" href="/font.woff2" as="font" type="font/woff2" crossorigin />
```

## Monitoring

```js
import { onCLS, onFCP, onLCP } from 'web-vitals';

onCLS(console.log);
onFCP(console.log);
onLCP(console.log);
```

## Metricas de Sucesso

- Lighthouse >= 90
- Web Vitals dentro do target
- Bundle size sob controle
- FPS constante a 60

