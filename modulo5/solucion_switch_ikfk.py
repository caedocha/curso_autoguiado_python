"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Solución para crear un switch IK/FK.
"""

import maya.cmds as cmds

#
# ********************************* FUNCIONES ZERO-OUT COMIENZAN AQUI *********************************
#
def create_empty_group(grp_name):
    """
    Creates the controller's empty group.
    """
    is_group_empty = True
    cmds.group(em=is_group_empty, name=grp_name)
    print("Group " + grp_name + " created")

def transfer_attributes(ctrl_name, grp_name):
    """
    Transfer the attributes' values from the controller to the group.
    """
    tx_attribute = ".translateX"
    ty_attribute = ".translateY"
    tz_attribute = ".translateZ"
    rx_attribute = ".rotateX"
    ry_attribute = ".rotateY"
    rz_attribute = ".rotateZ"

    ctrl_tx = cmds.getAttr(ctrl_name + tx_attribute)
    ctrl_ty = cmds.getAttr(ctrl_name + ty_attribute)
    ctrl_tz = cmds.getAttr(ctrl_name + tz_attribute)
    ctrl_rx = cmds.getAttr(ctrl_name + rx_attribute)
    ctrl_ry = cmds.getAttr(ctrl_name + ry_attribute)
    ctrl_rz = cmds.getAttr(ctrl_name + rz_attribute)

    cmds.setAttr(grp_name + tx_attribute, ctrl_tx)
    cmds.setAttr(grp_name + ty_attribute, ctrl_ty)
    cmds.setAttr(grp_name + tz_attribute, ctrl_tz)

    cmds.setAttr(grp_name + rx_attribute, ctrl_rx)
    cmds.setAttr(grp_name + ry_attribute, ctrl_ry)
    cmds.setAttr(grp_name + rz_attribute, ctrl_rz)

    print("Transferred controller's values to group")

def zero_out_controller(ctrl_name):
    """
    Sets to zero the attributes of the controller.
    """
    tx_attribute = ".translateX"
    ty_attribute = ".translateY"
    tz_attribute = ".translateZ"
    rx_attribute = ".rotateX"
    ry_attribute = ".rotateY"
    rz_attribute = ".rotateZ"

    cmds.setAttr(ctrl_name + tx_attribute, 0)
    cmds.setAttr(ctrl_name + ty_attribute, 0)
    cmds.setAttr(ctrl_name + tz_attribute, 0)

    cmds.setAttr(ctrl_name + rx_attribute, 0)
    cmds.setAttr(ctrl_name + ry_attribute, 0)
    cmds.setAttr(ctrl_name + rz_attribute, 0)

    print("Zeroed-out controller's values")

def zero_out(ctrl_name):
    print("Controller " + ctrl_name + " selected ")
    grp_name = ctrl_name + "_grp"
    create_empty_group(grp_name)
    transfer_attributes(ctrl_name, grp_name)
    cmds.parent(ctrl_name, grp_name)
    print("Parented controller under group")
    zero_out_controller(ctrl_name)

def zero_out_main(*args):
    """
    Main function where all the zeroing-out logic is grouped.
    """
    print("Starting zero-out")
    selected_controllers = cmds.ls(sl=True)
    for ctrl_name in selected_controllers:
        zero_out(ctrl_name)
    print("Zero-out complete")
#
# ********************************* FUNCIONES ZERO-OUT TERMINAN AQUI *********************************
#

def block_and_hide_attrs(switch_name):
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

    cmds.setAttr(switch_name + tx_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(switch_name + ty_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(switch_name + tz_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(switch_name + rx_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(switch_name + ry_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(switch_name + rz_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(switch_name + sx_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(switch_name + sy_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(switch_name + sz_attribute, lock=True, keyable=False, channelBox=False)

def position_switch(switch_name):
    switch_ty = 2
    point_const = cmds.pointConstraint(wrist_joint, switch_name, weight=1)[0]
    cmds.delete(point_const)
    cmds.select(switch_name)

    # Se mueve el switch en el eje Y para separarlo un poco del joint de la muñeca.
    cmds.setAttr(switch_name + ".ty", switch_ty)

def create_switch_attributes(switch_name):
    cmds.select(switch_name)
    cmds.addAttr(ln="description", at="enum", en="1=IK,0=FK:")
    cmds.setAttr(switch_name + ".description", edit=True, channelBox=True)
    cmds.addAttr(ln="switch", at="long", min=0, max=1, dv=1)
    cmds.setAttr(switch_name + ".switch", edit=True, keyable=True)
    cmds.select(d=True)

def main(wrist_joint):
    print("Creating IK/FK switch.")

    switch_name = "ikfk_switch"
    loc = cmds.spaceLocator(name=switch_name)

    print("Positioning IK/FK switch")
    position_switch(switch_name)

    print("Zeroing-out IK/FK switch")
    zero_out(switch_name)

    print("Parenting IK/FK switch to wrist joint")
    cmds.pointConstraint(wrist_joint, switch_name, weight=1, maintainOffset=True)

    print("Block and hide attributes of IK/FK switch")
    block_and_hide_attrs(switch_name)

    print("Creating switch attributes")
    create_switch_attributes(switch_name)

wrist_joint = cmds.ls(sl=True)[0]
main(wrist_joint)
