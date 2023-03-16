import os

def remover_prefixo(prefixo):
    local = '.'

    for pasta, _, arquivo in os.walk(local):
        for arquivo in arquivo:

            if prefixo in arquivo:
                nome_original = arquivo
                novo_nome = arquivo.split(prefixo)[1]

                if novo_nome != nome_original:
                    antigo_caminho = os.path.join(pasta, nome_original)
                    novo_caminho = os.path.join(pasta, novo_nome)

                    if not os.path.isfile(novo_caminho):
                        os.rename(antigo_caminho, novo_caminho)

def main():
    prefixo = input('Digite o prefixo que deseja remover dos arquivos: ')
    remover_prefixo(prefixo)

if __name__ == '__main__':
    main()
