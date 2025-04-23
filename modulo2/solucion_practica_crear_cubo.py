"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""
import maya.cmds as cmds

name = "cubo_de_practica"
pos_x = 1
pos_y = 2
pos_z = 3
angle = 45
scale = 2

cmds.polyCube(name=name)
cmds.move(pos_x, pos_y, pos_z)
cmds.rotate(angle, angle, angle)
cmds.scale(scale, scale, scale)
