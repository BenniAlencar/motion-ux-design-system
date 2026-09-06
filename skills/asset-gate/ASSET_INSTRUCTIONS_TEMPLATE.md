---
name: asset-instructions-template
version: 1.0.0
---

# Asset Instructions Template

## Instrucoes de Assets - {{project_name}}

Para entrega final, enviar os seguintes assets:

{% if missing_logo %}
## 1. Logo

**Formato:** SVG ou PNG
**Tamanho minimo:** 500x500 pixels
**Fundo:** Transparente
**Licenca:** Propriedade da marca ou licenca de uso comercial

**Como enviar:**
- Upload em `/assets/logo.svg` ou `/assets/logo.png`
- Ou enviar por email para {{contact_email}}

**Dicas:**
- SVG e preferivel para escalabilidade
- PNG deve ter fundo transparente
- Evitar logos com fundo branco ou jpg

---
{% endif %}

{% if missing_images %}
## 2. Imagens

{% for image in missing_images %}
### {{image.name}}

**Formato:** {{image.format}}
**Dimensoes:** {{image.dimensions}}
{% if image.max_size_kb %}
**Tamanho maximo:** {{image.max_size_kb}} kB
{% endif %}
**Estilo:**
{{image.style | indent(2)}}

{% if image.stock_suggestions %}
**Sugestoes de busca (stock gratuito):**
{% for suggestion in image.stock_suggestions %}
- {{suggestion}}
{% endfor %}
{% endif %}

{% if image.how_to_create %}
**Como fazer:**
{{image.how_to_create | indent(2)}}
{% endif %}

---
{% endfor %}
{% endif %}

{% if missing_fonts %}
## 3. Fontes

{% for font in missing_fonts %}
### {{font.name}}

**Fonte:** {{font.source}}
**Licenca:** {{font.license}}
**Link:** {{font.url}}

{% endfor %}
{% endif %}

{% if missing_3d_models %}
## 4. Modelos 3D

{% for model in missing_3d_models %}
### {{model.name}}

**Formato:** {{model.format}} (GLB, GLTF, ou Spline URL)
**Tamanho maximo:** {{model.max_size_mb}} MB
**Especificacoes:**
{{model.specifications | indent(2)}}

**Como obter:**
{{model.how_to_obtain | indent(2)}}

---
{% endfor %}
{% endif %}

{% if missing_rive %}
## 5. Animacoes Rive

{% for rive in missing_rive %}
### {{rive.name}}

**Formato:** .riv
**Tamanho maximo:** {{rive.max_size_kb}} kB
**State machines:** {{rive.state_machines}}

**Como obter:**
{{rive.how_to_obtain | indent(2)}}

---
{% endfor %}
{% endif %}

{% if missing_lottie %}
## 6. Animacoes Lottie

{% for lottie in missing_lottie %}
### {{lottie.name}}

**Formato:** .json (Lottie)
**Tamanho maximo:** {{lottie.max_size_kb}} kB

**Como obter:**
{{lottie.how_to_obtain | indent(2)}}

---
{% endfor %}
{% endif %}

{% if missing_video %}
## 7. Videos

{% for video in missing_video %}
### {{video.name}}

**Formato:** MP4 (H.264)
**Dimensoes:** {{video.dimensions}}
**Duracao maxima:** {{video.max_duration_s}}s
**Tamanho maximo:** {{video.max_size_mb}} MB

**Como obter:**
{{video.how_to_obtain | indent(2)}}

---
{% endfor %}
{% endif %}

## Prazo

Enviar todos assets ate: **{{deadline}}**

## Dudas

Contato: **{{contact_email}}**

---

## Checklist de Envio

- [ ] Logo (SVG ou PNG, 500x500 min, fundo transparente)
{% for image in missing_images %}
- [ ] {{image.name}} ({{image.format}}, {{image.dimensions}})
{% endfor %}
{% if missing_fonts %}
- [ ] Fontes confirmadas
{% endif %}
{% if missing_3d_models %}
- [ ] Modelos 3D (GLB/Spline)
{% endif %}
{% if missing_rive %}
- [ ] Animacoes Rive
{% endif %}
{% if missing_lottie %}
- [ ] Animacoes Lottie
{% endif %}
{% if missing_video %}
- [ ] Videos (MP4 H.264)
{% endif %}

---

**Status atual:** {{asset_state}}
**Delivery:** {{delivery_state}}

{% if delivery_state == 'prototype' %}
**Nota:** Este projeto esta em modo **prototype** com placeholders. Para entrega final, todos assets acima devem ser fornecidos.
{% endif %}
