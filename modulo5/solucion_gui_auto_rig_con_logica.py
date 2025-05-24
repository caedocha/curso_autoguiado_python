"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Solución para crear una GUI para correr script que automatizan algunas partes del rig de un brazo.
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
# ********************************* FUNCIONES CREAR CADENAS DE JOINTS COMIENZAN AQUI *********************************
#

def create_joint_chains_main(*args):
    print("Creating joint chains")
    side = "r"
    orientation = "xyz"
    secondaryAxisOrient = "yup"
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
        cmds.select(non_wrist_joints) 
        cmds.joint(edit=True, oj=orientation, secondaryAxisOrient=secondaryAxisOrient, ch=True, zso=True)
        cmds.select(cl=True)
        cmds.select(wrist_jnt)
        cmds.joint(edit=True, oj="none", ch=True, zso=True)
        cmds.select(cl=True)
#
# ********************************* FUNCIONES CREAR CADENAS DE JOINTS TERMINAN AQUI *********************************
#

#
# ********************************* FUNCIONES CREAR CONTROLADORES FK COMIENZAN AQUI *********************************
#

def create_fk_controller(target_joint):
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
    print("Creating FK controllers")
    target_joints = cmds.ls(sl=True)
    for target_joint in target_joints:
        create_fk_controller(target_joint)

#
# ********************************* FUNCIONES CREAR CONTROLADORES FK TERMINAN AQUI *********************************
#

def delete_window_if_exists(window_name):
    if(cmds.window(window_name, q=True, exists=True)):
        print("Found old window from previous runs. Deleting it.")
        cmds.deleteUI(window_name, window=True)

def create_gui(window_name):
    print("Creating auto-rig GUI")

    # Variables con la configuración de la ventana
    window_title = "Arm Auto-rig"
    window_width = 370
    window_height = 200

    # Variables con la configuración de los botones
    button_width = 350
    button_height = 50

    # VENTANA
    win = cmds.window(title=window_title,rtf=True, sizeable=False, widthHeight=(window_width,window_height))

    # LAYOUT
    layout = cmds.columnLayout(p=win, cat=("left",10),rs=10)

    # CONTROLES
    cmds.button(p=layout,h=button_height,w=button_width,l="Create IK/FK/Bind joint chains", command=create_joint_chains_main)
    cmds.button(p=layout,h=button_height,w=button_width,l="Create FK controller(s)", command=create_fk_controllers_main)
    cmds.button(p=layout,h=button_height,w=button_width,l="Zero-out", command=zero_out_main)

    # MOSTRAR VENTANA
    cmds.showWindow(win)
    print("Done")

def main():
    window_name = "autoRigWindow"
    delete_window_if_exists(window_name)
    create_gui(window_name)

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
