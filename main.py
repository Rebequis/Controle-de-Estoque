def ler_arquivo(nome_arquivo):
    texto_limpo = Pre_processar_arquivo(nome_arquivo)
    if texto_limpo is None:
        return None

    lista_nome = []
    palavras = texto_limpo.split()

    for nome in palavras:
        nome = nome.strip()
        if nome != "":

            lista_nome.append(nome)

    return lista_nome
