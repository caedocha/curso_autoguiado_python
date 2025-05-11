"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra cómo crear un FK controlador para un joint usando el parámetro `normal(nr)` de `cmds.circle`
"""
import maya.cmds as cmds

# Selecciona el primer elemento del valor retornado por `cmds.ls` usando índices.
# Este script asume que solo se selecciona el joint al que se le va a crear el controlador.
targetJoint = cmds.ls(sl=True)[0]

# Se crean las variables de los nombres del controlador y el grupo del controlador.
newControllerName = targetJoint + "_ctrl"
groupName = newControllerName + "_grp"

# Se crea el controlador usando el parámetro `normal(nr)` para que el controlador quede alineado con el joint correctamente.
print("================ Create controller for joint " + targetJoint)
cmds.circle(c=(0,0,0), nr=(1,0,0), r=1, d=3, ut=0, tol=0.1, s=8, ch=1, name=newControllerName)

print("Grouping up controller")
# Se crea un grupo. Se especifica que esté vacío usando el parámetro `empty(em)`.
cmds.group(em=True, n=groupName)
# Se "parentea" el controlador nuevo al grupo.
cmds.parent(newControllerName, groupName)

# Se crea un parent constraint entre el groupo y el joint para posicionar el controlador.
# Note que se saca el nombre del parent constraint usando un índice.
# Solo nos interesa ese primer valor de lo que retorna esta función.
print("Positioning controller")
pointConst = cmds.parentConstraint(targetJoint, groupName, weight=1)[0]
# Se borra el parent constraint, solo era necesario temporalmente para posicionar el controlador.
cmds.delete(pointConst)

print("Parenting joint to controller")
# Se crea el orient constraint que hará que el controlador pueda controlador al joint.
cmds.orientConstraint(newControllerName, targetJoint)
