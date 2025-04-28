
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra cómo sacar valores individuales de una lista.
"""

import maya.cmds as cmds

# Selecciona y lista todos los objetos en la escena.
cmds.select(all=True)
all_objs = cmds.ls(sl=True)

# Los índices de las listas SIEMPRE comienzan en 0.
# Por lo que para sacar el primer valor de la lista siempre se usa el índice 0.
first_selected_obj = all_objs[0]
print("First object in the list: " + str(first_selected_obj))

# Una forma fácil de saber cuál índice usar es restarle 1 a la posición del valor.
# Por ejemplo, si uno sabe que desea sacar el segundo elemento de la lista, hay que restar 2 - 1
# para determinar el índice de la segunda casilla de la lista.
second_selected_obj = all_objs[1]
print("Second object in the list: " + str(second_selected_obj))

# Hay varias formas de sacar el último elemento de la lista.
# La posición del último valor es variable ya que el número de objetos de la lista puede variar.
# Eso hace que no se pueda usar un valor estático como 1, 2, 3, etc. Como en los ejemplos anteriores.
# La forma más común es usar la función `len` para conocer el número de elementos de la lista y luego restarle 1.
# El valor retornado por `len`, como el índice, indica la última posición de la lista.
last_selected_obj = all_objs[len(all_objs) - 1]
print("Last object in the list using positive index and len(): " + str(last_selected_obj))

# Otra forma de sacar los valores al final de la lista es usar números negativos.
# Como no se usa el -0, el índice negativo del último valor es -1.
# Así subsiguientemente con los demás elementos: -2, -3, -4 etc.
# Este es un método menos intuitivo que el otro.
last_selected_obj = all_objs[-1]
print("Last object in the list using negative index: " + str(last_selected_obj))

# Se usa `len` para saber el número de elementos de una lista.
number_of_objects_in_the_scene = len(all_objs)
print("Number of objects in the scene: " + str(last_selected_obj))
