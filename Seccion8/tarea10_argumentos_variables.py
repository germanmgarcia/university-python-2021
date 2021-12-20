def sumarNumeros(*args:int) -> int:
    total = 0
    for i in args:
        total += i
    return  total

resultado = sumarNumeros(2, 4, 8, 6)
print(resultado)