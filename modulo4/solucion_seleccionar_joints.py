"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra la solución para filtrar solamente los joints de una selección de objetos más grande.
"""
import maya.cmds as cmds

# Crea la lista que va a guardar los nombres de los joints.
joints = []

# Lista todos los objetos seleccionados, de cualquier tipo.
all_objs = cmds.ls(sl=True)

# Itera sobre los objetos seleccionados.
for obj in all_objs:
    # Valida si el tipo del objeto es "joint".
    if(cmds.nodeType(obj) == "joint"):
        #  Si es True, lo agrega en la lista de joints.
        joints.append(obj)

# Limpia la selección de todos los objetos.
cmds.select(cl=True)

# Valida si hay joints en la lista de joints.
if(len(joints) > 0):
    # Si es True, selecciona esos joints.
    cmds.select(joints)
else:
    # Si es False, muestra un mensaje de retroalimentación en el script editor.
    print("Whoops! There are no joints in the selection.")
