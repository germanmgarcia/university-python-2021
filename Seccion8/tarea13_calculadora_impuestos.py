pago = float(input('Proporcionar el pago del impuesto: '))
impuesto = float(input('Proporcionar el impuesto: '))

def funcion_calcular_impuesto(*args):
    pago = args[0]
    impuesto = pago * (args[1] / 100)
    return pago + impuesto

resultado = funcion_calcular_impuesto(pago, impuesto)
print(resultado)



# # Función que calcula el impuesto de un pago
# def calcular_total(pago_sin_impuesto, impuesto):
#     return pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
#
# # Ejecutamos la función
# pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
# impuesto = float(input('Proporcione el monto del impuesto: '))
# pago_con_impuesto = calcular_total(pago_sin_impuesto, impuesto)
# print(f'Pago con impuesto: {pago_con_impuesto}')