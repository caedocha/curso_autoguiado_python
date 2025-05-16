# Operadores Relacionales

## Igualdad (==)

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

obj = cmds.ls(sl=True)[0]
result = obj == "joint1"
print("Is selected object 'joint1'? " + str(result))
```

## Diferencia (!=)

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

obj = cmds.ls(sl=True)[0]
result = obj != "joint1"
print("Is selected NOT object 'joint1'? " + str(result))

```

## Mayor a (>)

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

obj = cmds.ls(sl=True)
result = len(obj) > 0

print("Are there any objects selected? " + str(result))
```

## Mayor o Igual a (>=)

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

obj = cmds.ls(sl=True)
# Para seguir contestando la pregunta de si hay objetos seleccionados,
# se debe variar un poco la condición.
result = len(obj) >= 1

print("Are there any objects selected? " + str(result))
```

## Menor a (<)

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

cubito = "mi_cubito"
cmds.polyCube(name = cubito)
cmds.move(1,0,0)
tx = cmds.getAttr(cubito + ".tx")
result = tx < 1

print("Is mi_cubito's tx less than 1? " + str(result))
```

## Menor o Igual a (<=)

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

cubito = "mi_cubito"
cmds.polyCube(name = cubito)
cmds.move(1,0,0)
tx = cmds.getAttr(cubito + ".tx")
result = tx <= 1

print("Is mi_cubito's tx less than or equal 1? " + str(result))
```
