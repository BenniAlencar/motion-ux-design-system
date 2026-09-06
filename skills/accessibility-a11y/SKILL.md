---
name: accessibility-a11y
description: WCAG, keyboard navigation, focus, screen reader, reduced-motion
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - accessibility
    - a11y
    - wcag
    - keyboard
    - focus
    - screen reader
  routes:
    - quality
depends_on:
  - cerebro-orquestrador
outputs:
  - a11y_audit
  - keyboard_plan
  - focus_styles
  - reduced_motion_css
  - sr_text
---

# Accessibility A11y

## Stack

- WCAG 2.2 AA/AAA
- Keyboard navigation
- Focus visible
- Screen reader text
- Reduced motion

## Enxame de Agentes

1. **A11y Auditor** - Audita contraste, estrutura, labels
2. **Keyboard Designer** - Planeja navegacao por teclado
3. **Focus Stylist** - Cria focus visible styles
4. **SR Writer** - Escreve texto para screen reader
5. **Motion Designer** - Cria reduced-motion variants

## Checklist WCAG AA

- [ ] Contraste 4.5:1 texto normal, 3:1 texto grande
- [ ] Focus visible em todos elementos interativos
- [ ] Keyboard navigation completa (Tab, Enter, Space, Arrow)
- [ ] Alt text em imagens, aria-label em icones
- [ ] Estrutura de headings logica (h1 -> h2 -> h3)
- [ ] Skip link para conteudo principal
- [ ] Reduced motion respeitado

## Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  
  /* Manter essencia visual sem motion */
  .hero_halo {
    animation: none;
    opacity: 0.2;
    transform: scale(1);
  }
}
```

## Focus Visible

```css
:focus-visible {
  outline: 2px solid var(--focus-ring, #00ffff);
  outline-offset: 2px;
}

:focus:not(:focus-visible) {
  outline: none;
}
```

## Skip Link

```html
<a href="#main-content" class="skip-link">Pular para conteudo principal</a>

<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  padding: 8px;
  z-index: 100;
}
.skip-link:focus {
  top: 0;
}
</style>
```

## Output

```yaml
a11y_audit:
  contrast: pass
  keyboard: pass
  focus_visible: pass
  sr_text: pass
  reduced_motion: pass
  issues:
    - severity: warning
      description: "Contraste 4.2:1 em texto secundario (minimo 4.5:1)"
      fix: "Escurecer cor para #666"
```
