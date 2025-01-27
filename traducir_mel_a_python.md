**Ejemplo: polyCube y rotate**

```mel
polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;
rotate -r -eu -fo 0 88.685659 0 ;
```

Siempre agregar `import maya.cmds as cmds` al inicio

```python
import maya.cmds as cmds
```

Agregar prefijo `cmds.` al comando

```python
import maya.cmds as cmds
cmds.polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;
cmds.rotate -r -eu -fo 0 88.685659 0 ;
```

Agregar paréntesis al inicio y al final de los parámetros

```python
import maya.cmds as cmds
cmds.polyCube(-w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1);
cmds.rotate(-r -eu -fo 0 90 0);
```

Quitar el punto y coma (;)

```python
import maya.cmds as cmds
cmds.polyCube(-w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1)
cmds.rotate(-r -eu -fo 0 90 0)
```

Separar parámetros con comas (,)

```python
import maya.cmds as cmds
cmds.polyCube(-w 1, -h 1, -d 1, -sx 1, -sy 1, -sz 1, -ax 0 1 0, -cuv 4, -ch 1)
cmds.rotate(-r, -eu, -fo 0 90 0)
```

Cambiar formato de los parámetros con nombre

```python
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=0 1 0, cuv=4, ch=1)
cmds.rotate(r, eu, fo=0 90 0)
```

Agregar paréntesis y comas(,) si son tuplas (3 números juntos)

```python
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)
cmds.rotate(r, eu, fo, 0,90,0)
```

Agregar True si son booleanos (parámetros sin un valor a su lado)

```python
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)
cmds.rotate(r=True, eu=True, fo=True, 0,90,0)
```

Cambiar la posición de los parámetros posicionales

```python
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)
cmds.rotate(0, 90, 0, r=True, eu=True, fo=True)
```
