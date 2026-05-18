def ler_arquivo(nome_arquivo):

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            lista = arquivo.read().splitlines

            if lista is None:
                print('Arquivo vazio')
                return None
            else:
                return lista

    except (FileNotFoundError):
        print('Arquivo não encontrado')
        return None
