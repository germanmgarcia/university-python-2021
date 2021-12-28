class Cubo:
    '''
    Clase para calcular el volúmen de un cubo
    '''
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo

ancho = int(input('Proporcionar el ancho: '))
alto = int(input('Proporcionar el alto: '))
profundo = int(input('Proporcionar el profundo: '))

cubo1 = Cubo(ancho, alto, profundo)

print(f'Volúmen cubo: {cubo1.calcular_volumen()}')