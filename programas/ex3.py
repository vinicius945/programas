
def busca(lista: list, valor, pos):
    while pos < len(lista) and lista[pos] != valor:
        pos = pos + 1

    if pos < len(lista):
        return pos
    else:
        return -1

lst = [2, 5, 6, 9, -1, 0, 7, 2, 4, 6, -1, 0]
x = 11
for i in range(len(lst)):
    valor = x - lst[i]
    resp = busca(lst, valor, i + 1)
    if resp != -1:
        print(lst[i], lst[resp])
   