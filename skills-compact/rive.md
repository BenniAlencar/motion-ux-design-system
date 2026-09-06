# rive

**Skill compactada — conteudo completo**
Fonte: `skills/rive/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Rive

## Manifesto

Animacoes interativas e state-driven usando Rive (rive.app) para microinteracoes complexas com logica de estado.

## Stack

- @rive-app/react (React)
- rive-web (vanilla JS)
- Rive Editor (criacao)

## Keywords

rive, animation, interactive, state-machine, rive-app, microinteraction, game-like

## Visao Geral

Rive permite:
1. Criar animacoes com state machines
2. Responder a inputs do usuario
3. Animacoes game-like complexas
4. Arquivos extremamente leves (< 100KB)

## Como Usar (React)

```tsx
import { useRive, useStateMachineInput } from '@rive-app/react';

function App() {
  const { RiveComponent } = useRive({
    src: 'animation.riv',
    stateMachines: ['State Machine 1'],
    layout: { fit: 'contain' },
  });

  const hoverInput = useStateMachineInput('hover', 'boolean', false);

  return (
    <div
      onMouseEnter={() => hoverInput.value = true}
      onMouseLeave={() => hoverInput.value = false}
    >
      <RiveComponent />
    </div>
  );
}
```

## Como Usar (Vanilla)

```js
import { Rive, Layout, Fit } from '@rive-app/canvas';

const rive = new Rive({
  src: 'animation.riv',
  canvas: document.getElementById('canvas'),
  stateMachines: ['State Machine 1'],
  layout: new Layout({ fit: Fit.Contain }),
});

// Inputs
const hoverInput = rive.stateMachineInput('hover');
hoverInput.value = true;

// Events
rive.on('stateChange', (event) => {
  console.log('State:', event.data);
});
```

## State Machines

Rive suporta:
- Boolean inputs (hover, active)
- Number inputs (progress, speed)
- Trigger inputs (click, jump)
- Transicoes condicionais
- Animacoes blendadas

## Metricas de Sucesso

- Arquivo .riv < 100KB
- Resposta instantanea a inputs
- State machine logica clara
- Animacoes suaves a 60fps

