# MISSION CONTROL AI
***Nome da Missão:*** Projeto Aurora  
***Nome da Equipe:*** Equipe Netuno

Sistema em Python que simula o monitormaneto inteligente de uma missão espacial experimental, analisando ciclos de dados e gerando relatórios automáticos de risco. 

---

## Descrição
O **Mission Control AI** lê uma matriz de dados simuldados da missão (`dados_missao`) com 6 ciclos de monitoramento. Em cada ciclo, 5 parâmetros são analisados individualmente, recebem uma classificação de risco (NORMAL / ATENÇÃO / CRÍTICO) e uma pontuação. O sistema então:
* classifica o status geral de cada ciclo;
* gera recomendações automáticas para itens críticos;
* calcula a tendência da missão (melhora / piora / estável);
* identifica a área mais afetada ao longo de todos os ciclos;
* exibe um relatório final completo no terminal
---
## Estrutura do Repositório
```
mission-control-ai/
│  
├── README.md  
└── mission_control.py  
```
---
## Como Executar
Requisito: Python 3.8 ou superior
```
python mission_control.py
```
---
## Estrutura dos Dados
Matriz `dados_missao`  
Cada linha representa um ciclo; cada coluna, um parâmetro:

| **Posição** | **Parâmetro** | **Unidade** |
|:-----------:|---------------|:-----------:|
|      0      | Temperatura   |     ºC      |
|      1      | Comunicação   |      %      |
|      2      | Bateria       |      %      |
|      3      | Oxigênio      |      %      |
|      4      | Estabilidade  |      %      |

## Regras de Alerta

**Temperatura (ºC)**

| **Condição** | **Classificação** |
| ---------- | ---------- |
| menor que 18 °C | ATENÇÃO |
| de 18 °C até 30 °C | NORMAL |
| maior que 30 °C até 35 °C | ATENÇÃO |
| maior que 35 °C | CRÍTICO |

**Comunicação (%)**

| **Condição** | **Classificação** |
| ---------- | ---------- |
| menor que 30% | CRÍTICO |
| de 30% até 59% | ATENÇÃO |
| 60% ou mais | NORMAL |

**Bateria (%)**

| **Condição** | **Classificação** |
| ---------- | ---------- |
| menor que 20% | CRÍTICO |
| de 20% até 49% | ATENÇÃO |
| 50% ou mais | NORMAL |

**Oxigênio (%)**

| **Condição** | **Classificação** |
| ---------- | ---------- |
| menor que 80% | CRÍTICO |
| de 80% até 89% | ATENÇÃO |
| 90% ou mais | NORMAL |

**Estabilidade (%)**

| **Condição** | **Classificação** |
| ---------- | ---------- |
| menor que 40% | CRÍTICO |
| de 40% até 69% | ATENÇÃO |
| 70% ou mais | NORMAL |

## Pontuação de Risco

| **Classificação** | **Pontos** |
|-------------------|:----------:|
| NORMAL            |     0      |
| ATENÇÃO           |     1      |
| CRÍTICO           |     2      |

Pontuação máxima por ciclo: **10 pontos** (5 parâmetros * 2)

---

## Classificação do Ciclo
| **Pontuação Total** | **Status**        |
|:-------------------:|-------------------|
|        0 - 2        | MISSÃO ESTÁVEL    |
|        3 - 5        | MISSÃO EM ATENÇÃO |
|       6 - 10        | MISSÃO CRÍTICA    |

## Funções Principais
| **Função**                     | **Descrição**                                  |
|--------------------------------|------------------------------------------------|
| `analisar_temperatura(valor)`  | Classifica a temperatura e retorna pontuação   |
| `analisar_comunicacao(valor)`  | Classifica a comunicação e retorna pontuação   |
| `analisar_bateria(valor)`      | Classifica a bateria e retorna pontuação       |
| `analisar_oxigenio(valor)`     | Classifica o oxigenio e retorna pontuação      |
| `analisar_estabilidade(valor)` | Classifica a estabilidade e retorna pontuação  |
| `classificar_ciclo(pts)`       | Converte pontuação total em status do ciclo    |
| `analisar tendencia(r0, rf)`   | Compara primeiro e último ciclo para tendência |
| `area_mais_afetada`            | Retorna a área com maior acúmulo de risco      |
| `gerar_recomendacoes(alertas)` | Gera recomendações para itens CRÍTICO          |
| `gerar_relatorio_final(dados)` | Faz a análise e imprime o relatório            |

---

## Exemplo de Saída

```
==============================================================
 MISSION CONTROL AI | Projeto Aurora
 Equipe: Equipe Netuno
==============================================================

 CICLO 1
--------------------------------------------------------------
 Parametro                         valor Status
--------------------------------------------------------------
 Temperatura interna                24ºC NORMAL
 Comunicacao com a base              92% NORMAL
 Sistema de energia                  88% NORMAL
 Suporte de oxigenio                 96% NORMAL
 Estabilidade operacional            90% NORMAL
--------------------------------------------------------------
 Pontuacao de risco: 0/10   ->   MISSAO ESTAVEL
 
 ...
 (Outros Ciclos)
 ...
 
==============================================================
 RESUMO GERAL DA MISSAO
==============================================================
 
 Tendencia da missao:
 A missao apresentou tendencia de PIORA

 Area mais afetada: Temperatura interna (6 pontos acumulados)

 Pontuacao acumulada por area:
 Ciclo 1:  0/10  
 Ciclo 2:  0/10  
 Ciclo 3:  1/10  ■
 Ciclo 4:  6/10  ■■■■■■
 Ciclo 5: 10/10  ■■■■■■■■■■
 Ciclo 6:  5/10  ■■■■■

==============================================================
 Relatorio concluido!
==============================================================
```