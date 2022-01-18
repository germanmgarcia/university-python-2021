from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        raise NumerosIdenticosException('Números idénticos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e}, {type(e)}')
else: #Se ejecuta unicamente si no ocurre ninguna excepción
    print('No se arrojó ninguna excepción')
finally: #Independientemente si se lanza una excepción o no se ejecuta
    print('Ejecución del bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos...')