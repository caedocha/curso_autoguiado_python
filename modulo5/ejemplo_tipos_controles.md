# Tipos de Controles

## Botón

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Ejemplo para crear una interfaz gráfica con un botón.
"""

import maya.cmds as cmds

def main():
    print("Creating simple GUI")

    #
    # VENTANA
    #
    win = cmds.window(title="Simple GUI with a button",rtf=True, sizeable=False, widthHeight=(370,60))

    #
    # LAYOUT
    #
    layout = cmds.columnLayout(p=win, cat=("left",10),rs=10)

    #
    # CONTROLES
    #
    cmds.button(p=layout,h=50,w=350,l="Mi botóncito")

    #
    # MOSTRAR VENTANA
    #
    cmds.showWindow(win)
    print("Done")

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
```

## _Text_

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Ejemplo para crear una interfaz gráfica con un control de texto.
"""

import maya.cmds as cmds

def main():
    print("Creating simple GUI")

    #
    # VENTANA
    #
    win = cmds.window(title="Simple GUI with text",rtf=True, sizeable=False, widthHeight=(370,60))

    #
    # LAYOUT
    #
    layout = cmds.columnLayout(p=win, cat=("left",10),rs=10)

    #
    # CONTROLES
    #
    cmds.text(p=layout, w=280, align="center", l="Mi texto de prueba", ww=True)

    #
    # MOSTRAR VENTANA
    #
    cmds.showWindow(win)
    print("Done")

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
```
