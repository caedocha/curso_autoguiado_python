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

#
# ********************************* FUNCIONES CREAR SWITCH COMIENZAN AQUI *********************************
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

def create_switch_controller(*args):
    print("Creating IK/FK switch.")

    wrist_joint = cmds.ls(sl=True)[0]
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

#
# ********************************* FUNCIONES CREAR SWITCH TERMINAN AQUI *********************************
#

#
# ********************************* FUNCIONES PARA CONECTAR CONSTRAINTS AL SWITCH TERMINAN AQUI *********************************
#

def connect_fk_weights_to_switch(switch_name, obj, attr):
    print("Connecting FK weight to switch")
    plusMinusNode = cmds.shadingNode("plusMinusAverage", asUtility=True)
    cmds.setAttr(plusMinusNode + ".operation", 2)
    cmds.setAttr(plusMinusNode + ".input1D[0]", 1)
    cmds.connectAttr(switch_name + ".switch", plusMinusNode + ".input1D[1]")
    cmds.connectAttr(plusMinusNode + ".output1D", obj + "." + attr)

def connect_ik_weights_to_switch(switch_name, obj, attr):
    print("Connecting IK weight to switch")
    cmds.connectAttr(switch_name + ".switch", obj + "." + attr)

def connect_constraints_to_switch(*args):
    print("Connecting positive side of the switch to constraints")
    objs = cmds.ls(sl=True)
    switch_name = objs[len(objs) - 1]
    for obj in objs:
        if(cmds.nodeType(obj) == "parentConstraint"):
            attrs = cmds.listAttr(obj)
            for attr in attrs:
                attr_parts = attr.split("_")
                if(attr_parts[len(attr_parts) - 1] == "ikW0"):
                    connect_ik_weights_to_switch(switch_name, obj, attr)
                if(attr_parts[len(attr_parts) - 1] == "fkW1"):
                    connect_fk_weights_to_switch(switch_name, obj, attr)

#
# ********************************* FUNCIONES PARA CONECTAR CONSTRAINTS AL SWITCH TERMINAN AQUI *********************************
#

def main():
    print("Creating IK/FK Switch GUI")

    # Variables con la configuracion de la ventana
    window_title = "IK/FK Switch"
    window_width = 370
    window_height = 130

    # Variables con la configuracion de los botones
    button_width = 350
    button_height = 50

    # VENTANA
    win = cmds.window(title=window_title,rtf=True, sizeable=False, widthHeight=(window_width,window_height))

    # LAYOUT
    layout = cmds.columnLayout(p=win, cat=("left",10),rs=10)

    # CONTROLES
    cmds.button(p=layout,h=button_height,w=button_width,l="Create switch controller", command=create_switch_controller)
    cmds.button(p=layout,h=button_height,w=button_width,l="Connect constraints to switch", command=connect_constraints_to_switch)

    # MOSTRAR VENTANA
    cmds.showWindow(win)
    print("Done")

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
