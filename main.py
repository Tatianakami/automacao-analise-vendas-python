import pandas as pd
import numpy as np

dados = pd. read_csv("excel/vendas.csv")
print("dados da planilha")
print(dados)

valores = dados["valor"]

total = valores.sum()
print("total de valores")
print(total)

#criar nova coluna com aumento de 10%
dados["valor_com_aumento"]  =  dados["valor"] * 1.1
dados.to_csv("excel/resultado.csv", index=False)
print("arquivo resultado.csv criado com sucesso")

# Filtrar produtos com valor maior que 100
caros = dados[dados["valor"] > 100]

print("\nProdutos com valor maior que 100:")
print(caros)

# Salvar
caros.to_csv("excel/produtos_caros.csv", index=False)

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.bar(dados["produto"], dados["valor"])

plt.title("Relatório de Vendas por Produto", fontsize=14)
plt.xlabel("Produto", fontsize=12)
plt.ylabel("Valor (R$)", fontsize=12)

plt.grid(axis='y')

plt.savefig("excel/grafico_vendas.png")

plt.show()