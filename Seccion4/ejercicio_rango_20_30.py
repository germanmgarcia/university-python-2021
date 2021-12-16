edad = int(input('Introduce tu edad: '))

veintes = edad >= 20 and edad < 30
treintas = edad >=30 and edad < 40

if veintes or treintas:
    # print(f'Dentro de rango (20\'s) o (30\'s)')
    if veintes:
        print(f'Dentro de los 20\'s')
    elif treintas:
        print(f'Dentro de los 30\'s')
    else:
        print(f'Fuera de rango')
else:
    print(f"No está dentro de los 20's ni 30's")