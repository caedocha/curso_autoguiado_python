"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Solución para crear la GUI del proyecto final.
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
    """
    Zeros-out a controller.
    """
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
# ********************************* FUNCIONES CREAR CADENAS DE JOINTS COMIENZAN AQUI *********************************
#
def create_joint_constraints(locators, side):
    """
    Creates the parent constraints between the IK and FK joints and the bind one.
    """
    print("Creating parent constraints")
    for loc in locators:
        jnt = "jnt_" + side + "_" + loc
        print("Creating constraints for " + loc)
        ik_jnt = jnt + "_ik"
        fk_jnt = jnt + "_fk"
        bind_jnt = jnt + "_bind"
        cmds.parentConstraint(ik_jnt, bind_jnt)
        cmds.parentConstraint(fk_jnt, bind_jnt)

def orient_wrist_joint(wrist_jnt):
    """
    Orients the wrist joint using "Orient Joint to World" option.
    """
    print("Orienting wrist joint")
    cmds.select(wrist_jnt)
    cmds.joint(edit=True, oj="none", ch=True, zso=True)
    cmds.select(cl=True)

def orient_nonwrist_joints(non_wrist_joints):
    """
    Orients the non-wrist joints with a particular orientation.
    """
    print("Orienting non-wrist joints")
    orientation = "xyz"
    secondaryAxisOrient = "yup"
    cmds.select(non_wrist_joints) 
    cmds.joint(edit=True, oj=orientation, secondaryAxisOrient=secondaryAxisOrient, ch=True, zso=True)
    cmds.select(cl=True)

def create_joint_chains_main(*args):
    """
    Main function connected to the GUI.
    Creates the IK, FK and bind joints based on manually-placed locators.
    """
    print("Creating joint chains")
    side = "r"
    chain_types = ["ik", "fk", "bind"]

    locators = cmds.ls(sl=True)
    cmds.select(cl=True)

    for type in chain_types:
        non_wrist_joints = []
        wrist_jnt = ""
        for loc in locators:
            tx = cmds.getAttr(loc+".tx")
            ty = cmds.getAttr(loc+".ty")
            tz = cmds.getAttr(loc+".tz")
            jnt_pos = (tx, ty, tz)
            jnt_name = "jnt_" + side + "_" + loc + "_" + type
            cmds.joint(n=jnt_name, p=jnt_pos)
            if(loc != "wrist"):
                non_wrist_joints.append(jnt_name)
            else:
                wrist_jnt = jnt_name
        orient_nonwrist_joints(non_wrist_joints)
        orient_wrist_joint(wrist_jnt)
    create_joint_constraints(locators, side)

#
# ********************************* FUNCIONES CREAR CADENAS DE JOINTS TERMINAN AQUI *********************************
#

#
# ********************************* FUNCIONES CREAR CONTROLADORES FK COMIENZAN AQUI *********************************
#

def create_fk_controller(target_joint):
    """
    Creates a single FK controller.
    """
    new_controller_name = target_joint + "_ctrl"

    # Atributos de traslación
    tx_attribute = ".translateX"
    ty_attribute = ".translateY"
    tz_attribute = ".translateZ"

    # Atributos de escala
    sx_attribute = ".scaleX"
    sy_attribute = ".scaleY"
    sz_attribute = ".scaleZ"

    print("Create controller for joint " + target_joint)
    cmds.circle(c=(0,0,0), nr=(1,0,0), sw=360, r=1, d=3, ut=0, tol=0.1, s=8, ch=1, name=new_controller_name)

    print("Positioning controller")
    parent_const = cmds.parentConstraint(target_joint, new_controller_name, weight=1)[0]
    cmds.delete(parent_const)

    print("Zeroing-out controller")
    zero_out(new_controller_name)

    print("Parenting joint to controller")
    cmds.orientConstraint(new_controller_name, target_joint)

    print("Blocking and hiding controller's translation and scale attributes")
    cmds.setAttr(new_controller_name + tx_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(new_controller_name + ty_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(new_controller_name + tz_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(new_controller_name + sx_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(new_controller_name + sy_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(new_controller_name + sz_attribute, lock=True, keyable=False, channelBox=False)


def create_fk_controllers_main(*args):
    """
    Main function connected to the GUI.
    Creates an FK controller per selected joint.
    """
    print("Creating FK controllers")
    target_joints = cmds.ls(sl=True)
    for target_joint in target_joints:
        create_fk_controller(target_joint)

#
# ********************************* FUNCIONES CREAR CONTROLADORES FK TERMINAN AQUI *********************************
#

#
# ********************************* FUNCIONES CREAR CONTROLADORES FK COMIENZAN AQUI *********************************
#

def block_and_hide_ik_controllers(ik_controller, pole_vector_controller):
    """
    Blocks the IK controllers scale attributes.
    """
    sx_attribute = ".scaleX"
    sy_attribute = ".scaleY"
    sz_attribute = ".scaleZ"
    cmds.setAttr(ik_controller + sx_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(ik_controller + sy_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(ik_controller + sz_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(pole_vector_controller + sx_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(pole_vector_controller + sy_attribute, lock=True, keyable=False, channelBox=False)
    cmds.setAttr(pole_vector_controller + sz_attribute, lock=True, keyable=False, channelBox=False)

def position_pole_vector_controller(elbow_joint, pole_vector_controller_group):
    """
    Positions the pole vector controller slightly behind the elbow joint.
    """
    pointConst = cmds.pointConstraint(elbow_joint, pole_vector_controller_group, weight=1)[0]
    cmds.delete(pointConst)
    cmds.move(0,0,-2, pole_vector_controller_group, relative=True)

def create_ik_rig(*args):
    """
    Main function connected to the GUI.
    Creates the IK rig for a set of joints.
    """
    print("Creating IK rig")

    joints = cmds.ls(sl=True)
    shoulder_joint = joints[0]
    elbow_joint = joints[1]
    wrist_joint = joints[2]

    pole_vector_controller = "poleVector_r_ctrl"
    pole_vector_controller_group = pole_vector_controller + "_grp"
    ik_controller = "ik_r_ctrl"
    ik_controller_group = ik_controller + "_grp"

    print("Creating IK handle")
    ik_handle = cmds.ikHandle(sj=shoulder_joint, ee=wrist_joint)[0]
    print(ik_handle)

    print("Creating pole vector controller")
    cmds.spaceLocator(n=pole_vector_controller)

    print("Grouping pole vector controller")
    cmds.group(em=True, n=pole_vector_controller_group)
    cmds.parent(pole_vector_controller, pole_vector_controller_group)

    print("Positioning pole vector controller")
    position_pole_vector_controller(elbow_joint, pole_vector_controller_group)

    print("Creating pole vector constraint")
    cmds.poleVectorConstraint(pole_vector_controller, ik_handle)

    print("Creating IK controller")
    cmds.circle(c=(0,0,0), nr=(1,0,0), r=1, d=3, ut=0, tol=0.1, s=8, ch=1, name=ik_controller)

    print("Grouping up IK controller")
    cmds.group(em=True, n=ik_controller_group)
    cmds.parent(ik_controller, ik_controller_group)

    print("Positioning IK controller")
    pointConst = cmds.parentConstraint(wrist_joint, ik_controller_group, weight=1)[0]
    cmds.delete(pointConst)

    print("Parenting IK handle to IK controller")
    cmds.parent(ik_handle, ik_controller)

    print("Blocking and hiding controller's scale attributes")
    block_and_hide_ik_controllers(ik_controller, pole_vector_controller)

    print("Done")

#
# ********************************* FUNCIONES CREAR CONTROLADORES FK TERMINAN AQUI *********************************
#

#
# ********************************* FUNCIONES CREAR SWITCH IK/FK COMIENZAN AQUI *********************************
#

def block_and_hide_attrs(switch_name):
    """
    Blocks and hide the translation, rotation and scale attributes of the switch controller.
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

def position_switch(switch_name, wrist_joint):
    """
    Positions the switch controller on top of the wrist joint.
    """
    switch_ty = 2
    point_const = cmds.pointConstraint(wrist_joint, switch_name, weight=1)[0]
    cmds.delete(point_const)
    cmds.select(switch_name)
    cmds.setAttr(switch_name + ".ty", switch_ty)

def create_switch_attributes(switch_name):
    """
    Creates the `switch` and `description` attribute of the switch controller.
    """
    cmds.select(switch_name)
    cmds.addAttr(ln="description", at="enum", en="1=IK,0=FK:")
    cmds.setAttr(switch_name + ".description", edit=True, channelBox=True)
    cmds.addAttr(ln="switch", at="long", min=0, max=1, dv=1)
    cmds.setAttr(switch_name + ".switch", edit=True, keyable=True)
    cmds.select(d=True)

def create_switch_controller(*args):
    """
    Creates the switch controller on top of the wrist joint.
    """
    print("Creating IK/FK switch.")

    wrist_joint = cmds.ls(sl=True)[0]
    switch_name = "ikfk_switch"
    loc = cmds.spaceLocator(name=switch_name)

    print("Positioning IK/FK switch")
    position_switch(switch_name, wrist_joint)

    print("Zeroing-out IK/FK switch")
    zero_out(switch_name)

    print("Parenting IK/FK switch to wrist joint")
    cmds.pointConstraint(wrist_joint, switch_name, weight=1, maintainOffset=True)

    print("Block and hide attributes of IK/FK switch")
    block_and_hide_attrs(switch_name)

    print("Creating switch attributes")
    create_switch_attributes(switch_name)

def connect_fk_to_switch(switch_name, obj, attr):
    """
    Inversely connects the switch attribute to the obj's attr.
    """
    print("Connecting FK to switch")
    reverse_node = cmds.shadingNode("reverse", asUtility=True)
    cmds.connectAttr(switch_name + ".switch", reverse_node + ".inputX")
    cmds.connectAttr(reverse_node + ".outputX", obj + "." + attr)

def connect_ik_to_switch(switch_name, obj, attr):
    """
    Directly connects the switch attribute to the obj's attr.
    """
    print("Connecting IK to switch")
    cmds.connectAttr(switch_name + ".switch", obj + "." + attr)

def connect_constraints_to_switch(*args):
    """
    Main function connected to the IK/FK switch GUI.
    Connects the bind jonit's IK/FK weights to the switch controller.
    """
    print("Connecting constraints to constraints")
    objs = cmds.ls(sl=True)
    switch_name = objs[len(objs) - 1]
    for obj in objs:
        if(cmds.nodeType(obj) == "parentConstraint"):
            attrs = cmds.listAttr(obj)
            for attr in attrs:
                attr_parts = attr.split("_")
                if(attr_parts[len(attr_parts) - 1] == "ikW0"):
                    connect_ik_to_switch(switch_name, obj, attr)
                if(attr_parts[len(attr_parts) - 1] == "fkW1"):
                    connect_fk_to_switch(switch_name, obj, attr)

def connect_ik_controllers_to_switch(*args):
    """
    Connects the IK controllers' visibility to the switch.
    """
    print("Connecting IK controllers to constraints")
    objs = cmds.ls(sl=True)
    switch_name = objs[len(objs) - 1]
    for obj in objs:
        obj_parts = obj.split("_")
        if(obj_parts[len(obj_parts) - 1] == "ctrl"):
            connect_ik_to_switch(switch_name, obj, "visibility")

def connect_fk_controllers_to_switch(*args):
    """
    Connects the FK controllers' visibility to the switch.
    """
    print("Connecting FK controllers to constraints")
    objs = cmds.ls(sl=True)
    switch_name = objs[len(objs) - 1]
    for obj in objs:
        obj_parts = obj.split("_")
        if(obj_parts[len(obj_parts) - 1] == "ctrl"):
            connect_fk_to_switch(switch_name, obj, "visibility")

def create_ik_fk_switch_gui(*args):
    """
    Displays IK/FK switch GUI.
    """
    print("Display IK/FK switch GUI")

    # Variables con la configuración de la ventana
    window_title = "IK/FK Switch"
    window_width = 370
    window_height = 380

    # Variables con la configuración de los controles
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
    cmds.text(p=layout, w=text_width, h=text_height, align="center", l="3. Select the IK controllers and then the switch to connect them", ww=True)
    cmds.button(p=layout,h=button_height,w=button_width,l="Connect IK controllers to switch", command=connect_ik_controllers_to_switch)
    cmds.text(p=layout, w=text_width, h=text_height, align="center", l="4. Select the FK controllers and then the switch to connect them", ww=True)
    cmds.button(p=layout,h=button_height,w=button_width,l="Connect FK controllers to switch", command=connect_fk_controllers_to_switch)

    # MOSTRAR VENTANA
    cmds.showWindow(win)
    print("Done")

#
# ********************************* FUNCIONES CREAR SWITCH IK/FK TERMINAN AQUI *********************************
#

def delete_window_if_exists(window_name):
    if(cmds.window(window_name, q=True, exists=True)):
        print("Found old window from previous runs. Deleting it.")
        cmds.deleteUI(window_name, window=True)

def create_gui(window_name):
    """
    Creates main GUI
    """
    print("Creating auto-rig GUI")

    # Variables con la configuración de la ventana
    window_title = "Arm Auto-rig"
    window_width = 370
    window_height = 480

    # Variables con la configuración de los controles
    button_width = 350
    button_height = 50
    text_width = 350
    text_height = 20

    # VENTANA
    win = cmds.window(title=window_title,rtf=True, sizeable=False, widthHeight=(window_width,window_height))

    # LAYOUT
    layout = cmds.columnLayout(p=win, cat=("left",10),rs=10)

    # CONTROLES
    cmds.text(p=layout, w=text_width, h=text_height, align="center", l="1. Select the locators to create the joint chains", ww=True)
    cmds.button(p=layout,h=button_height,w=button_width,l="Create IK/FK/Bind joint chains", command=create_joint_chains_main)
    cmds.text(p=layout, w=text_width, h=text_height, align="center", l="2. Select the FK joint(s) to create the FK controllers", ww=True)
    cmds.button(p=layout,h=button_height,w=button_width,l="Create FK controller(s)", command=create_fk_controllers_main)
    cmds.text(p=layout, w=text_width, h=text_height, align="center", l="3. Select the IK joints in order to create the IK rig", ww=True)
    cmds.button(p=layout,h=button_height,w=button_width,l="Create IK Rig", command=create_ik_rig)
    cmds.text(p=layout, w=text_width, h=text_height, align="center", l="4. Open the IK/FK switch menu", ww=True)
    cmds.button(p=layout,h=button_height,w=button_width,l="Create IK/FK Switch", command=create_ik_fk_switch_gui)
    cmds.text(p=layout, w=text_width, h=text_height, align="center", l="Select the object(s) to zero-out", ww=True)
    cmds.button(p=layout,h=button_height,w=button_width,l="Zero-out", command=zero_out_main)

    # MOSTRAR VENTANA
    cmds.showWindow(win)
    print("Done")

def main():
    """
    Main function, everything starts here!
    """
    window_name = "autoRigWindow"
    delete_window_if_exists(window_name)
    create_gui(window_name)

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
