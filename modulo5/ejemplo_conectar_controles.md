# Cómo Conectar Botones a Funciones

Conectar los botones con las funciones que han escrito es fácil.

La función `cmds.button` tiene un parámetro llamada `command(c)` que recibe la función que debe ejecutar cuando se le hace _click_ al botón.

A este parámetro se le puede pasar la función para hacer _zero-out_, para crear cadenas de _joints_, para crear controladores, etc. Las posibilidades son ilimitadas.

Aquí se presenta una _script_ que imprime en el _output_ del _script editor_ un mensaje.

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Ejemplo para conectar los botones con una función.
"""

import maya.cmds as cmds

def hello(*args):
    print("Hello!")

def main():
    print("Creating simple GUI")

    # VENTANA
    win = cmds.window(title="Connect button with hello function",rtf=True, sizeable=False, widthHeight=(370,60))

    # LAYOUT
    layout = cmds.columnLayout(p=win, cat=("left",10),rs=10)

    # CONTROLES
    cmds.button(p=layout,h=50,w=350,l="Say hello!", command=hello)

    # MOSTRAR VENTANA
    cmds.showWindow(win)
    print("Done")

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
```
