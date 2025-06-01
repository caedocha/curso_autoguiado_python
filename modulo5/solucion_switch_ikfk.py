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
    """
    Blocks and hides the translation, rotation and scale attribute of the switch controller.
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
    """
    Positions the switch controller on top of the wrist joint.
    """
    switch_ty = 2
    point_const = cmds.pointConstraint(wrist_joint, switch_name, weight=1)[0]
    cmds.delete(point_const)
    cmds.select(switch_name)

    # Se mueve el switch en el eje Y para separarlo, un poco, del joint de la muñeca.
    cmds.setAttr(switch_name + ".ty", switch_ty)

def create_switch_attributes(switch_name):
    """
    Creates the switch controller's switch and description attributes.
    """
    cmds.select(switch_name)
    # El atributo de `description` es una ayuda visual para entender cómo función el switch.
    cmds.addAttr(ln="description", at="enum", en="1=IK,0=FK:")
    cmds.setAttr(switch_name + ".description", edit=True, channelBox=True)
    # El atributo de `switch` es un número entero que solo acepta 1 ó 0.
    cmds.addAttr(ln="switch", at="long", min=0, max=1, dv=1)
    cmds.setAttr(switch_name + ".switch", edit=True, keyable=True)
    cmds.select(d=True)

def create_switch_controller(*args):
    """
    Main function connected to the GUI.
    Creates the switch controller based on the selected wrist joint.
    """
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
    """
    Inversely connects the FK weight to the controller's switch attribute.
    """
    # El valor del atributo del `switch` se debe invertir para conectarlo a los pesos FK.
    # Esto permite que cuando el `switch` está en 1, la cadena IK es la que controla
    # y la cadena FK se apaga. Y cuando el `switch` está en 0, sucede lo contrario.
    print("Connecting FK weight to switch")

    # Para lograr este comportamiento se crea un `reverse node` que se va a conectar
    # entre el atributo de `switch` y el peso FK. El nodo va a invertir el valor del switch.
    # Va a convertir 1 a 0, y 0 a 1.
    reverse_node = cmds.shadingNode("reverse", asUtility=True)
    cmds.connectAttr(switch_name + ".switch", reverse_node + ".inputX")
    cmds.connectAttr(reverse_node + ".outputX", obj + "." + attr)

def connect_ik_weights_to_switch(switch_name, obj, attr):
    """
    Directly connects the IK weight to the controller's switch attribute.
    """
    print("Connecting IK weight to switch")

    # En el caso del los pesos IK, el valor del `switch` se conecta directamente al peso IK.
    cmds.connectAttr(switch_name + ".switch", obj + "." + attr)

def connect_constraints_to_switch(*args):
    """
    Connects the joints' contraints with the IK/FK switch controller.
    """
    print("Connecting switch to constraints")
    objs = cmds.ls(sl=True)

    # Por convensión, el último valor de la lista de objetos es el controlador del switch.
    switch_name = objs[len(objs) - 1]
    for obj in objs:
        # Una forma de filtrar los contraints es usando su tipo de nodo.
        obj_parts = obj.split("_")
        # Solo conecta los atributos si es uno de los parent constraints.
        # Si es el controlador del switch, se ignora.
        if(obj_parts[len(obj_parts) - 1] == "parentConstraint1"):
            side = obj_parts[1] # l, r
            body_part = obj_parts[2] # shoulder, elbow, wrist
            # Se arman los nombres de los pesos usando las convenciones de los nombres de
            # los joints, constraints y pesos.
            ik_weight = "jnt_" + side + "_" + body_part + "_ikW0"
            fk_weight = "jnt_" + side + "_" + body_part + "_fkW1"
            connect_ik_weights_to_switch(switch_name, obj, ik_weight)
            connect_fk_weights_to_switch(switch_name, obj, fk_weight)

#
# ********************************* FUNCIONES PARA CONECTAR CONSTRAINTS AL SWITCH TERMINAN AQUI *********************************
#

def main():
    print("Creating IK/FK Switch GUI")

    # Variables con la configuracion de la ventana
    window_title = "IK/FK Switch"
    window_width = 370
    window_height = 210

    # Variables con la configuracion de los controles
    button_width = 350
    button_height = 50
    text_width = 350
    text_height = 20

    # VENTANA
    win = cmds.window(title=window_title,rtf=True, sizeable=False, widthHeight=(window_width,window_height))

    # LAYOUT
    layout = cmds.columnLayout(p=win, cat=("left",10),rs=10)

    # CONTROLES
    cmds.text(p=layout, w=text_width, h=text_height, align="center", l="1. Select the wrist joint to create switch controller", ww=True)
    cmds.button(p=layout,h=button_height,w=button_width,l="Create switch controller", command=create_switch_controller)
    cmds.text(p=layout, w=text_width, h=text_height, align="center", l="2. Select the joint's constraints and then the switch to connect them", ww=True)
    cmds.button(p=layout,h=button_height,w=button_width,l="Connect constraints to switch", command=connect_constraints_to_switch)

    # MOSTRAR VENTANA
    cmds.showWindow(win)
    print("Done")

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
