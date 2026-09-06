# flip

**Skill compactada — conteudo completo**
Fonte: `skills/flip/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Flip

## Manifesto

Animacoes FLIP (First Last Invert Play) para transicoes de layout suaves e animacoes de lista/grid.

## Stack

- gsap + Flip (plugin GSAP)
- CSS transforms
- requestAnimationFrame

## Keywords

flip, flipp-animation, layout-transition, list-animation, grid-animation, reordering

## Visao Geral

FLIP permite:
1. Animar mudancas de layout
2. Transicoes de lista/grid
3. Reordenacao de elementos
4. Expand/collapse animacoes

## Como Usar

```js
import { gsap } from 'gsap';
import Flip from 'gsap/Flip';

gsap.registerPlugin(Flip);

// Salvar estado inicial
const state = Flip.getState('.items');

// Fazer mudanca de layout
items.forEach(item => {
  item.style.order = Math.floor(Math.random() * items.length);
});

// Animar transicao
Flip.from(state, {
  duration: 0.5,
  ease: 'power1.inOut',
  stagger: 0.1,
});
```

## Expand/Collapse

```js
const state = Flip.getState('.card');

card.classList.toggle('expanded');

Flip.from(state, {
  duration: 0.3,
  ease: 'power2.inOut',
  props: { borderRadius: true },
});
```

## Lista Animada

```js
const state = Flip.getState('li');

// Adicionar/remover itens
list.appendChild(newItem);
oldItem.remove();

Flip.from(state, {
  duration: 0.5,
  stagger: 0.05,
  ease: 'back.out(1.7)',
});
```

## Metricas de Sucesso

- Transicoes suaves a 60fps
- Layout animado corretamente
- Stagger funcionando
- Sem layout shift visivel

