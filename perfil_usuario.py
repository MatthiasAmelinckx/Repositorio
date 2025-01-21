#Tarea Matthias Amelinckx de Perfil de Usuario

#Aquí se da la bienvenida al usuario y se pregunta su nombre
print("¡Bienvenido al programa de tu perfil, usuario!")
print("Preparemos tu perfil. Por favor responde las siguientes preguntas.")
nombre=str(input("¿Cuál es tu nombre? "))
print("Un placer,", nombre.upper)

#Aquí se pregunta el sexo al usuario
sexo = str(input (nombre+", ¿eres hombre, mujer u otro? "))
if sexo == str("hombre"):
    print("Bienvenido.")
elif sexo == str("mujer"):
    print("Bienvenida.")
else:
    print("Un placer recibirte.")

#Procedemos a preguntar el país de origen del usuario y hacerle el cuestionario acorde a su país natal.
#En el mismo bloque, preguntaremos la cosa favorita del país del usuario
pais=str(input(nombre+", ¿cuál es tu país de origen? Las opciones son Venezuela, España o Estados Unidos. "))
if pais == ("Venezuela"):
    print("Un país hermoso.")
    favorito = str(input("¿Qué es lo favorito de tu país, las guacamayas, las arepas o las vistas? "))
    print ("También me encantan "+favorito+", es de lo mejor de Venezuela.")
elif pais == ("Estados Unidos"):
    print("El hogar del sueño americano.")
    favorito = str(input("¿Cuál es tu comida favorita? Elige entre las hamburguesas, las pizzas o las malteadas. "))
    print("Que buena elección. Mi comida favorita en Estados Unidos también es "+favorito+".")
elif pais == ("España"):
    print("Una nación de cultura sin fin.")
    favorito = str(input("¿Qué es tu cosa favorita de España, la historia, el deporte o la comida? "))
    print("Estoy sorprendido, "+favorito+" también es mi cosa favorita de España.")
else:
    print(nombre+", esa no es una de las opciones...")

print("Tu perfil está listo: Tu nombre es "+nombre+". Te identificas como "+sexo+" y tu país de origen es "+pais)