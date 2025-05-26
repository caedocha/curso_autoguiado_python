"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Solución para crear una GUI para correr script que automatizan algunas partes del rig de un brazo.
"""

import maya.cmds as cmds

def main():
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
    cmds.button(p=layout,h=button_height,w=button_width,l="Create IK/FK/Bind joint chains")
    cmds.button(p=layout,h=button_height,w=button_width,l="Create FK controller(s)")
    cmds.button(p=layout,h=button_height,w=button_width,l="Zero-out")

    # MOSTRAR VENTANA
    cmds.showWindow(win)
    print("Done")

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
