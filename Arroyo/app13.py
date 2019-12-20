#EJERCICIO NUMERO 19
#EN ESTE EJERCICO CALCULAREMOS LA DISCTANCIA DE CUALQUIER VEHICULO QUE HALLA RECORRIDO
#PARA HALLAR LA DISTANCIA NECESITAREMOS LA VELOCIDAD Y EL TIEMPO
def calcular_potencia(trabajo,tiempo):
    potencia=trabajo/tiempo
    #SI LA DISTANCIA ES MAYOR A 800 LE SALDRA UN MENSAJE DE ALIENTO; Ha recorrido un muy buen trayecto
    if (potencia>50):
        mensaje="La potencia de su motor es optimo, numericamente es igual a: ", potencia
    #CASO COTRARIO LE MOSTRARA QUE DEBE RECORRER MAS LUGARES
    else:
        mensaje="Usted deberia cambiar su motor, La potencia de su motor es", potencia

    return mensaje
