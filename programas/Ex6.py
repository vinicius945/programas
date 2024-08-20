def ordenar_pessoas(pessoas):
    return sorted(pessoas, key=lambda x: ([0], x[1]))

pessoas = [("João", 25), ("Maria", 30), ("Joao", 20), ("Pedro", 25), ("Maria", 20)]
pessoas_ordenadas = ordenar_pessoas(pessoas)
print(pessoas_ordenadas)