def multiplicarNumeros(*args:int) -> int:
    total = args[0]
    for i in args[1:]:
        total *= i
    return  total

resultado = multiplicarNumeros(2, 4, 8, 6)
print(resultado)