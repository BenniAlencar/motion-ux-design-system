---
name: motion-framer
description: Framer Motion para animacoes React com spring e layout
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - framer motion
    - motion
    - react animation
    - spring
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
outputs:
  - motion_plan
  - spring_config
  - integration_code
---

# Framer Motion

## Stack

- framer-motion
- React

## Enxame de Agentes

1. **Motion Analyst** - Analisa animacoes necessarias
2. **Spring Designer** - Configura spring physics
3. **Layout Planner** - Planeja layout animations
4. **Integration Engineer** - Gera codigo React

## Animacao Simples

```tsx
import { motion } from 'framer-motion'

export function FadeIn({ children }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: 'easeOut' }}
    >
      {children}
    </motion.div>
  )
}
```

## Spring (Linear-style)

```tsx
import { motion, useSpring, useTransform } from 'framer-motion'

export function SpringButton() {
  const [props, api] = useSpring(() => ({
    scale: 1,
    rotate: 0,
    config: { tension: 300, friction: 20 },
  }))

  return (
    <motion.button
      style={props}
      onHoverStart={() => api.start({ scale: 1.05, rotate: 2 })}
      onHoverEnd={() => api.start({ scale: 1, rotate: 0 })}
    >
      Clique
    </motion.button>
  )
}
```

## Layout Animation

```tsx
import { motion, LayoutGroup } from 'framer-motion'

export function Accordion() {
  const [open, setOpen] = useState(false)
  
  return (
    <LayoutGroup>
      <motion.div layout onClick={() => setOpen(!open)}>
        <motion.div layoutId="header">Titulo</motion.div>
        {open && (
          <motion.div
            layout
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            Conteudo
          </motion.div>
        )}
      </motion.div>
    </LayoutGroup>
  )
}
```

## Scroll Animations

```tsx
import { motion, useScroll, useTransform } from 'framer-motion'

export function ParallaxHero() {
  const { scrollY } = useScroll()
  const y = useTransform(scrollY, [0, 500], [0, -100])
  const opacity = useTransform(scrollY, [0, 300], [1, 0])
  
  return (
    <motion.section style={{ y, opacity }}>
      <h1>Hero</h1>
    </motion.section>
  )
}
```

## Output

```yaml
motion_plan:
  animations:
    - type: fade_in
      duration: 0.5
      ease: easeOut
    - type: spring_button
      tension: 300
      friction: 20
    - type: parallax_scroll
      scroll_range: [0, 500]
      y_range: [0, -100]
  integration: react
  layout_group: true
```
