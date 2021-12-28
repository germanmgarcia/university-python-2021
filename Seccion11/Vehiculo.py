class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo: [color: {self.color}, ruedas: {self.ruedas}]'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Coche: [velocidad: {self.velocidad}] {super().__str__()}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return  f'Bicicleta: [tipo: {self.tipo}] {super().__str__()}'


vehiculo1 = Vehiculo('rojo', 4)
print(f'Clase Vehiculo: {vehiculo1}')

coche1 = Coche('rojo', 4, 40)
print(f'Clase Coche: {coche1}')

bicicleta1 = Bicicleta('rojo', 2, 'montaña')
print(f'Clase Bicicleta: {bicicleta1}')