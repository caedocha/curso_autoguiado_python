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
    # El zero-out se modificó para que retornara el nombre del grupo.
    return grp_name

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
    # Se retorna una lista con los nombres del controlador y el grupo.
    return [controller_name, grp_name]

# *************************************** AQUÍ SE CREA LA JERARQUÍA DE CONTROLADORES FK  ***************************************
def create_controller_hierarchy(all_ctrls_and_grps):
    """
    Creates hierarchy of FK controllers.
    """
    # La lista de grupos y controladores luce algo similar a esto:
    #            grupo             ,        controlador      ,         grupo            ,       controlador    ,           grupo          ,     controlador
    # ['jnt_r_shoulder_fk_ctrl_grp', 'jnt_r_shoulder_fk_ctrl', 'jnt_r_elbow_fk_ctrl_grp', 'jnt_r_elbow_fk_ctrl', 'jnt_r_wrist_fk_ctrl_grp', 'jnt_r_wrist_fk_ctrl']
    number_of_objs = len(all_ctrls_and_grps)
    print("Groups and FK controllers to create hierarchy:")
    print(all_ctrls_and_grps)
    # El ciclo recorre toda la lista de grupos y controladores para "parentear" cada grupo con el controlador que le antecede.
    # Se utiliza la función `range` en vez de recorrer la lista directamente porque en cada iteración se debe buscar también
    # el objeto que le sigue para poder hacer el "parent".
    for i in range(number_of_objs):
        obj = all_ctrls_and_grps[i]
        parts = obj.split("_")
        print("Current obj: " + obj)
        # Solo se crea el "parent" si el objeto de la iteracién actual es un controlador.
        if(parts[len(parts) - 1] == "ctrl"):
            # Obtiene el índice de la siguiente iteración.
            next_index = i + 1
            # Verifica que exista un objeto en el siguiente índice.
            # Si el próximo índice es mayor al total de objetos en la lista,
            # quiere decir que el ciclo llegó al final y puede terminar.
            if(next_index < number_of_objs):
                # Obtiene el siguiente objeto. En este caso se trata de un grupo.
                next_obj = all_ctrls_and_grps[next_index]
                print("Next obj: " + next_obj)
                # "Parentea" el grupo con el controlador.
                cmds.parent(next_obj, obj)
                print("Parented " + next_obj + " to " + obj)
# *************************************** AQUÍ SE CREA LA JERARQUÍA DE CONTROLADORES FK  ***************************************

def main(selected_joints):
    print("Selected joints are: " + str(selected_joints))
    all_ctrls_and_grps = []
    for target_joint in selected_joints:
        print("Creating controller for joint " + target_joint)
        controller_and_group = setup_fk_controller(target_joint)
        grp = controller_and_group[1]
        ctrl = controller_and_group[0]
        all_ctrls_and_grps.append(grp)
        all_ctrls_and_grps.append(ctrl)
    create_controller_hierarchy(all_ctrls_and_grps)

selected_joints = cmds.ls(sl=True)
main(selected_joints)
