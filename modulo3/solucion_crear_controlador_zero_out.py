"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra cómo crear un controlador FK para un joint usando zero-out.
"""

import maya.cmds as cmds

# Selecciona el primer elemento del valor retornado por `cmds.ls` usando índices.
# Este script asume que solo se selecciona el joint al que se le va a crear el controlador.
target_joint = cmds.ls(sl=True)[0]

# Se crean las variables de los nombres del controlador.
new_controller_name = target_joint + "_ctrl"

# Se crea el controlador.
print("================ Create controller for joint " + target_joint)
cmds.circle(c=(0,0,0), nr=(1,0,0), sw=360, r=1, d=3, ut=0, tol=0.1, s=8, ch=1, name=new_controller_name)

print("Positioning controller")
parent_const = cmds.parentConstraint(target_joint, new_controller_name, weight=1)[0]
# Se borra el parent constraint, solo era necesario temporalmente para posicionar el controlador.
cmds.delete(parent_const)

print("Zeroing-out controller")

"""
**************************************** ZERO-OUT INICIO ****************************************
"""

print("Controller " + new_controller_name + " selected ")

# Variable con el nombre del grupo. Se crea concatenando el nombre del controlador con el sufijo "_grp".
grp_name = new_controller_name + "_grp"

# Variable que indica que se cree un grupo vacío cuando se llame a la función `cmds.group`.
is_group_empty = True

# Crea un grupo vacío con el nombre de la variable "grp_name".
# Si no se especifica que se cree el grupo vacío con el parámetro `emptyGroup(em)`, el grupo va a agrupar los objetos seleccionados.
# Para lograr el "zero-out", eso no es deseado.
cmds.group(em=is_group_empty, name=grp_name)
print("Group " + grp_name + " created")

"""
Se definen los sufijos de los atributos de traslación y rotación que se van a usar con las funciones `cmds.getAttr` y `cmds.setAttr`.
"""

# Atributos de traslación
tx_attribute = ".translateX"
ty_attribute = ".translateY"
tz_attribute = ".translateZ"

# Atributos de rotación
rx_attribute = ".rotateX"
ry_attribute = ".rotateY"
rz_attribute = ".rotateZ"

# Atributos de escala
sx_attribute = ".scaleX"
sy_attribute = ".scaleY"
sz_attribute = ".scaleZ"
"""
Se obtienen los valores del controlador que se transferirán al grupo usando `cmds.getAttr`.
"""

# Se obtiene los valores de los atributos de traslación de los ejes X, Y y Z del controlador
cube_tx = cmds.getAttr(new_controller_name + tx_attribute)
cube_ty = cmds.getAttr(new_controller_name + ty_attribute)
cube_tz = cmds.getAttr(new_controller_name + tz_attribute)

# Se obtiene los valores de los atributos de rotación de los ejes X, Y y Z del controlador
cube_rx = cmds.getAttr(new_controller_name + rx_attribute)
cube_ry = cmds.getAttr(new_controller_name + ry_attribute)
cube_rz = cmds.getAttr(new_controller_name + rz_attribute)

print("Obtained controller's attributes for zeroing out.")

"""
Transferencia de valores del controlador al grupo usando `cmds.setAttr`
"""
# Atributos de traslación
cmds.setAttr(grp_name + tx_attribute, cube_tx)
cmds.setAttr(grp_name + ty_attribute, cube_ty)
cmds.setAttr(grp_name + tz_attribute, cube_tz)

# Atributos de rotación
cmds.setAttr(grp_name + rx_attribute, cube_rx)
cmds.setAttr(grp_name + ry_attribute, cube_ry)
cmds.setAttr(grp_name + rz_attribute, cube_rz)

print("Transferred controller's values to group")

"""
Parent controlador bajo grupo
"""
cmds.parent(new_controller_name, grp_name)

print("Parented controller under group")

"""
"Zero-out" de valores de controlador usando `cmds.setAttr`
"""
# Atributos de traslación
cmds.setAttr(new_controller_name + tx_attribute, 0)
cmds.setAttr(new_controller_name + ty_attribute, 0)
cmds.setAttr(new_controller_name + tz_attribute, 0)

# Atributos de rotación
cmds.setAttr(new_controller_name + rx_attribute, 0)
cmds.setAttr(new_controller_name + ry_attribute, 0)
cmds.setAttr(new_controller_name + rz_attribute, 0)

print("Zeroed-out controller's values")

"""
**************************************** ZERO-OUT FINAL ****************************************
"""

print("Parenting joint to controller")
# Se crea el orient constraint que hará que el controlador pueda controlador al joint.
cmds.orientConstraint(new_controller_name, target_joint)

print("Blocking and hiding controller's translation and scale attributes")
# Para bloquear y ocultar atributos, se usa `cmds.setAttr` con los parámetros lock, keyable y channelBox.
cmds.setAttr(new_controller_name + tx_attribute, lock=True, keyable=False, channelBox=False)
cmds.setAttr(new_controller_name + ty_attribute, lock=True, keyable=False, channelBox=False)
cmds.setAttr(new_controller_name + tz_attribute, lock=True, keyable=False, channelBox=False)
cmds.setAttr(new_controller_name + sx_attribute, lock=True, keyable=False, channelBox=False)
cmds.setAttr(new_controller_name + sy_attribute, lock=True, keyable=False, channelBox=False)
cmds.setAttr(new_controller_name + sz_attribute, lock=True, keyable=False, channelBox=False)

