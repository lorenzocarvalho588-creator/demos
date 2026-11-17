# Análise de vendas fictícias

Uma demonstração pequena e reproduzível de análise de dados. O conjunto de pedidos é **fictício** e foi criado apenas para mostrar o processo.

## Perguntas

1. Qual foi o faturamento dos pedidos concluídos?
2. Qual canal trouxe mais receita?
3. Qual categoria teve a maior margem bruta?
4. Quanto valor foi cancelado?

## Como executar

Na raiz deste repositório:

```bash
python3 analise-de-dados/vendas-demo/analisar.py
```

O script usa apenas a biblioteca padrão do Python. Ele lê [pedidos.csv](pedidos.csv), separa pedidos concluídos dos cancelados e imprime os indicadores. Os valores monetários estão em reais.

## Resultado da amostra

| Indicador | Valor |
| --- | ---: |
| Pedidos concluídos | 14 |
| Faturamento | R$ 6.400,00 |
| Canal com maior receita | Site, R$ 2.900,00 |
| Categoria com maior margem bruta | Serviços, R$ 2.960,00 |
| Pedidos cancelados | 2, somando R$ 640,00 |

## Leitura dos resultados

O canal com maior receita mostra onde houve mais faturamento neste exemplo; não prova que ele seja o mais rentável para aquisição de clientes. A margem bruta é receita menos custo informado no arquivo e não inclui despesas operacionais, impostos ou marketing. Pedidos cancelados são mostrados separadamente e não entram no faturamento.
