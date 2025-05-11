"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra cómo crear un controlador FK para un joint rotando los vértices del controlador.

Los pasos de script son casi idénticos a los pasos descritos en la solución que utiliza el parámetro `normal(nr)`.
Refiérase al archivo `solucion_crear_controlador.py`.
"""
import maya.cmds as cmds
  
targetJoint = cmds.ls(sl=True)[0]
newControllerName = targetJoint + "_ctrl"
groupName = newControllerName + "_grp"

print("================ Create controller for joint " + targetJoint)
cmds.circle(c=(0,0,0), nr=(0,0,1), r=1, d=3, ut=0, tol=0.1, s=8, ch=1, name=newControllerName)

print("Grouping up controller")
cmds.group(em=True, n=groupName)
cmds.parent(newControllerName, groupName)

print("Positioning controller")
pointConst = cmds.parentConstraint(targetJoint, groupName, weight=1)[0]
cmds.delete(pointConst)

# Se deselecciona los objetos que están actualmente seleccionados.
# Debemos seleccionar solamente los vértices del controlador, no el controlador en sí,
# para no alterar los valores del controlador. Se usan los índices que tienen los vértices.
# En este caso se selecciona un rango del vértice 0 al 7.
# Luego esos vértices se rotan 90 grados en el eje Z. Finalmente, se deseleccionan.
# Si usted selecciona los vértices manualmente, script editor va a mostrar
# resultados parecidos a este snippet.
# Lo mas importante de este snippet es la forma en que se seleccionan vértices con Python.
print("Rotate controller's vertices")
cmds.select(cl=True)
cmds.select(newControllerName + ".cv[0:7]")
cmds.rotate(0,0,90,r=True, eu=True, fo=True)
cmds.select(cl=True)

print("Parenting joint to controller")
cmds.orientConstraint(newControllerName, targetJoint)
