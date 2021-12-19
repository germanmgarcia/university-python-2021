# Definir funa tupla
frutas = ('Naranja', 'Plátano', 'Guayaba')
print(frutas)
# Saber el largo
print(len(frutas))
# Acceder a un elemento
print(frutas[0])
# Navegación inversa
print(frutas[-1])
# Acceder a un rango
print(frutas[0:1]) # Sin incluir el último índice
# Recorrer elementos
for fruta in frutas:
    print(fruta, end=' ')
# Cambiar valor tupla
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n', frutas)
# Eliminar la tupla
del frutas
print(frutas)
