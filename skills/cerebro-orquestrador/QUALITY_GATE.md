---
name: cerebro-quality-gate
version: 1.0.0
---

# Cerebro - Quality Gate

## Checklist de Qualidade

### Funcional

- [ ] Intent classification correta
- [ ] Skills selecionadas sao relevantes
- [ ] Execution plan tem ordem logica
- [ ] Dependencies entre steps estao corretas
- [ ] Asset gate identifica todos assets faltantes

### Performance

- [ ] Response time < 500ms
- [ ] Memory usage < 100MB
- [ ] No loops infinitos na classificacao
- [ ] Cache de skills carregadas

### Accessibility

- [ ] Asset instructions sao claras e acessiveis
- [ ] Next action e compreensivel
- [ ] Warnings sao explicados claramente

### Motion

- [ ] Narrative tem ritmo adequado (intro, revelacao, climax)
- [ ] Scroll ranges fazem sentido (0-0.3, 0.3-0.7, 0.7-1.0)

### Visual

- [ ] Output YAML e bem formatado
- [ ] Exemplos sao claros
- [ ] Trace IDs sao unicos e legiveis

## Criterios de Aceitacao

### Pass

- Todas as secoes acima: pass
- No blocking issues
- Asset instructions claras
- Next action acionavel

### Pass with Warnings

- Todas as secoes acima: pass ou pass_with_warnings
- Warnings documentados
- No blocking issues

### Fail

- Qualquer secao: fail
- Blocking issues presentes
- Asset instructions incompletas

## Rollback Plan

Se quality gate falhar:

1. **Reverter para ultimo snapshot valido**
2. **Reduzir complexidade da classificacao**
3. **Simplificar narrative para padrao**
4. **Documentar gaps explicitamente**

## Evidence Packet

Para cada execucao, coletar:

```yaml
evidence:
  - type: intent_classification
    content: intent_classification object
  - type: skills_selected
    content: selected_skills array
  - type: execution_plan
    content: execution_plan array
  - type: asset_gate
    content: asset_gate_report object
  - type: quality_report
    content: quality_state object
  - type: snapshot
    content: run_snapshot object
```
