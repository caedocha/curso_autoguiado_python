"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra cómo utilizar un ciclo dentro de otro para crear una matriz de cubos.
"""
import maya.cmds as cmds

# Las variables que indican el número de cubos en los ejes X y Y.
cube_number_x = 10
cube_number_y = 10
# La escala de los cubos. Se utiliza 0.5 para que haya espacio entre los cubos.
# Si la escala fuera 1, los cubos se tocarían y no se distinguiría la matriz.
cube_scale = 0.5

# La función `range` recibe un número que le indica  al ciclo cuántas veces debe iterar.
# La variable `i` guarda un número que va aumentando uno por uno.
# Es una forma sencilla de iterar el número de veces que uno desea cuando no se
# tiene una lista de objetos para iterar sobre ellos.
for i in range(cube_number_x):
    # El ciclo anidado dentro del otro va a iterar por completo en cada iteración del ciclo papá.
    # Es decir el número total de iteraciones de ambos ciclos es `cube_number_x` x `cube_number_y`. O sea, 10 x 10 = 100 veces.
    for j in range(cube_number_y):
        # Crea un cubo, lo escala y lo mueve. Las coordenadas X y Y van a ir cambiando
        # ya que sus valores son los de las variables `i` y `j`.
        # El valor en el eje Z es 0 porque no nos interasa mover el cubo en ese eje.
        # Al correr el script, pueden ver los valores que se usan para mover cada cubo
        # en el output del script editor.
        print("Coordinates X: " + str(i) + ", Y: " + str(j))
        cmds.polyCube()
        cmds.scale(cube_scale, cube_scale, cube_scale)
        cmds.move(i,j,0)
