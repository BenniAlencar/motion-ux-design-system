# observer

**Skill compactada — conteudo completo**
Fonte: `skills/observer/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Observer

## Manifesto

Intersection Observer API para detectar visibilidade de elementos e triggerar animacoes quando entram na viewport.

## Stack

- IntersectionObserver API (nativo)
- GSAP ScrollTrigger (opcional)
- requestAnimationFrame

## Keywords

observer, intersection-observer, viewport, visibility, lazy-load, scroll-trigger

## Visao Geral

Observer permite:
1. Detectar quando elementos entram na viewport
2. Triggerar animacoes on-scroll
3. Lazy loading de imagens/videos
4. Analytics de visibilidade

## Como Usar

```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, {
  threshold: 0.1, // 10% visivel
  rootMargin: '0px 0px -100px 0px',
});

document.querySelectorAll('.animate-on-scroll').forEach(el => {
  observer.observe(el);
});
```

## Com GSAP

```js
gsap.utils.toArray('.animate').forEach(el => {
  gsap.from(el, {
    scrollTrigger: {
      trigger: el,
      start: 'top 80%',
      toggleActions: 'play none none none',
    },
    opacity: 0,
    y: 100,
  });
});
```

## Lazy Loading

```js
const imageObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      imageObserver.unobserve(img);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  imageObserver.observe(img);
});
```

## Metricas de Sucesso

- Deteccao precisa de visibilidade
- Animacoes triggeradas no momento certo
- Lazy loading funcionando
- Performance otimizada (sem scroll listeners)

