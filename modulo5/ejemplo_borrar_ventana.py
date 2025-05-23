"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Ejemplo para borrar la ventana antes de recrearla cuando se corre el script múltiples veces.
"""

import maya.cmds as cmds

def delete_window_if_exists(windowName):
    # Se valida si la ventana ya ha sido creada anteriormente con
    # la función `cmds.window` en modo de query(q) y el parámetro
    # booleano `exists`.
    if(cmds.window(windowName, q=True, exists=True)):
        # Si la ventana si existe, entonces se borra.
        print("Found old window from previous runs. Deleting it.")
        cmds.deleteUI(windowName, window=True)

def main():
    print("Creating simple UI")

    # Las variables de los nombres de los controles para poder identificarlos.
    sliderName = "slider"
    textboxName = "textbox"
    checkboxName = "checkbox"
    windowName = "mainWindow"

    # Antes de crear la interfaz gráfica, primero verifique que la ventana no
    # exista por corridas anteriores del script. Pero si existe, bórrela para
    # comenzar desde cero.
    delete_window_if_exists(windowName)

    # La ventana es el contendor principal. Siempre hay que empezar creándola.
    win = cmds.window(windowName, title="Simple UI",rtf=True)

    # Se crea un layout de columnas. Noten que para asoaciarlo a la ventana, al layout
    # se le pasa el párametro parent(p) con el nombre de la ventana.
    # Esto indica que layout va adentro de la ventana.
    layout = cmds.columnLayout(p=win, w=300, h=200,cat=("left",10),rs=10)

    # Se crean controladores de varios tipos. Noten que a los controles se les indica
    # a quién pertenecen con el parámetro parent(p) pero en este caso el "papá" es el layout.
    cmds.floatSliderGrp(sliderName, p=layout,label="Slider",w=280,min=0,max=100,value=50,step=1,field=True,cal=[1,"left"])
    cmds.textFieldGrp(textboxName, p=layout,h=50,label="Textbox",w=280,cal=[1,"left"])
    cmds.checkBox(checkboxName,p=layout,l="Checkbox",w=280,enable=True)
    cmds.button(p=layout,h=50,w=280,l="Button")

    # Después de agregar el layout y los controles, se muestra la ventana.
    cmds.showWindow(win)
    print("Done")

main()
