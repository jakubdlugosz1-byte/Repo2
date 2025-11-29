def mnozenie(lista):
    nowa_lista = []
    for liczba in lista:
        nowa_lista.append(liczba * 2)
    return nowa_lista

liczby = [1, 2, 3, 34, 52]
wynik = mnozenie(liczby)
print(wynik)

def pomnoz_przez_dwa_lista_skladana(lista):
    return [liczba * 2 for liczba in lista]

liczby = [1, 2, 3, 34, 52]
wynik = pomnoz_przez_dwa_lista_skladana(liczby)
print(wynik)

