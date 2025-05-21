"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra la solución para crear el rig IK de la cadena de joints de un brazo.
"""
import maya.cmds as cmds

# Los nombres de los joints.
shoulder_joint = "jnt_r_shoulder_ik"
elbow_joint = "jnt_r_elbow_ik"
wrist_joint = "jnt_r_wrist_ik"

# Los nombres de los controladores y los grupos de los controladores.
pole_vector_controller = "poleVector_r_ctrl"
pole_vector_controller_group = pole_vector_controller + "_grp"
ik_controller = "ik_r_ctrl"
ik_controller_group = ik_controller + "_grp"

# Atributos de escala para bloquear y ocultarlos
sx_attribute = ".scaleX"
sy_attribute = ".scaleY"
sz_attribute = ".scaleZ"

print("Creating IK handle")
# Se crea el IK handle usando el joint del hombro y la muñeca.
# Luego se guarda el nombre del IK handle en la variable `ik_handle`.
# Note que la funcion ikHandle devuelve una lista de objetos,
# el primero es el nombre del IK handle.
ik_handle = cmds.ikHandle(sj=shoulder_joint, ee=wrist_joint)[0]
print(ik_handle)

print("Creating pole vector controller")
# Crea un locator para que sea el controlador del pole vector.
cmds.spaceLocator(n=pole_vector_controller)

print("Grouping pole vector controller")
# Crea un grupo vacío y luego "parentea" el controlador del pole vector.
cmds.group(em=True, n=pole_vector_controller_group)
cmds.parent(pole_vector_controller, pole_vector_controller_group)

print("Positioning pole vector controller")
# Posiciona el pole vector sobre el joint de hombro y lo mueve un poco para atrás.
pointConst = cmds.pointConstraint(elbow_joint, pole_vector_controller_group, weight=1)[0]
cmds.delete(pointConst)
cmds.move(0,0,-2, pole_vector_controller_group, relative=True)

print("Creating pole vector constraint")
# Crea el pole vector.
cmds.poleVectorConstraint(pole_vector_controller, ik_handle)

print("Creating IK controller")
# Crea el controlador IK.
cmds.circle(c=(0,0,0), nr=(1,0,0), r=1, d=3, ut=0, tol=0.1, s=8, ch=1, name=ik_controller)

print("Grouping up IK controller")
# Crea un grupo vacío y "parentea" el controlador con ese grupo.
cmds.group(em=True, n=ik_controller_group)
cmds.parent(ik_controller, ik_controller_group)

print("Positioning IK controller")
# Posiciona el controlador IK sobre el joint de la muñeca.
pointConst = cmds.parentConstraint(wrist_joint, ik_controller_group, weight=1)[0]
cmds.delete(pointConst)

print("Parenting IK handle to IK controller")
# "Parentea" el IK handle con el controlador IK.
cmds.parent(ik_handle, ik_controller)

print("Blocking and hiding controller's scale attributes")
# Para bloquear y ocultar atributos, se usa `cmds.setAttr` con los parámetros lock, keyable y channelBox.
# Bloquea los atributos de escala del controlador de IK.
cmds.setAttr(ik_controller + sx_attribute, lock=True, keyable=False, channelBox=False)
cmds.setAttr(ik_controller + sy_attribute, lock=True, keyable=False, channelBox=False)
cmds.setAttr(ik_controller + sz_attribute, lock=True, keyable=False, channelBox=False)

# Bloquea los atributos de escala del controlador del pole vector.
cmds.setAttr(pole_vector_controller + sx_attribute, lock=True, keyable=False, channelBox=False)
cmds.setAttr(pole_vector_controller + sy_attribute, lock=True, keyable=False, channelBox=False)
cmds.setAttr(pole_vector_controller + sz_attribute, lock=True, keyable=False, channelBox=False)

print("Done")
