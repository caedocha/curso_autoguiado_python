"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

En este ejemplo, se explora cómo usar las funciones `cmds.select` y `cmds.ls` para seleccionar, filtrar y
listar objetos en la escena.
Ejecute cada ejemplo individualmente para ver las varias formas de seleccionar en acción.
"""
import maya.cmds as cmds

# *********** Ejemplo 1 **************
# Crea una cadena de 4 joints cuyo primer joint se llama "first_jnt"
name = "first_jnt"
cmds.joint(n=name)
cmds.joint()
cmds.joint()
cmds.joint()

# Limpiar selección. Además detiene la creación de la cadena de joints.
cmds.select(cl=True)

# Selecciona el joint por el nombre. O sea, selecciona el joint "first_jnt"
cmds.select(name) 

# **************** IMPORTANTE *********************
# Lista los objetos seleccionados. O sea, el joint "first_jnt".
# La combinación de `cmds.select` + `cmds.ls(sl=True)` es muy importante porque
# permite obtener la lista de objetos actualmente seleccionados para poder usarlos
# en el script.
objs = cmds.ls(sl=True)
print("Currently selected objects:")
print(objs)

 # Limpia la selección
cmds.select(cl=True)

# *********** Ejemplo 2 **************
# Listar todos los joints en la escena.
# Hay muchas formas de listar y filtrar objetos de la escena. Dos casos comunes son filtrar por nombre(s)
# o por tipo de objeto. Es importante familiarizarse con la documentación de `cmds.select` y `cmds.ls`.
# Cuentan con muchos parámetros para seleccionar y listar de diversas formas.
objs2 = cmds.ls(type="joint")
print("Currently selected objects:")
print(objs2)

 # Limpia selección
cmds.select(cl=True)

# *********** Ejemplo 3 **************
# Selecciona jerarquía
cmds.select(name, hi=True) 
objs3 = cmds.ls(sl=True)
print("Currently selected objects:")
print(objs3)
