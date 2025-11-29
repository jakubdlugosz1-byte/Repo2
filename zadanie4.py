def co_drugi_element(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])


liczby = list(range(1, 11))
co_drugi_element(liczby)
