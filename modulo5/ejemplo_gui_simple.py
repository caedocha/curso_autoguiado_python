"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Ejemplo para crear una interfaz gráfica simple.
"""

import maya.cmds as cmds

def main():
    print("Creating simple UI")

    # Las variables de los nombres de los controles para poder identificarlos.
    slider_name = "slider"
    textbox_name = "textbox"
    checkbox_name = "checkbox"

    #
    # VENTANA
    #
    # La ventana es el contendor principal. Siempre hay que empezar creándola.
    win = cmds.window(title="Simple UI",rtf=True)

    #
    # LAYOUT
    #
    # Se crea un layout de columnas. Noten que para asoaciarlo a la ventana, al layout
    # se le pasa el párametro parent(p) con el nombre de la ventana.
    # Esto indica que layout va adentro de la ventana.
    layout = cmds.columnLayout(p=win, w=300, h=200,cat=("left",10),rs=10)

    #
    # CONTROLES
    #
    # Se crean controladores de varios tipos. Noten que a los controles se les indica
    # a quién pertenecen con el parámetro parent(p) pero en este caso el "papá" es el layout.
    cmds.floatSliderGrp(slider_name, p=layout,label="Slider",w=280,min=0,max=100,value=50,step=1,field=True,cal=[1,"left"])
    cmds.textFieldGrp(textbox_name, p=layout,h=50,label="Textbox",w=280,cal=[1,"left"])
    cmds.checkBox(checkbox_name,p=layout,l="Checkbox",w=280,enable=True)
    cmds.button(p=layout,h=50,w=280,l="Button")

    #
    # MOSTRAR VENTANA
    #
    # Después de agregar el layout y los controles, se muestra la ventana.
    cmds.showWindow(win)
    print("Done")

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
