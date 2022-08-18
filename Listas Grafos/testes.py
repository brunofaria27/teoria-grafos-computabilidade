
def main():
    lista = [1, 3, 2, 1, 3, 2, 4]
    lista2 = [3, 4, 4, 2, 2, 5, 5]
    ordenar(lista, lista2)
    print(lista)
    print(lista2)


def ordenar(lst, lst2):
    lst2_new = []
    for i in lst:
        lst2_new.append(lst2[i])
    lst2.clear()
    lst2.extend(lst2_new)
    lst.sort()

main()