# Simulação de ECG com filtro passa-baixa

Bem-vindo! Este repositório contém uma pequena simulação de sinal de ECG com ruído e aplicação de um filtro passa-baixa simples, implementada em `simulation.py`.

**Visão geral**
- **O que o código faz:** Gera um sinal simulado que representa batimentos cardíacos (senoidal) somados a um ruído senoidal. Em seguida, aplica um filtro passa-baixa exponencial (filtro do tipo média móvel exponencial) para reduzir o ruído e plota o sinal original e o sinal filtrado.

**Principais pontos do `simulation.py`**
- `N`: número de amostras (padrão = 100).
- `ALPHA`: coeficiente do filtro passa-baixa (padrão = 0.1). Valores menores suavizam mais o sinal.
- Geração do sinal: usa funções trigonométricas de `math` para criar batimento e ruído.
- Filtro: implementação simples recursiva do filtro exponencial: `y[i] = ALPHA * x[i] + (1 - ALPHA) * y[i-1]`.
- Visualização: usa `matplotlib` para traçar o ECG bruto (com ruído) e o ECG filtrado.

**Tecnologias e bibliotecas usadas**
- Python (recomendado 3.8+)
- Biblioteca padrão: `math` (cálculo de seno e constantes)
- `matplotlib` — para plotagem e visualização dos sinais

Instalação rápida das dependências:

```
pip install matplotlib
```

Como executar a simulação:

```
python simulation.py
```

Ao executar, uma janela de plot será exibida mostrando o ECG bruto (linha tracejada vermelha) e o ECG filtrado (linha contínua azul). Ajuste `N` e `ALPHA` dentro de `simulation.py` para experimentar diferentes resoluções e níveis de suavização.

**Sugestões de experimentos**
- Tentar diferentes valores de `ALPHA` (ex.: 0.01, 0.05, 0.2) para ver o efeito do filtro.
- Aumentar `N` para observar comportamento em janelas maiores.
- Substituir o ruído por ruído aleatório (ex.: `random.uniform`) para testar robustez.

Se quiser, eu posso:
- Rodar a simulação aqui e mostrar a figura gerada.
- Adicionar um pequeno script que salve a figura como PNG.

---
Autor: Antonio Pereira - Simulação educativa de sinais biomédicos
