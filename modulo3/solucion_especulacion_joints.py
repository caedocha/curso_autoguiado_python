"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Esta solución muestra cómo crear una cadena de joints usando ciclos.
"""
import maya.cmds as cmds

# Crea una variable que guarda el número de joints a crear.
number_of_joints = 3
# Crea las variables necesarias para crear los nombres de los joints.
right_suffix = "_r_"
left_suffix = "_l_"
jnt_prefix = "jnt"

print("Creating left joint chain")
# Usa la función `range` iterar el número de veces definido en `number_of_joints`.
# Esto va a permitir crear el numero de joints requerido.
for i in range(number_of_joints):
    # Suma 1 a `i` porque `i` comienza en 0.
    # Multiplica `i` por -1 para obtener un valor en el eje negativo.
    jnt_pos = (i + 1) * -1
    # Crea el nombre del joint.
    jnt_name = jnt_prefix + left_suffix + str(i)
    # Crea el joint usando la posición y el nombre recién creados.
    cmds.joint(n=jnt_name, p=(jnt_pos,0,0))
print("Done")

# Limpia la selección para detener la creación de la cadena de joints.
cmds.select(d=True)

print("Creating right joint chain")
# Hace exactamente lo mismo para crear la otra cadena. La única diferencia es que
# en esta cadena, no hace falta multiplicar por -1 ya que esta cadena está en el
# eje positivo.
for i in range(number_of_joints):
    jnt_pos = i + 1
    jnt_name = jnt_prefix + right_suffix + str(i)
    cmds.joint(n=jnt_name, p=(jnt_pos,0,0))
print("Done")
