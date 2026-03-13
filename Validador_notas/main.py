import os
import csv

from Validador_notas.leitor_xml import ler_nota
from Validador_notas.analise import *

pasta = "notas"
saida = "resultado/relatorio.csv"

notas = []

for arquivo in os.listdir(pasta):

    caminho = os.path.join(pasta, arquivo)

    nota = ler_nota(caminho)

    notas.append(nota)

duplicadas = detectar_duplicadas(notas)
cnpj_suspeito = detectar_cnpj_suspeito(notas)
valores_suspeitos = detectar_valores_fora_media(notas)

total, media, maior = estatisticas(notas)

empresas = total_por_empresa(notas)

dados = []

for nota in notas:

    status = []

    if nota["numero"] in duplicadas:
        status.append("duplicada")

    if nota["numero"] in cnpj_suspeito:
        status.append("cnpj suspeito")

    if nota["numero"] in valores_suspeitos:
        status.append("valor suspeito")

    if not status:
        status = ["OK"]

    dados.append([
        nota["numero"],
        nota["cnpj"],
        nota["valor"],
        "; ".join(status)
    ])

with open(saida, "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow(["numero", "cnpj", "valor", "status"])

    writer.writerows(dados)

print("\nRELATÓRIO GERADO\n")

print("Total faturado:", total)
print("Média das notas:", media)
print("Maior nota:", maior)

print("\nFaturamento por empresa:\n")

for cnpj, valor in empresas.items():

    print(cnpj, "->", valor)

print("\nArquivo salvo em:", saida)