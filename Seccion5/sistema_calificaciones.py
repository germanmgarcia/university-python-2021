calificacion = int(input('Proporciona un valor entre 0 y 10: '))
mensaje = None
if 9 <= calificacion <= 10:
    mensaje = 'A'
elif 8 <= calificacion < 9:
    mensaje = 'B'
elif 7 <= calificacion < 8:
    mensaje = 'C'
elif 6 <= calificacion < 7:
    mensaje = 'D'
elif 0 <= calificacion < 6:
    mensaje = 'F'
else:
    mensaje = 'Nota no reconocida'

print(f'{mensaje}')