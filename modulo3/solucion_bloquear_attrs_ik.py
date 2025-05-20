"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra cómo bloquear y ocultar los atributos de un IK controlador.
"""

import maya.cmds as cmds

objs = cmds.ls(sl=True)

# Atributos de escala
sx_attribute = ".scaleX"
sy_attribute = ".scaleY"
sz_attribute = ".scaleZ"

for obj in objs:
    cmds.setAttr(obj + sx_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(obj + sy_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(obj + sz_attribute, lock=True, keyable=False, channelBox=False)
