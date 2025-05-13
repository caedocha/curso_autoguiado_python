"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este script crea 2 cadenas de joints.
"""
import maya.cmds as cmds

# Las variables que se van a usar para crear los nombres de los joints.
right_suffix = "_r_"
left_suffix = "_l_"
jnt_name = "jnt"
jnt_number = 0

# Concatena el nombre del primer joint y lo asigna a la variable `jnt`
jnt = jnt_name + left_suffix + str(jnt_number)
# Crea el primer joint en la posición -1, 0, 0.
cmds.joint(n=jnt, p=(-1,0,0))

# Aumenta en 1 la variable contadora.
jnt_number = jnt_number + 1
# Concatena el nombre del segundo joint y lo asigna a la variable `jnt`
jnt = jnt_name + left_suffix + str(jnt_number)
# Crea el segundo joint en la posición -2, 0, 0.
cmds.joint(n=jnt, p=(-2,0,0))

# Aumenta en 1 la variable contadora.
jnt_number = jnt_number + 1
# Concatena el nombre del tercer joint y lo asigna a la variable `jnt`
jnt = jnt_name + left_suffix + str(jnt_number)
# Crea el tercer joint en la posición -3, 0, 0.
cmds.joint(n=jnt, p=(-3,0,0))

# Se detiene la creación de la primera cadena de joints al deseleccionarlos.
cmds.select(d=True)

# Resettea la variable contadora.
jnt_number = 0

# Inicia la creación de la segunda cadena de joints.
# La creación de esta cadena de joints es igual a la anterior, en lo que
# varía es en el sufijo y las posiciones de los joints.
jnt = jnt_name + right_suffix + str(jnt_number)
cmds.joint(n=jnt, p=(1,0,0))

jnt_number = jnt_number + 1
jnt = jnt_name + right_suffix + str(jnt_number)
cmds.joint(n=jnt, p=(2,0,0))

jnt_number = jnt_number + 1
jnt = jnt_name + right_suffix + str(jnt_number)
cmds.joint(n=jnt, p=(3,0,0))
