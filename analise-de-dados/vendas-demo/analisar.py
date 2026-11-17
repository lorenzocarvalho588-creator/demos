"""Resumo reproduzível de vendas fictícias."""

import csv
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


ARQUIVO = Path(__file__).with_name("pedidos.csv")


def moeda(valor: Decimal) -> str:
    return f"R$ {valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")


def analisar():
    receita_por_canal = defaultdict(Decimal)
    receita_por_categoria = defaultdict(Decimal)
    custo_por_categoria = defaultdict(Decimal)
    receita_total = Decimal("0")
    valor_cancelado = Decimal("0")
    concluidos = 0
    cancelados = 0

    with ARQUIVO.open(newline="", encoding="utf-8") as arquivo:
        for pedido in csv.DictReader(arquivo):
            receita = Decimal(pedido["receita"])
            custo = Decimal(pedido["custo"])
            if pedido["status"] == "cancelado":
                cancelados += 1
                valor_cancelado += receita
                continue
            if pedido["status"] != "concluido":
                raise ValueError(f"Status desconhecido: {pedido['status']}")

            concluidos += 1
            receita_total += receita
            receita_por_canal[pedido["canal"]] += receita
            receita_por_categoria[pedido["categoria"]] += receita
            custo_por_categoria[pedido["categoria"]] += custo

    print(f"Pedidos concluídos: {concluidos}")
    print(f"Faturamento: {moeda(receita_total)}")
    print(f"Pedidos cancelados: {cancelados} ({moeda(valor_cancelado)})")
    print("\nReceita por canal:")
    for canal, receita in sorted(receita_por_canal.items(), key=lambda item: item[1], reverse=True):
        print(f"  {canal}: {moeda(receita)}")
    print("\nMargem bruta por categoria:")
    margens = {
        categoria: receita - custo_por_categoria[categoria]
        for categoria, receita in receita_por_categoria.items()
    }
    for categoria, margem in sorted(margens.items(), key=lambda item: item[1], reverse=True):
        print(f"  {categoria}: {moeda(margem)}")


if __name__ == "__main__":
    analisar()
