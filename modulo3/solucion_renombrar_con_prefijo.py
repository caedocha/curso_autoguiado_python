
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Solución para renombrar joints con un prefijo.
"""

print("Selecting parent joint")
# La variable que contiene el prefijo con el que se van a renombrar los joints.
prefix = "jnt_"

# Asumiendo que solo selecciona el primer joint de la cadena.
# Guarda el primer valor de la lista de objetos seleccionados.
joints = cmds.ls(sl=True)
first_joint = joints[0]

# Usa "first_joint" para luego seleccionar la jerarquía de joints.
cmds.select(first_joint, hi=True)

print("Now selecting the entire joint hierarchy")

# Lista la cadena de joints ahora seleccionados.
joints = cmds.ls(sl=True)

# Recorre uno por uno, los joints seleccionados.
for jnt in joints:
    print("Current joint name: " + jnt)
    # Concatena el prefijo y el nombre original del joint para crear el nuevo nombre.
    new_name = prefix + jnt
    # Renombra el joint con su nuevo nombre.
    cmds.rename(jnt, new_name)
    print("New joint name: " + new_name)
print("Done renaming the joints")
