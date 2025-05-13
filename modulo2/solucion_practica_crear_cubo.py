"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este script crea un cubo, lo nombra, lo mueve, lo rota y lo escala.
"""
import maya.cmds as cmds

# Las variables del nombre y los atributos de traslación, rotación y escala.
name = "cubo_de_practica"
pos_x = 1
pos_y = 2
pos_z = 3
angle = 45
scale = 2

# Se crea el cubo con el nombre de la variable `name`.
cmds.polyCube(name=name)
# Se mueve el cubo.
cmds.move(pos_x, pos_y, pos_z)
# Se rota el cubo.
cmds.rotate(angle, angle, angle)
# Se escala el cubo.
cmds.scale(scale, scale, scale)
