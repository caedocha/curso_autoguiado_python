"""
Solución de Zero-Out Simplificado
Este script hace un "zero out" simplificado al objeto que esté seleccionado.
Hacer "zero out" se refiere a crear un grupo y transfirle los valores del controlador para que este quede con los valores por defecto de traslación, escala y rotación.
"""
import maya.cmds as cmds

# Liste el primer objeto que esté seleccionado. Usualmente, va a ser el controlador al que se le haga el "zero out".
ctrl = cmds.ls(sl=True)[0]
print("Controller " + ctrl + " selected ")

# Variable con el nombre del grupo. Se crea concatenando el nombre del controlador con el sufijo "_grp".
grp_name = ctrl + "_grp"

# Variable que indica que se cree un grupo vacío cuando se llame a la función `cmds.group`.
is_group_empty = True

# Crea un grupo vacío con el nombre de la variable "grp_name".
# Si no se especifica que se cree el grupo vacío con el parámetro `emptyGroup(em)`, el grupo va a agrupar los objetos seleccionados.
# Para lograr el "zero-out", eso no es deseado.
cmds.group(em=is_group_empty, name=grp_name)
print("Group " + grp_name + " created")

"""
Se definen los sufijos de los atributos de traslación, rotación y escala que se van a usar con las funciones `cmds.getAttr` y `cmds.setAttr`.
"""

# Atributos de traslación
tx_attribute = ".translateX"
ty_attribute = ".translateY"
tz_attribute = ".translateZ"

# Atributos de escala
sx_attribute = ".scaleX"
sy_attribute = ".scaleY"
sz_attribute = ".scaleZ"

# Atributos de rotación
rx_attribute = ".rotateX"
ry_attribute = ".rotateY"
rz_attribute = ".rotateZ"

"""
Se obtienen los valores del controlador que se transferirán al grupo usando `cmds.getAttr`.
"""

# Se obtiene los valores de los atributos de traslación de los ejes X, Y y Z del controlador
cube_tx = cmds.getAttr(ctrl + tx_attribute)
cube_ty = cmds.getAttr(ctrl + ty_attribute)
cube_tz = cmds.getAttr(ctrl + tz_attribute)

# Se obtiene los valores de los atributos de escala de los ejes X, Y y Z del controlador
cube_sx = cmds.getAttr(ctrl + sx_attribute)
cube_sy = cmds.getAttr(ctrl + sy_attribute)
cube_sz = cmds.getAttr(ctrl + sz_attribute)

# Se obtiene los valores de los atributos de rotación de los ejes X, Y y Z del controlador
cube_rx = cmds.getAttr(ctrl + rx_attribute)
cube_ry = cmds.getAttr(ctrl + ry_attribute)
cube_rz = cmds.getAttr(ctrl + rz_attribute)

print("Obtained controller's attributes for zeroing out.")

"""
Transferencia de valores del controlador al grupo usando `cmds.setAttr`
"""
# Atributos de traslacion
cmds.setAttr(grp_name + tx_attribute, cube_tx)
cmds.setAttr(grp_name + ty_attribute, cube_ty)
cmds.setAttr(grp_name + tz_attribute, cube_tz)

# Atributos de escala
cmds.setAttr(grp_name + sx_attribute, cube_sx)
cmds.setAttr(grp_name + sy_attribute, cube_sy)
cmds.setAttr(grp_name + sz_attribute, cube_sz)

# Atributos de rotacion
cmds.setAttr(grp_name + rx_attribute, cube_rx)
cmds.setAttr(grp_name + ry_attribute, cube_ry)
cmds.setAttr(grp_name + rz_attribute, cube_rz)

print("Transfered controller's values to group")

"""
Parent controlador bajo grupo
"""
cmds.parent(ctrl, group_name)

print("Parented controller under group")

"""
"Zero-out" de valores de controlador usando `cmds.setAttr`
"""
# Atributos de traslacion
cmds.setAttr(ctrl + tx_attribute, 0)
cmds.setAttr(ctrl + ty_attribute, 0)
cmds.setAttr(ctrl + tz_attribute, 0)

# Atributos de escala
cmds.setAttr(ctrl + sx_attribute, 1)
cmds.setAttr(ctrl + sy_attribute, 1)
cmds.setAttr(ctrl + sz_attribute, 1)

# Atributos de rotacion
cmds.setAttr(ctrl + rx_attribute, 0)
cmds.setAttr(ctrl + ry_attribute, 0)
cmds.setAttr(ctrl + rz_attribute, 0)

print("Zeroed-out controller's values")

print("Done!")
