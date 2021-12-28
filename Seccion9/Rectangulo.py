class Rectangulo:
    '''
    Clase Rectangulo para calcular el área de un rectángulo
    '''
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'Área Rectángulo: {rectangulo1.calcular_area()}')