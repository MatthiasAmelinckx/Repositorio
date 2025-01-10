#Trabajo de Arepas Dinámicas hecho por Matthias Amelinckx.
#Los volumenes trabajados con la taza, cucharada y cucharadita son de 240, 15 y 5 mL respectivamente.

print("¡Bienvenido! Para hacer una arepa necesitarás: 1 taza de agua, 1 taza de harina, 1 cucharadita de sal y 1 cucharada de aceite.")
print("Puede encontrar la receta para la preparación de sus arepas en cualquier página web. Recomendamos la de la página de la marca PAN.")

ml_de_agua = float(input("¿Cuántas tazas de agua quieres usar? "))*240
ml_de_harina = float(input("¿Cuántos tazas de harina quieres usar? "))*240
ml_de_sal = float(input("¿Cuántas cucharaditas de sal quieres usar? "))*5
ml_de_aceite = float(input("¿Cuántas cucharadas de aceite quieres usar? "))*15

#Se multiplica por 9/10 para tener en cuenta la pérdida de volumen al cocinar las arepas.
ml_totales = ((ml_de_agua + ml_de_harina + ml_de_sal + ml_de_aceite) * 9) / 10

#Se hace una división entera para saber cuántas arepas se pueden hacer con la mezcla resultante. Se asume que el volumen de una arepa es de 225 mL.
cantidad_de_arepas = ml_totales//225

print("El volumen total de su mezcla es de", ml_totales, "mL. Con esto, podrá hacer", cantidad_de_arepas, "arepas.")