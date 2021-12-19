# Definir una lista de tipo str
nombres = ['juan', 'karla', 'Ricardo', 'Maria']
# imprimir la lista nombres
print(nombres)
# acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
# Imprimir un rango
print(nombres[0:2]) # sin incluir el índice 2
# Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
# Desde el índice indicado hasta el final
print(nombres[1:])
# Cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen más nombres en la lista')
# Preguntar el largo de una lista
print(len(nombres))
# Agregar un elemento
nombres.append('Lorenzo')
print(nombres)
# Insertar un elemento en un índice en específico
nombres.insert(1, 'Octavio')
print(nombres)
# Remover un elemento
nombres.remove('Octavio')
print(nombres)
# Remover el último valor agregado
nombres.pop()
print(nombres)
# Eliminar un indice
del nombres[0]
print(nombres)
# Limpiar la lista
nombres.clear()
print(nombres)