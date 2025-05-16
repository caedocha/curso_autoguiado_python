# Operadores Relacionales

## Igualdad (==)

```python
import maya.cmds as cmds
obj = cmds.ls(sl=True)[0]
result = obj == "joint1"
print("Is selected object 'joint1'? " + str(result))
```

## Diferencia (!=)

```python
```

## Mayor a (>)

```python
import maya.cmds as cmds
obj = cmds.ls(sl=True)
result = len(obj) > 0

print("Are there any objects selected? " + str(result))
```

## Mayor o Igual a (>=)

```python
import maya.cmds as cmds
obj = cmds.ls(sl=True)
result = len(obj) >= 1

print("Are there any objects selected? " + str(result))
```

## Menor a (<)

```python
```

## Menor o Igual a (<=)

```python
```
