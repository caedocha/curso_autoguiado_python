"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Solución para crear controladores FK usando funciones
Este script crea un controlador FK usando funciones para ordenar el script y hacerlo reutilizable.
"""

import maya.cmds as cmds

# ************************************ FUNCIONES ZERO-OUT INICIO ***********************************

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
    Main zero-out function where all the zeroing-out logic is grouped.
    """
    grp_name = ctrl_name + "_grp"
    create_empty_group(grp_name)
    transfer_attributes(ctrl_name, grp_name)
    cmds.parent(ctrl_name, grp_name)
    print("Parented controller under group")
    zero_out_controller(ctrl_name)

# ************************************ FUNCIONES ZERO-OUT FINAL ***********************************

def create_controller(target_joint):
    """
    Create FK controller using the target_joint's name.
    """
    new_controller_name = target_joint + "_ctrl"
    print("Create controller for joint " + target_joint)
    cmds.circle(c=(0,0,0), nr=(1,0,0), sw=360, r=1, d=3, ut=0, tol=0.1, s=8, ch=1, name=new_controller_name)
    return new_controller_name

def move_controller_to_target(ctrl, target_joint):
    """
    Positions controller over the target joint using a temporary parent constraint.
    """
    print("Positioning controller")
    print(ctrl)
    print(target_joint)
    parent_const = cmds.parentConstraint(target_joint, ctrl, weight=1)[0]
    cmds.delete(parent_const)

def constraint_joint_to_controller(ctrl, target_joint):
    """
    Creates constraint to control joint with controller
    """
    print("Constraining joint to controller")
    cmds.orientConstraint(ctrl, target_joint)

def setup_fk_controller(target_joint):
    """
    Sets up FK controller. Also creates contraints with the target joint.
    """
    controller_name = create_controller(target_joint)
    move_controller_to_target(controller_name, target_joint)
    grp_name = zero_out(controller_name)
    constraint_joint_to_controller(controller_name, target_joint)
    print("Done")

# *************************************** AQUÍ SE CREA LA JERARQUÍA DE CONTROLADORES FK  ***************************************
def create_controller_hierarchy(selected_joints):
    """
    Creates hierarchy of FK controllers.
    """
    print("Creating FK controllers' hierarchy")
    number_of_joints = len(selected_joints)
    for i in range(number_of_joints):
        current_joint = selected_joints[i]
        print("Current joint: " + current_joint)
        next_index = i + 1
        if(next_index < number_of_joints):
            next_joint = selected_joints[next_index]
            print("Next joint: " + next_joint)
            current_controller = current_joint + "_ctrl"
            next_group = next_joint + "_ctrl_grp"
            cmds.parent(next_group, current_controller)
            print("Parented " + next_group + " to " + current_controller)
        else:
            print("Reached last joint in the list, hierarchy completed")
    print("Created FK controllers' hierarchy")
# *************************************** AQUÍ SE CREA LA JERARQUÍA DE CONTROLADORES FK  ***************************************

def main(selected_joints):
    print("Selected joints are: " + str(selected_joints))
    for target_joint in selected_joints:
        print("Creating controller for joint " + target_joint)
        setup_fk_controller(target_joint)
    create_controller_hierarchy(selected_joints)

selected_joints = cmds.ls(sl=True)
main(selected_joints)
