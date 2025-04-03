# Ejemplo: polyCube y rotate**

Este ejemplo muestra cómo traducir un _snippet_ de código de MEL a Python, paso a paso.

Iniciaremos con este _snippet_ de código de MEL que crea un cubo y luego lo rota 45 grados en los ejes X, Y y Z:

```mel
polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;
rotate -r -eu -fo 45 45 45 ;
```

Vamos a aplicar, paso a paso,los cambios de la guía "Cómo traducir comandos de MEL a Python" para ir convirtiendo poco a poco el código MEL a Python.

1. Siempre agregue `import maya.cmds as cmds` al inicio:

```python
import maya.cmds as cmds
```

2. Agregue el prefijo `cmds.` a las funciones:

```python
import maya.cmds as cmds
cmds.polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;
cmds.rotate -r -eu -fo 45 45 45 ;
```

3. Agregue paréntesis al inicio y al final de los parámetros:

```python
import maya.cmds as cmds
cmds.polyCube(-w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1);
cmds.rotate(-r -eu -fo 45 45 45);
```

4. Borre el punto y coma (;):

```python
import maya.cmds as cmds
cmds.polyCube(-w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1)
cmds.rotate(-r -eu -fo 45 45 45)
```

5. Separe parámetros con comas (,):

```python
import maya.cmds as cmds
cmds.polyCube(-w 1, -h 1, -d 1, -sx 1, -sy 1, -sz 1, -ax 0 1 0, -cuv 4, -ch 1)
cmds.rotate(-r, -eu, -fo 45 45 45)
```

6. Cambie formato de los parámetros con nombre:

```python
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=0 1 0, cuv=4, ch=1)
cmds.rotate(r, eu, fo, 45, 45, 45)
```

6.1 Agregue paréntesis y comas(,) si son tuplas (3 números juntos):

```python
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)
cmds.rotate(r, eu, fo, 45, 45, 45)
```

6.2 Agregue `True` si son booleanos (parámetros sin un valor a su lado):

```python
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)
cmds.rotate(r=True, eu=True, fo=True, 45, 45, 45)
```

7. Cambie la posición de los parámetros posicionales:

```python
import maya.cmds as cmds
cmds.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)
cmds.rotate(45, 45, 45, r=True, eu=True, fo=True)
```

El código de Python final hace lo mismo que el código original de MEL. Pueden probar correrlo en el _script editor_.


