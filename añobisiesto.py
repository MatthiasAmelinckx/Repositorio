#Trabajo de Año Bisiesto hecho por Matthias Amelinckx.
#El objetivo de este programa es determinar si un año entre 1900 
#y 2199 es bisiesto

def año_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

#Definimos la función que cuenta cuántos años bisiestos hay entre dos años
def cuenta_año_bisiesto(año1, año2):
    contador = 0
    for año in range (año1, año2+1):
        if año_bisiesto(año):
            contador += 1
    return contador

#Pedimos al usuario que introduzca los años necesarios para cumplir la función
año1=int(input("Diga un año entre 1900 y 2199: "))
año2=int(input("Diga otro año entre 1900 y 2199: "))

cantidad_AB = cuenta_año_bisiesto(año1, año2)

#Imprimimos el resultado
if cantidad_AB == 0:
    print(f"No hay años bisiestos entre {año1} y {año2}.")
elif cantidad_AB == 1: 
    print(f"Entre {año1} y {año2} hay 1 año bisiesto.")
else: 
    print(f"Entre {año1} y {año2} hay {cantidad_AB} años bisiestos.")
