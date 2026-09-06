# asset-gate

**Skill compactada — conteudo completo**
Fonte: `skills/asset-gate/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Asset Gate

## Manifesto

Gate para assets (imagens, logos, fonts, videos) garantindo qualidade, formato e tamanho adequados antes da entrega final.

## Stack

- Image optimization (Sharp, Squoosh)
- Font loading (Google Fonts, self-hosted)
- Asset validation

## Keywords

asset, image, font, logo, optimization, validation, quality-gate

## Visao Geral

Asset Gate garante:
1. Imagens otimizadas
2. Fonts carregando corretamente
3. Logos em alta qualidade
4. Assets validados antes da entrega

## Checklist de Assets

### Logo
- [ ] SVG ou PNG com fundo transparente
- [ ] Minimo 500x500px
- [ ] Versao clara e escura

### Imagens
- [ ] Hero background: 1920x1080, JPG, < 500KB
- [ ] Product shots: 800x600, PNG, fundo transparente
- [ ] Thumbnails: 400x300, WebP, < 100KB

### Fonts
- [ ] Google Fonts ou self-hosted
- [ ] Preload para fonts criticas
- [ ] Fallbackfonts definidas

## Template de Asset Instructions

```markdown
Para entrega final, enviar:

1. Logo (SVG ou PNG, 500x500 min, fundo transparente)

2. Imagens:
   - Hero background (1920x1080, JPG, < 500kB)
   - Product shot 1 (800x600, PNG, fundo transparente)
   - Product shot 2 (800x600, PNG, fundo transparente)

3. Fontes: Inter (Google Fonts, gratuito)
```

## Otimizacao

```bash
# Comprimir imagens
npx imagemin images/* --out-dir=images-optimized

# Converter para WebP
npx @squoosh/cli input.png output.webp --webp '{"quality":80}'
```

## Metricas de Sucesso

- Todos os assets presentes
- Imagens otimizadas (< 500KB cada)
- Fonts carregando rapidamente
- Logo em alta qualidade

