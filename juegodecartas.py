#Tarea "¡Batalla! Juego de cartas" hecho por Matthias Amelinckx.
#Las reglas del juego se encuentran en la asignación de la tarea.

#Aquí se generan las 52 cartas de un mazo común.
import random
numeros = list(range(1,14))
pintas = ["treboles", "diamantes", "picas", "corazones"]
cartas = [f"{numero} de {pinta}" for numero in numeros for pinta in pintas]

#Aquí se barajan las cartas.
random.shuffle(cartas)
carta_anterior = None

#Aquí se establecen los puntos iniciales y se inicia el juego.
puntos_j = 0
puntos_c = 0

print("¡Comienza el juego de cartas!")

#Este es el ciclo principal del juego, donde se sacan las cartas y se comparan.

while cartas:
    input("Presiona Enter para sacar una carta.")
    carta_actual = cartas.pop(0)
    print(f"Carta actual: {carta_actual}")
    
    if carta_anterior:
        valor_anterior=carta_anterior.split()[0]
        valor_actual=carta_actual.split()[0]

        if valor_anterior == valor_actual:
            accion = input("¡Batalla! Escribe 'batalla' para ganar un punto: ").strip().lower()
            if accion == "batalla":
                puntos_j += 1
                print("¡Ganaste un punto!")
            else:
                puntos_c += 1
                print("¡Batalla! La computadora gana un punto.")
    
    carta_anterior = carta_actual

#Al culminar el juego, se muestran los resultados y se determina el ganador.

print("Juego terminado")
print(f"Puntos del jugador: {puntos_j}")
print(f"Puntos de la computadora: {puntos_c}")

if puntos_j > puntos_c:
    print("¡Ganaste el juego!")
elif puntos_j < puntos_c:
    print("La computadora ganó el juego.")
else:
    print("El juego terminó en empate.")