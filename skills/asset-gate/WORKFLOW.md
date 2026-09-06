---
name: asset-gate-workflow
version: 1.0.0
---

# Asset Gate - Workflow

## Passo 1: Receber Lista de Assets do Cerebro

```yaml
required_assets:
  - type: logo
    status: missing
    required_for: final_delivery
  - type: images
    status: missing
    count: 3
    required_for: final_delivery
  - type: fonts
    status: unknown
    required_for: final_delivery
```

## Passo 2: Asset Intake

Catalogar assets fornecidos:

```yaml
asset_inventory:
  logo:
    provided: false
    format: null
    size_kb: null
    license: null
  
  images:
    provided: false
    count: 0
    formats: []
    licenses: []
  
  fonts:
    provided: false
    names: []
    licenses: []
```

## Passo 3: Manifest Builder

Criar asset manifest:

```yaml
# asset_manifest.yaml
project: "Minha Landing"
version: 1.0.0
updated: "2026-09-05T23:30:00Z"

assets:
  logo:
    status: missing
    required_for: final_delivery
    specifications:
      format: [SVG, PNG]
      min_size: "500x500"
      background: transparent
      license: owned ou purchased
  
  images:
    - name: hero_background
      status: missing
      required_for: final_delivery
      specifications:
        format: JPG
        dimensions: "1920x1080"
        max_size_kb: 500
        style: "Iluminacao natural, fundo neutro, tons de azul e cinza"
        license: stock_purchased ou original
    
    - name: product_shot_1
      status: missing
      required_for: final_delivery
      specifications:
        format: PNG
        dimensions: "800x600"
        background: transparent
        style: "Produto isolado, iluminacao studio"
        license: original
    
    - name: product_shot_2
      status: missing
      required_for: final_delivery
      specifications:
        format: PNG
        dimensions: "800x600"
        background: transparent
        style: "Produto isolado, iluminacao studio"
        license: original
  
  fonts:
    - name: Inter
      status: recommended
      source: "Google Fonts"
      license: OFL (gratuito)
      usage: web
```

## Passo 4: Provenance Tracker

Rastrear origem e direitos:

```yaml
provenance:
  logo:
    source: "Aguardando envio do cliente"
    license: "A confirmar"
    digest: null
  
  images:
    hero_background:
      source: "Aguardando envio do cliente"
      license: "A confirmar (deve ser stock_purchased ou original)"
      digest: null
```

## Passo 5: Placeholder Designer

Criar placeholders quando assets faltam:

```yaml
placeholders:
  logo:
    path: "/assets/placeholder-logo.svg"
    type: svg
    style: "Retangulo cinza com texto 'LOGO'"
  
  images:
    hero_background:
      path: "/assets/placeholder-hero-bg.jpg"
      type: jpg
      style: "Gradiente azul-cinza"
    
    product_shot_1:
      path: "/assets/placeholder-product-1.png"
      type: png
      style: "Retangulo cinza com texto 'PRODUCT 1'"
    
    product_shot_2:
      path: "/assets/placeholder-product-2.png"
      type: png
      style: "Retangulo cinza com texto 'PRODUCT 2'"
```

## Passo 6: Rights Checker

Verificar licencas de uso:

```yaml
rights_check:
  logo:
    status: pending
    required_documentation: "Confirmacao de propriedade ou licenca de uso"
  
  images:
    hero_background:
      status: pending
      required_documentation: "Licenca stock ou comprovante de autoria"
    
    product_shot_1:
      status: pending
      required_documentation: "Comprovante de autoria (foto original do produto)"
    
    product_shot_2:
      status: pending
      required_documentation: "Comprovante de autoria (foto original do produto)"
```

## Passo 7: Gerar Asset Instructions

Criar instrucoes claras para o usuario:

```markdown
# Instrucoes de Assets - Minha Landing

Para entrega final, enviar os seguintes assets:

## 1. Logo

**Formato:** SVG ou PNG
**Tamanho minimo:** 500x500 pixels
**Fundo:** Transparente
**Licenca:** Propriedade da marca ou licenca de uso comercial

**Como enviar:**
- Upload em /assets/logo.svg ou /assets/logo.png
- Ou enviar por email para design@empresa.com

---

## 2. Imagens

### 2.1 Hero Background

**Formato:** JPG
**Dimensoes:** 1920x1080 pixels
**Tamanho maximo:** 500 kB
**Estilo:**
- Iluminacao natural
- Fundo neutro
- Paleta: tons de azul e cinza
- Evitar texto na imagem

**Sugestoes de busca (stock gratuito):**
- Unsplash: "minimal blue background"
- Pexels: "abstract blue gradient"
- Pixabay: "tech background blue"

---

### 2.2 Product Shot 1

**Formato:** PNG (fundo transparente)
**Dimensoes:** 800x600 pixels
**Estilo:**
- Produto isolado
- Iluminacao de studio
- Sem sombras fortes
- Angulo 3/4 ou frontal

**Como fazer:**
- Usar smartphone com boa iluminacao
- Fundo branco ou cinza claro
- Remover fundo com remove.bg ou Photoshop

---

### 2.3 Product Shot 2

(Mesmas especificacoes acima)

---

## 3. Fontes

**Recomendacao:** Inter (Google Fonts, gratuito)
**Link:** https://fonts.google.com/specimen/Inter
**Licenca:** OFL (Open Font License)

---

## Prazo

Enviar todos assets ate: [DATA]

## Dudas

Contato: design@empresa.com
```

## Passo 8: Atualizar Run Snapshot

Documentar no snapshot:

```yaml
run_snapshot:
  asset_state: asset_pending
  delivery_state: prototype
  blocking_assets:
    - type: logo
      status: missing
    - type: images
      status: missing
      count: 3
  asset_instructions_ref: "skills/asset-gate/ASSET_INSTRUCTIONS_TEMPLATE.md"
  next_action: "Aguardar logo e imagens para final delivery"
```
