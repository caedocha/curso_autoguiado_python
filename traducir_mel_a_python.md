**Ejemplo: polyCube y rotate**

```mel
polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;
rotate -r -eu -fo 0 88.685659 0 ;
```

Siempre agregar `import maya.cmds as cmds` al inicio

```
import maya.cmds as cmds
```

Agregar prefijo `cmds.` al comando

```
import maya.cmds as cmds
cmds.polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;
cmds.rotate -r -eu -fo 0 88.685659 0 ;
```

Agregar paréntesis al inicio y al final de los parámetros

```
import maya.cmds as cmds
cmds.polyCube(-w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1);
cmds.rotate(-r -eu -fo 0 90 0);
```

Quitar el punto y coma (;)

```
import maya.cmds as cmds
cmds.polyCube(-w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1)
cmds.rotate(-r -eu -fo 0 90 0)
```

Separar parámetros con comas (,)

```
import maya.cmds as cmds
cmds.polyCube(-w 1, -h 1, -d 1, -sx 1, -sy 1, -sz 1, -ax 0 1 0, -cuv 4, -ch 1)
cmds.rotate(-r, -eu, -fo 0 90 0)
```

Cambiar formato de los parámetros con nombre

```
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=0 1 0, cuv=4, ch=1)
cmds.rotate(r, eu, fo=0 90 0)
```

Agregar paréntesis y comas(,) si son tuplas ( 3 números juntos)

```
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)
cmds.rotate(r, eu, fo, 0,90,0)
```

Agregar True si son booleans

```
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)
cmds.rotate(r=True, eu=True, fo=True, 0,90,0)
```

7. Cambiar la posición de los parámetros posicionales

```
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)
cmds.rotate(0, 90, 0, r=True, eu=True, fo=True)
```
