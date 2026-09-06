# accessibility-a11y

**Skill compactada — conteudo completo**
Fonte: `skills/accessibility-a11y/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Accessibility A11y

## Manifesto

Acessibilidade WCAG AA para garantir que experiencias web sejam usaveis por todas as pessoas, incluindo aquelas com deficiencias.

## Stack

- HTML semantico
- ARIA attributes
- Keyboard navigation
- Screen reader testing

## Keywords

accessibility, a11y, wcag, aria, keyboard, screen-reader, semantic-html

## Visao Geral

A11y garante:
1. Navegacao por teclado
2. Leitura por screen readers
3. Contraste de cores adequado
4. HTML semantico

## Checklist WCAG AA

- [ ] Todo elemento interativo focavel por teclado
- [ ] Focus visible em todos os elementos
- [ ] Alt text em todas as imagens
- [ ] Labels em todos os inputs
- [ ] Contraste >= 4.5:1 para texto
- [ ] Reduced motion respeitado
- [ ] Skip links para navegacao
- [ ] Landmarks HTML (header, main, footer)

## Exemplo de Codigo

```tsx
// Botao acessivel
<button
  onClick={handleClick}
  onKeyDown={handleKeyDown}
  aria-label="Close modal"
  className="close-button"
>
  <span className="sr-only">Close</span>
  <svg aria-hidden="true">...</svg>
</button>

// Imagem com alt
<img src="hero.jpg" alt="Hero section showing products" />

// Input com label
<label htmlFor="email">Email</label>
<input id="email" type="email" aria-describedby="email-help" />
<span id="email-help">We'll never share your email</span>
```

## Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

```js
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReducedMotion) {
  // Animacoes normais
} else {
  // Animacoes minimas ou nenhuma
}
```

## Metricas de Sucesso

- Lighthouse accessibility >= 90
- Navegacao por teclado completa
- Screen reader lendo todo conteudo
- Contraste passando testes

