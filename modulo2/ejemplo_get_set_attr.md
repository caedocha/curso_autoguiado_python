# Ejemplo para Usar las Funciones GetAttr y SetAttr

Las funciones `cmds.getAttr` y `cmds.setAttr` son muy útiles para escribir _scripts_ para hacer _tooling_ para _rig_.
En este ejemplo, se usa un atributo sencillo como es la traslación. Sin embargo, cualquier atributo de cualquier objeto puede ser usado.

No solamente los atributos, por defecto, que aparecen visibles en el _attribute editor_.

Cualquier nodo en el _graph editor_, cualquier _constraint_, cualquier atributo invisible o bloqueado, cualquier atributo _custom_, etc. Las posibilidades son ilimitadas.

*Importante:* Familiarecese con estas funciones y otras relacionadas como `addAttr`, `listAttr`, `connectAttr`, `disconnectAttr` y `attributeQuery`.


```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

En este ejemplo, se demuestra el uso de las funciones `cmds.getAttr` y `cmds.setAttr`.
Se crean 2 cubos y usando dichas funciones, se consultan los atributos de translación de uno de ellos
y se le transfieren al otro.
"""
import maya.cmds as cmds

# Las variables de los nombres de los 2 cubos.
cube_name = "myCube1"
another_cube_name = "myCube2"

# Las variables que guardan los atributos de traslación de los ejes X, Y y Z.
tx_attribute = ".translateX"
ty_attribute = ".translateY"
tz_attribute = ".translateZ"

# Se crean los 2 cubos con las varibles de nombre.
cmds.polyCube(name=cube_name)
cmds.polyCube(name=another_cube_name)

# Se mueve el primer cubo a otra posición, para poder ver una diferencia, cuando se trasfieran los valores de translación de este cubo al otro.
cmds.move(5, 2, 8, cube_name)

# La función `cmds.getAttr` permite consultar los valores de los diversos atributos de un objeto.
# En este caso se concatena el nombre del primer cubo con los 3 atributos de translación para obtener sus valores de translación que se van a guardar en variables.
cube_tx = cmds.getAttr(cube_name + tx_attribute)
cube_ty = cmds.getAttr(cube_name + ty_attribute)
cube_tz = cmds.getAttr(cube_name + tz_attribute)

# Al tener guaradados, en variables, los valores de traslación del primer cubo, se va a usar la función `cmds.setAttr` para cambiar los valores de traslación del segundo cubo.
# En este caso se concatena el nombre del segundo cubo con los 3 atributos de traslación. Adicionalmente se pasan las variables que tienen los valores de traslación del primer cubo.
cmds.setAttr(another_cube_name + tx_attribute, cube_tx)
cmds.setAttr(another_cube_name + ty_attribute, cube_ty)
cmds.setAttr(another_cube_name + tz_attribute, cube_tz)

# El resultado es que el segundo cubo se mueve a la misma posición que el primero.
```
