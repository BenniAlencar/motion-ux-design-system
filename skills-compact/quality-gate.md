# quality-gate

**Skill compactada — conteudo completo**
Fonte: `skills/quality-gate/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Quality Gate

## Manifesto

Gate de qualidade final validando performance, acessibilidade, SEO e best practices antes da entrega ao cliente.

## Stack

- Lighthouse CI
- Web Vitals
- Axe accessibility
- Bundle analyzer

## Keywords

quality, gate, lighthouse, accessibility, performance, seo, validation

## Visao Geral

Quality Gate valida:
1. Lighthouse scores
2. Acessibilidade WCAG
3. SEO metadata
4. Best practices

## Checklist de Qualidade

### Performance
- [ ] Lighthouse Performance >= 80
- [ ] FCP < 1.5s
- [ ] LCP < 2.5s
- [ ] CLS < 0.1
- [ ] FPS >= 60

### Acessibilidade
- [ ] Lighthouse Accessibility >= 90
- [ ] Navegacao por teclado
- [ ] Alt text em imagens
- [ ] Labels em inputs
- [ ] Contraste >= 4.5:1

### SEO
- [ ] Title tag unica
- [ ] Meta description
- [ ] Open Graph tags
- [ ] Favicon
- [ ] Sitemap.xml

### Best Practices
- [ ] HTTPS
- [ ] No console errors
- [ ] No console warnings
- [ ] Bundle size otimizado
- [ ] Images otimizadas

## Template de Quality Report

```yaml
quality_report:
  lighthouse:
    performance: 92
    accessibility: 95
    best_practices: 100
    seo: 98
  web_vitals:
    fcp: 1.2s
    lcp: 2.1s
    cls: 0.05
  accessibility:
    keyboard_navigation: pass
    screen_reader: pass
    contrast: pass
  performance:
    bundle_js: 180KB
    bundle_css: 45KB
    fps: 60
```

## Metricas de Sucesso

- Todos os checks passando
- Lighthouse >= 80 em todas as categorias
- Web Vitals dentro do target
- Zero errors/warnings

