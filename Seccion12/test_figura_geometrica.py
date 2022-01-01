from Cuadrado import  Cuadrado
from Rectangulo import Rectangulo

print('Creación Objeto Cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación Objeto Rectángulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=3, alto=8, color='verde')
print(f'Cálculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)