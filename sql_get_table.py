import os
import re
import sys


def obter_tabelas(arquivo_sql):
    with open(arquivo_sql, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        # Use expressão regular para encontrar o nome das tabelas com o esquema
        tabelas_encontradas = re.findall(r'\b(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)\.([a-zA-Z_][a-zA-Z0-9_]*)\b', conteudo.lower())
        return tabelas_encontradas


def listar_tabelas_em_pasta(pasta):
    tabelas_totais = set()

    # Garanta que o caminho da pasta é absoluto
    pasta = os.path.abspath(pasta)

    # Liste todos os arquivos na pasta
    for arquivo in os.listdir(pasta):
        # Verifique se o arquivo tem a extensão .sql
        if arquivo.endswith('.sql'):
            caminho_completo = os.path.join(pasta, arquivo)
            tabelas_do_arquivo = obter_tabelas(caminho_completo)
            tabelas_totais.update(tabelas_do_arquivo)

    return tabelas_totais


if __name__ == "__main__":
    # Substitua 'caminho/para/sua/pasta' pelo caminho da sua pasta
    caminho_pasta_sql = os.path.abspath(sys.argv[1])
    tabelas_encontradas = listar_tabelas_em_pasta(caminho_pasta_sql)

    saida = ''

    print(sys.argv[2])

    for esquema, tabela in tabelas_encontradas:

        try:
            saida = saida + sys.argv[2].replace("#", f'{esquema}.{tabela}') + '\n'
        except IndexError as inderr:
            saida = saida + f'{esquema}.{tabela}\n'

    with open('tables.txt', 'w') as arquivo:
        arquivo.write(saida)
