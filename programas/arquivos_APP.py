def gravar_peca(matriz: list):

    #Vamos usar o separador ; (semicolon)
    #Vai criar um arquivo na mesma pasta com as peÃ§as inseridas

    arquivo = open('pecas.csv', mode='w')

    for peca in matriz:
        
        for info in peca:

            arquivo.write(info)
            arquivo.write(';')

        arquivo.write('\n')

    arquivo.close()

    print('Arquivo gravado com sucesso!')