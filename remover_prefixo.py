from os import walk, path, rename

def remover_prefixo(prefixo):
    local = '.'

    for _, _, arquivos in walk(local):
        for arquivo in arquivos:
            if prefixo in arquivo:
                nome_original = arquivo
                novo_nome = arquivo.split(prefixo)[1]

                if novo_nome != nome_original and not path.isfile(path.join(local, novo_nome)):
                    rename(path.join(path.join(local, nome_original), path.join(local, novo_nome)))

def main():
    prefixo = input('Digite o prefixo que deseja remover dos arquivos: ')
    remover_prefixo(prefixo)

if __name__ == '__main__':
    main()
