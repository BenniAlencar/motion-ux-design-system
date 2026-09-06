---
name: asset-gate
description: Asset intake, manifest, provenance, rights, placeholder policy
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - asset
    - assets
    - logo
    - imagem
    - fonte
    - 3d
    - glb
    - spline
  routes:
    - quality
depends_on:
  - cerebro-orquestrador
outputs:
  - asset_manifest
  - asset_state
  - blocking_assets
  - placeholder_policy
  - provenance_report
---

# Asset Gate

## Stack

- Asset manifest YAML
- Provenance tracking
- Placeholder policy
- Rights check

## Enxame de Agentes

1. **Asset Intake** - Recebe e cataloga assets
2. **Manifest Builder** - Cria asset manifest
3. **Provenance Tracker** - Rastreia origem e direitos
4. **Placeholder Designer** - Cria placeholders quando assets faltam
5. **Rights Checker** - Verifica licencas de uso

## Asset Checklist

- [ ] Logo (SVG/PNG, min 500x500, fundo transparente)
- [ ] Copy real (nome, tagline, CTA, body copy)
- [ ] Imagens (direcao visual aprovada, min 1920x1080)
- [ ] Fontes (licenca ou alternativa livre)
- [ ] 3D/GLB (se aplicavel, otimizado < 10MB)
- [ ] Spline URL (se aplicavel, export otimizado)
- [ ] Rive/Lottie (se aplicavel, < 500kB)
- [ ] Video (se aplicavel, < 10MB, codec H.264)

## Asset Manifest Template

```yaml
# asset_manifest.yaml
project: Nome do Projeto
version: 1.0.0
updated: 2026-09-05

assets:
  logo:
    status: provided | pending | placeholder
    path: /assets/logo.svg
    format: SVG
    size_kb: 12
    license: owned
    usage: [web, print, social]
    
  images:
    - name: hero_bg
      status: provided
      path: /assets/hero-bg.jpg
      format: JPG
      size_kb: 450
      dimensions: 1920x1080
      license: stock_purchased
      
  fonts:
    - name: Inter
      status: provided
      source: Google Fonts
      license: OFL
      usage: web
      
  models_3d:
    - name: product_hero
      status: pending
      format: GLB
      required_for: final_delivery
      placeholder: /assets/product-poster.jpg
```

## Asset State

```yaml
asset_state:
  overall: provided | pending | placeholder_only
  delivery_state: final | prototype | blocked
  blocking_assets:
    - type: logo
      status: missing
      required_for: final_delivery
      impact: "Nao e possivel entregar versao final sem logo"
  placeholders_used:
    - type: image
      count: 3
      paths: ["/assets/placeholder-1.jpg"]
```

## Placeholder Policy

```yaml
placeholder_policy:
  strategy: explicit
  rules:
    - "Placeholders devem ser claramente identificados visualmente"
    - "Nao usar placeholders em producao sem aprovacao explicita"
    - "Sempre incluir asset_manifest com status de cada asset"
    - "Documentar assets pendentes no run_snapshot"
```

## Provenance

```yaml
provenance_report:
  assets:
    - name: logo.svg
      source: "Cliente via email 2026-09-01"
      license: "Propriedade do cliente"
      digest: sha256:abc123...
      
    - name: hero-bg.jpg
      source: "Unsplash (foto por @photographer)"
      license: "Unsplash License (gratuito para uso comercial)"
      url: https://unsplash.com/photos/...
      digest: sha256:def456...
```

## Output

```yaml
asset_gate_report:
  asset_state: asset_pending
  delivery_state: prototype
  blocking_assets:
    - type: logo
      status: missing
  placeholders_count: 3
  provenance_complete: true
  rights_all_cleared: false
  next_action: "Aguardar logo e aprovacao de imagens para final delivery"
```
