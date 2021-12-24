def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32) * 5/9

celsius = float(input('Proporcione el valor en celsius: '))
fahrenheit = float(input('Proporcione el valor en fahrenheit: '))

resultado1 = celsius_fahrenheit(celsius)
resultado2 = fahrenheit_celsius(fahrenheit)
print(resultado1)
print(resultado2)


# # Función que convierte de celsius a fahrenheit
# def celsius_fahrenheit(celsius):
#         return celsius * 9/5 + 32
#
# def fahrenheit_celsius(fahrenheit):
#         return (fahrenheit-32) * 5/9
#
# # Realizamos algunas pruebas de conversión
# celsius = float(input('Proporcione su valor en celsius: '))
# resultado = celsius_fahrenheit(celsius)
# # Los dos puntos después de la variable de resultado dan un formato de 2 digitos flotantes
# print(f'{celsius} C a F: {resultado:.2f}')
# fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
# resultado = fahrenheit_celsius(fahrenheit)
# print(f'{fahrenheit} F a C: {resultado:.2f}')