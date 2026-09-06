# tonejs

**Skill compactada — conteudo completo**
Fonte: `skills/tonejs/`

================================================================================

================================================================================
## 📄 SKILL.md
================================================================================

# Tone.js

## Manifesto

Audio interativo e sincronizado com animacoes usando Tone.js para web audio API simplificada.

## Stack

- tone (npm)
- Web Audio API (nativo)
- React/hooks (opcional)

## Keywords

tonejs, audio, web-audio, music, sound, interactive-audio, oscillator, synth, effect

## Visao Geral

Tone.js permite:
1. Sintetizar sons em tempo real
2. Tocar samples de audio
3. Sincronizar audio com animacoes
4. Criar experiencias audio-reactivas

## Como Usar

```js
import * as Tone from 'tone';

// Sintetizador
const synth = new Tone.Synth({
  oscillator: { type: 'sine' },
  envelope: { attack: 0.1, decay: 0.2, sustain: 0.5, release: 1 },
}).toDestination();

// Tocar nota
synth.triggerAttackRelease('C4', '8n');

// Sequenciador
const loop = new Tone.Loop((time) => {
  synth.triggerAttackRelease('C4', '8n', time);
  synth.triggerAttackRelease('E4', '8n', time + 0.25);
  synth.triggerAttackRelease('G4', '8n', time + 0.5);
}, '4n').start(0);

Tone.Transport.start();
```

## Audio Reativo

```js
// Analyzer para visualizacao
const meter = new Tone.Meter();
const player = new Tone.Player('sound.mp3').connect(meter).toDestination();

function animate() {
  const level = meter.value[0]; // 0-1
  // Usar level para animar visual
  requestAnimationFrame(animate);
}
animate();
```

## Sincronizacao com Animacao

```js
const synth = new Tone.Synth().toDestination();
const loop = new Tone.Loop((time) => {
  synth.triggerAttackRelease('C4', '8n', time);
  
  // Sincronizar com animacao GSAP
  gsap.to('.circle', {
    scale: 1.5,
    duration: 0.25,
    yoyo: true,
    repeat: 1,
  });
}, '4n').start(0);

Tone.Transport.start();
```

## Metricas de Sucesso

- Audio sem glitches
- Sincronizacao precisa com animacoes
- Latencia baixa (< 50ms)
- Suporte a todos os navegadores modernos

