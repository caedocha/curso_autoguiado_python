# Ejemplo Para Crear un Controlador y un Grupo Usando Concatenación

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

En este ejemplo, se crea un controlador y un grupo sencillo para demostrar el uso de la concatenación
para definir nombres de objetos del rig basados en otros objetos.
"""
import maya.cmds as cmds

# Se define el nombre del controlador.
controller_name = "fk_shoulder_ctrl"

# Usando la concatenación, se define el nombre del grupo, que es la combinación entre el nombre del controlador más el sufijo "_grp".
# El nombre resultante es "fk_shoulder_ctrl_grp".
group_name = controller_name + "_grp"

# Se crea el círculo que funcionará de controlador FK.
cmds.circle(name=controller_name)

# Se crea el grupo con el nombre concatenado. Automáticamente, `cmds.group` agrupa lo que haya seleccionado.
# Como el controlador lo estaba, se agrupa automáticamente bajo este grupo.
cmds.group(name=group_name)
```
