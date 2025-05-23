"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Ejemplo para crear una interfaz grafica para hacer zero-out.
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


# Esta es la función que se asocia con el botón.
# Se va a ejecutar cada vez que al botón se le haga click.
# Un detalle especial es que para poder estar asociado al botón
# debe recibir este parámetro `*args`.
# En este curso no ahondaremos en cómo funcionan este tipo de parámetros.
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

def delete_window_if_exists(window_name):
    if(cmds.window(window_name, q=True, exists=True)):
        print("Found old window from previous runs. Deleting it.")
        cmds.deleteUI(window_name, window=True)

def create_gui(window_name):
    win = cmds.window(window_name, title="Zero-out!",rtf=True)
    layout = cmds.columnLayout(p=win, w=300, h=200,cat=("left",10),rs=10)
    cmds.separator(p=layout, vis=True)
    cmds.text(p=layout, w=280, align="center", l="Select the controllers you want to zero-out and then click the button", ww=True)

    # ******************* IMPORTANTE: ********************
    # Note como ahora al botón se le pasa, en el parámetro `command`, el nombre de la función de `zero_out_main`.
    cmds.button(p=layout,h=50,w=280,l="Zero-out controller(s)", command=zero_out_main)
    cmds.showWindow(win)

def main():
    print("Creating zero-out GUI")
    window_name = "zeroOutWindow"
    delete_window_if_exists(window_name)
    create_gui(window_name)
    print("Done")

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
