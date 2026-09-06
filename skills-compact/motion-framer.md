# motion-framer

**Skill compactada — conteudo completo**
Fonte: `skills/motion-framer/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Motion / Framer Motion

## Manifesto

Biblioteca de animacao para React com API declarativa baseada em componentes para microinteracoes e animacoes complexas.

## Stack

- framer-motion (npm)
- React
- CSS transforms

## Keywords

motion, framer-motion, react, animation, microinteraction, gesture, spring

## Visao Geral

Framer Motion permite:
1. Animacoes declarativas em React
2. Gestos (hover, tap, drag)
3. Spring physics
4. Layout animations

## Como Usar

```tsx
import { motion } from 'framer-motion';

function Box() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 100 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      whileHover={{ scale: 1.1 }}
      whileTap={{ scale: 0.9 }}
    >
      Animated Box
    </motion.div>
  );
}
```

## Gestos

```tsx
<motion.div
  drag
  dragConstraints={{ left: 0, right: 100, top: 0, bottom: 100 }}
  onDragEnd={() => console.log('Dragged!')}
>
  Draggable
</motion.div>
```

## Layout Animations

```tsx
<motion.layout
  layout
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  exit={{ opacity: 0 }}
>
  {items.map(item => (
    <motion.div key={item.id} layout>
      {item.name}
    </motion.div>
  ))}
</motion.layout>
```

## Spring Physics

```tsx
<motion.div
  animate={{ x: 100 }}
  transition={{ type: 'spring', stiffness: 300, damping: 30 }}
/>
```

## Metricas de Sucesso

- Animacoes a 60fps
- Gestos respondendo
- Layout animations suaves
- Spring physics natural

