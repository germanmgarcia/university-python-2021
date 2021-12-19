# Set
planetas = {'Marte', 'Júpeter', 'Venus'}
print(planetas)
# Largo
print(len(planetas))
# Revisar si un elemento está presente
print('Marte' in planetas)
# Agregar un elemento
planetas.add('Tierra')
print(planetas)
# No se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
# Eliminar elemento posiblemente arrojando un error
planetas.remove('Tierras')
print(planetas)
# Eliminar elemento sin arrojar error
planetas.discard('Júpiter')
print(planetas)
# Limpiar set
planetas.clear()
print(planetas)
# Eliminar el set
del planetas
print(planetas)