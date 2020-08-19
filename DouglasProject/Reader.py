def create_list(lista):
    # 1.4, 2.3, 3.4, 4.4
    lista.pop(0)
    # Filtro de questoes principais
    cont = 0
    while cont < len(lista):
        item = lista[cont]
        lista[cont] = item.split(',')
        for x in range(len(lista[cont])):
            lista[cont][x] = lista[cont][x].replace(".", "")
        cont += 1

    # Fim filtro
    return lista


def run():
    arquivo = open('dados.csv', 'r', encoding='utf-8')
    texto = arquivo.readlines()
    arquivo.close()

    for i in range(len(texto)):
        texto[i] = texto[i].replace("\n", "")
    return create_list(texto)
