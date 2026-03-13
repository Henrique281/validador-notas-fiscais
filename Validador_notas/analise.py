def detectar_duplicadas(notas):

    numeros = set()
    duplicadas = []

    for nota in notas:

        if nota["numero"] in numeros:
            duplicadas.append(nota["numero"])

        numeros.add(nota["numero"])

    return duplicadas


def detectar_cnpj_suspeito(notas):

    suspeitos = []

    for nota in notas:

        if len(nota["cnpj"]) != 14:
            suspeitos.append(nota["numero"])

    return suspeitos


def detectar_valores_fora_media(notas):

    valores = [n["valor"] for n in notas]

    media = sum(valores) / len(valores)

    suspeitos = []

    for nota in notas:

        if nota["valor"] > media * 3:
            suspeitos.append(nota["numero"])

    return suspeitos


def estatisticas(notas):

    valores = [n["valor"] for n in notas]

    total = sum(valores)
    media = total / len(valores)
    maior = max(valores)

    return total, media, maior


def total_por_empresa(notas):

    empresas = {}

    for nota in notas:

        cnpj = nota["cnpj"]

        if cnpj not in empresas:
            empresas[cnpj] = 0

        empresas[cnpj] += nota["valor"]

    return empresas