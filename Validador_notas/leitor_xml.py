import xml.etree.ElementTree as ET

def ler_nota(caminho):

    tree = ET.parse(caminho)
    root = tree.getroot()

    numero = ""
    cnpj = ""
    valor = 0

    for elem in root.iter():

        if "nNF" in elem.tag:
            numero = elem.text

        if "CNPJ" in elem.tag:
            cnpj = elem.text

        if "vNF" in elem.tag:
            valor = float(elem.text)

    return {
        "numero": numero,
        "cnpj": cnpj,
        "valor": valor
    }