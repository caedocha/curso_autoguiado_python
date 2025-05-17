
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra cómo usar las declaraciones condicionales para mostrar mensajes de retroalimentación
cuando no se cumple un prerequisito que el script necesita para funcionar.
En este caso se muestra un mensaje de retroalimentación explicando que se necesita selecciona al menos
un objeto para que el script funcione.
"""

import maya.cmds as cmds

# Se listan los objetos seleccionados.
selected_objects = cmds.ls(sl=True)

# Esta condición lógica compara que el número de objetos seleccionados sea mayor a cero.
# Recuerden que la función `len` devuelve el número de valores de la lista.
areThereAnyObjectsSelected = len(selected_objects) > 0

# Se imprime, en el script editor, el resultado.
print("Are there any selected objects? " + str(areThereAnyObjectsSelected))

# Se usa el if/else para evaluar si hay objetos seleccionados.
if(areThereAnyObjectsSelected):
    # En caso de que `areThereAnyObjectsSelected` sea True, se van a imprimir los objetos seleccionados.
    for obj in selected_objects:
        print(obj)
else:
    # En caso de que `areThereAnyObjectsSelected` sea False, se va a imprimir en el script editor, este mensaje.
    print("Whoops! You must select at least one object in the scene for this script to work properly.")
