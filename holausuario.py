from datetime import datetime
nombre = input ("¿Cuál es tu nombre, usuario? ")
if current_hour < 12:
  saludo = "Buenos días "
elif current_hour < 18:
  saludo = "Buenas tardes "
else:
  saludo = "Buenas noches "
print (f" {saludo}, {nombre}! Bienvenido a este curso de algoritmos y programación.")
