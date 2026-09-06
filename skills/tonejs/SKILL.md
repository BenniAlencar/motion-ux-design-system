---
name: tonejs
description: Tone.js para audio e musica interativa no browser
version: 1.0.0
status: active
owner: Benni Alencar
activation:
  keywords:
    - tone.js
    - tonejs
    - audio
    - musica
    - web audio
  routes:
    - motion
depends_on:
  - cerebro-orquestrador
outputs:
  - audio_plan
  - synth_config
  - integration_code
---

# Tone.js

## Stack

- tone
- Web Audio API

## Enxame de Agentes

1. **Audio Analyst** - Analisa necessidades de audio
2. **Synth Designer** - Configura sintetizadores
3. **Sequencer Builder** - Cria sequencias
4. **Integration Engineer** - Gera codigo

## Sintetizador Basico

```ts
import * as Tone from 'tone'

const synth = new Tone.Synth({
  oscillator: { type: 'sine' },
  envelope: { attack: 0.1, decay: 0.2, sustain: 0.5, release: 1 },
}).toDestination()

// Tocar nota
synth.triggerAttackRelease('C4', '8n')

// Tocar com interacao
document.addEventListener('click', () => {
  synth.triggerAttackRelease('E4', '8n')
})
```

## Sequenciador

```ts
const seq = new Tone.Sequence((time, note) => {
  synth.triggerAttackRelease(note, '8n', time)
}, ['C4', 'E4', 'G4', 'B4', 'A4', 'F4', 'D4', 'E4']).start()

Tone.Transport.start()
Tone.Transport.bpm.value = 120
```

## Reverb e Effects

```ts
const reverb = new Tone.Reverb({ decay: 2, wet: 0.5 }).toDestination()
const delay = new Tone.FeedbackDelay('8n', 0.5).toDestination()

const synth = new Tone.Synth().connect(reverb).connect(delay)
```

## Audio com Scroll

```ts
import Lenis from 'lenis'
import * as Tone from 'tone'

const filter = new Tone.AutoFilter({
  frequency: '8n',
  baseFrequency: 200,
  octaves: 2.6,
}).toDestination()

const synth = new Tone.Synth().connect(filter)

const lenis = new Lenis()
lenis.on('scroll', ({ velocity }) => {
  filter.frequency.value = 200 + Math.abs(velocity) * 100
})
```

## Output

```yaml
tone_plan:
  synths:
    - type: Synth
      oscillator: sine
      envelope: { attack: 0.1, decay: 0.2, sustain: 0.5, release: 1 }
  effects: [Reverb, FeedbackDelay, AutoFilter]
  sequencer: true
  bpm: 120
  scroll_interaction: true
  integration: vanilla
```
