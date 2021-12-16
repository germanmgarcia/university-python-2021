numero1 = int(input('Proporciona el número 1 : '))
numero2 = int(input('Proporciona el número 2: '))

if numero1 > numero2:
    print(f'El número mayor es: {numero1}')
elif numero1 == numero2:
    print(f'Los dos números son iguales')
else:
    print(f'El número mayor es: {numero2}')