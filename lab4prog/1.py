Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

print("Lista:", Moja_lista)
Moja_lista.append(10)
print("append:", Moja_lista)

Moja_lista.insert(2, 100)
print("insert:", Moja_lista)

Moja_lista.extend([7, 8])
print("extend:", Moja_lista)

Moja_lista.remove(3)
print("remove:", Moja_lista)

Moja_lista.pop()
print("pop:", Moja_lista)

Moja_lista.sort()
print("sort:", Moja_lista)

Moja_lista.reverse()
print("reverse:", Moja_lista)

print("count:", Moja_lista.count(3))
print("index:", Moja_lista.index(86))
print("Długość:", len(Moja_lista))
Kopia = Moja_lista.copy()
print("Kopia:", Kopia)

Kopia.clear()
print("Po clear:", Kopia)