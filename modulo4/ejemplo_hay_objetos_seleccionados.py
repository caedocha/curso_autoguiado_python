"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra un ejemplo de una condición lógica que evalua si hay objetos seleccionados.
"""
import maya.cmds as cmds

# Se listan los objetos seleccionados.
selected_objects = cmds.ls(sl=True)

# Esta condición lógica compara que el número de objetos seleccionados sea mayor a cero.
# Recuerden que la función `len` devuelve el número de valores de la lista.
areThereAnySelectedObjects = len(selected_objects) > 0

# Se imprime, en el script editor, el resultado.
print("Are there any selected objects? " + str(areThereAnySelectedObjects))
