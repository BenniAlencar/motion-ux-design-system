# Manifesto Operacional — Motion/UX Design System

**Versao:** 1.0.0  
**Status:** Canunico  
**Aplicacao:** Todos os agentes, skills e workflows

---

## Principio Fundamental

> Este sistema existe para transformar solicitacoes de usuarios em entregas de alta qualidade (codigo + assets + evidence) de forma autonoma, usando todo o conhecimento tecnico disponivel.

---

## Regras Obrigatorias

### 1. Consulta Universal

**TODA** solicitacao deve consultar:

1. **Todas as skills** em `skills/*/SKILL.md`
2. **Todos os materiais** em `agentes-training/*.txt`
3. **Todos os agents** em `skills/*/AGENTS.md`

Nenhuma skill pode ser ignorada. Nenhum material pode ser pulado.

### 2. Classificacao de Intencao

**SEMPRE** classifique antes de executar:

- `hero_scroll` — Hero com scroll que revela conteudo
- `landing` — Landing page completa
- `hero_3d` — Hero com 3D, particulas, shaders
- `microinteraction` — Buttons, cards, hover effects
- `site_completo` — Site multi-page
- `page_transition` — Transicoes de pagina
- `generative` — Arte generativa, creative coding
- `audio_interactive` — Audio/visual interativo

### 3. Selecao de Skills

**SEMPRE** selecione baseado na intencao:

| Intencao | Primary | Secondary | Required |
|----------|---------|-----------|----------|
| hero_scroll | gsap-scrolltrigger | lenis, motion-framer | accessibility-a11y, performance-budget |
| hero_3d | r3f-threejs-drei | webgpu-gpgpu, lygia, spline-runtime | accessibility-a11y, performance-budget |
| landing | gsap-scrolltrigger | lenis, barba-swup | accessibility-a11y, performance-budget, seo-metadata |
| microinteraction | motion-framer | gsap-core, animejs | accessibility-a11y |
| generative | webgpu-gpgpu | p5js, rapier-physics | performance-budget |
| audio_interactive | tonejs | webaudio-api, p5js | accessibility-a11y, performance-budget |

### 4. Asset Gate

**SEMPRE** gere instrucoes claras de assets nao-codigo:

```markdown
Para entrega final, enviar:

1. Logo (SVG ou PNG, 500x500 min, fundo transparente)

2. Imagens:
   - Hero background (1920x1080, JPG, < 500kB)
   - Product shot 1 (800x600, PNG, fundo transparente)
   - Product shot 2 (800x600, PNG, fundo transparente)

3. Fontes: Inter (Google Fonts, gratuito)
```

### 5. Quality Gate

**SEMPRE** valide antes de entregar:

- [ ] Lighthouse performance >= 80
- [ ] Frame time p95 < 16ms
- [ ] WCAG AA contraste
- [ ] Keyboard navigation completa
- [ ] Reduced motion respeitado

### 6. Evidence Packet

**SEMPRE** colete evidencias:

- Screenshots (desktop + mobile)
- Lighthouse metrics
- Frame time metrics
- Bundle size
- Video demos (scroll, keyboard, reduced-motion)

---

## Workflow Universal

```
SOLICITACAO DO USUARIO
         │
         ▼
┌─────────────────────────────────┐
│ 1. CARREGAR TODAS AS SKILLS     │
│    skills/*/SKILL.md            │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 2. CARREGAR TREINAMENTO         │
│    agentes-training/*.txt       │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 3. CLASSIFICAR INTENCAO         │
│    hero_scroll, landing, etc.   │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 4. SELECIONAR SKILLS            │
│    Primary + Secondary + Required│
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 5. DELEGAR PARA AGENTS          │
│    Architect, Code, Asset,      │
│    Quality, Evidence            │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 6. CONSOLIDAR E ENTREGAR        │
│    Codigo + Assets + Evidence   │
└─────────────────────────────────┘
```

---

## Agents do Sistema

### ArchitectAgent
**Responsabilidade:** Estrutura do projeto, selecao de templates, setup.

### CodeAgent
**Responsabilidade:** Implementacao do codigo.

### AssetAgent
**Responsabilidade:** Instrucoes de assets nao-codigo.

### QualityAgent
**Responsabilidade:** Validacao de qualidade.

### EvidenceAgent
**Responsabilidade:** Coleta de metrics e screenshots.

---

## Materiais de Treinamento

**Obrigatorios:**

- `BENNI_MASTER_OS_V10_ARTE_SUPREMA_SEM_DEPENDENCIAS.txt`
- `BENNI_MASTER_OS_V10_ULTRA_200_PADROES.txt`
- `CODIGOS_SECRETOS_DOMINAM_TUDO_V11.txt`
- `PACOTE_DOMINA_TUDO_V11_FINAL.txt`
- `PACOTE_FINAL_DEDUPLICADO_V3.txt`
- `SHOPIFY_EDITIONS_WINTER26_ACIMA_AWWWARDS_LIMPO.txt`
- `SHOPIFY_EDITIONS_WINTER26_ULTRA_200_PADROES_LIMPO.txt`
- `GSAP_*.txt`, `SCROLLTRIGGER_*.txt`, `LENIS_*.txt`
- `THREEJS_*.txt`, `R3F_*.txt`, `DREI_*.txt`, `SHADERS_*.txt`
- `SPLINE_*.txt`, `RIVE_*.txt`, `LOTTIEFILES_*.txt`
- `BARBA_*.txt`, `SWUP_*.txt`, `PIXI_*.txt`, `OGL_*.txt`, `LYGIA_*.txt`
- `WEBGPU_*.txt`, `TONEJS_*.txt`, `RAPIER_*.txt`, `P5_*.txt`
- `ANIMEJS_*.txt`, `MOTION_*.txt`, `TEMPLATE_PREMIADO_*.txt`
- `LOCOMOTIVE_*.txt`, `THEATREJS_*.txt`

---

## Metricas de Sucesso

| Metrica | Target |
|---------|--------|
| Intent Accuracy | > 95% |
| Skill Relevance | > 90% |
| Training Material Coverage | 100% |
| Asset Detection | 100% |
| Lighthouse Performance | >= 80 |
| Frame Time p95 | < 16ms |
| WCAG AA Contrast | Pass |
| Response Time | < 500ms |
| User Clarity | > 4.5/5 |

---

## Exemplo de Execucao

**Input:**
```
"Quero um hero com scroll que revela produtos"
```

**Execucao:**

1. Carregar skills: gsap-scrolltrigger, lenis, accessibility-a11y, performance-budget
2. Carregar treinamento: GSAP_*.txt, LENIS_*.txt, SCROLLTRIGGER_*.txt
3. Classificar: `hero_scroll` (confidence: 0.98)
4. Selecionar: primary=gsap-scrolltrigger, secondary=lenis, required=[a11y, perf]
5. Delegar: ArchitectAgent → CodeAgent → AssetAgent → QualityAgent → EvidenceAgent
6. Entregar: codigo + asset instructions + evidence packet

**Output:**
```tsx
// src/components/Hero.tsx
import { useGSAP } from 'gsap-triggers'
import { useLenis } from '@studio-freight/lenis'

export default function Hero() {
  // implementacao completa
}
```

```markdown
## Asset Instructions

Para entrega final, enviar:
1. Logo (SVG ou PNG, 500x500 min)
2. Hero background (1920x1080, JPG)
3. Product shots (800x600, PNG)
```

```yaml
# Evidence Packet
delivery_state: prototype
quality_report:
  lighthouse_performance: 92
  wcag_aa_contrast: pass
```

---

## Rollback

Se algo falhar:
- Reverter para versao anterior deste manifesto
- Manter consulta de skills (obrigatorio)
- Manter classificacao de intencao (obrigatorio)
- Opcional: remover consulta de treinamento se causar lentidao

---

## Contato

**Owner:** Benni Alencar  
**Repositorio:** https://github.com/BenniAlencar/motion-ux-design-system

---

**FIM DO MANIFESTO**
