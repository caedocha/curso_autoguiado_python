# Tipos de _Layouts_

## _Row Layout_

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

def delete_window_if_exists(window_name):
    if(cmds.window(window_name, q=True, exists=True)):
        cmds.deleteUI(window_name, window=True)

def main():
    # Variables de la ventana
    window_name = "row_window"
    window_width = 215
    window_height = 60
    window_title = "Row Layout"
    can_window_resize = False

    # Variables del layout
    layout_name = "row_layout"

    # Variables de los controles
    button_label = "Test"
    button_width= 50
    button_height = 50

    # Destruye la ventana si ya se había corrido el script.
    delete_window_if_exists(window_name)

    # Ventana
    cmds.window(window_name, widthHeight=(window_width, window_height), title=window_title, sizeable=can_window_resize)

    # Layout
    cmds.rowLayout(layout_name, parent=window_name, numberOfColumns=4, width=window_width, height=window_height)

    # Controles
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)

    # Mostrar ventana
    cmds.showWindow()

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
```

## _Column Layout_

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

def delete_window_if_exists(window_name):
    if(cmds.window(window_name, q=True, exists=True)):
        cmds.deleteUI(window_name, window=True)

def main():
    # Variables de la ventana
    window_name = "column_window"
    window_width = 300
    window_height = 200
    window_title = "Column Layout"

    # Variables del layout
    layout_name = "column_layout"

    # Variables de los controles
    button_label = "Test"
    button_width= 300
    button_height = 50
    can_window_resize = False

    # Destruye la ventana si ya se había corrido el script.
    delete_window_if_exists(window_name)

    # Ventana
    cmds.window(window_name, widthHeight=(window_width, window_height), title=window_title, sizeable=can_window_resize)

    # Layout
    cmds.columnLayout(layout_name, parent=window_name)

    # Controles
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)

    # Mostrar ventana
    cmds.showWindow()

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
```

## _Grid Layout_

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

def delete_window_if_exists(window_name):
    if(cmds.window(window_name, q=True, exists=True)):
        cmds.deleteUI(window_name, window=True)

def main():
    # Variables de la ventana
    window_name = "grid_window"
    window_width = 200
    window_height = 200
    window_title = "Grid Layout"

    # Variables del layout
    layout_name = "grid_layout"

    # Variables del layout
    button_label = "Test"
    button_width= 100
    button_height = 100
    can_window_resize = False

    # Destruye la ventana si ya se había corrido el script.
    delete_window_if_exists(window_name)

    # Ventana
    cmds.window(window_name, widthHeight=(window_width, window_height), title=window_title, sizeable=can_window_resize)

    # Layout
    cmds.gridLayout(layout_name, parent=window_name, numberOfColumns=2, cellWidthHeight=(button_width, button_height))

    # Controles
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)
    cmds.button(label=button_label, parent=layout_name, width=button_width, height=button_height)

    # Mostrar ventana
    cmds.showWindow()

# ************************** EL SCRIPT COMIENZA AQUI **************************
main()
```
