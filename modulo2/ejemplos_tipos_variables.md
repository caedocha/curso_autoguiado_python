# Ejemplos de Tipos de Variables

## _Strings_ o Cadenas de Caracteres Alfanuméricos



```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

cube_name = "mi_cubito"
cmds.polyCube(name = cube_name)
```

## Números Enteros o _Integers_, en Inglés

```python
"""
Este ejemplo usa 3 variables con números enteros dentro para mover un cubo a una posición específica.
"""
import maya.cmds as cmds

# Las 3 variables con enteros que representan los valores de traslación en los ejes X, Y y Z.
tx = 1
ty = 2
tz = 3

# Se crea un cubo. Su nombre es retornado por la función `cmds.polyCube` y se guarda en la variable `cube`.
cube = cmds.polyCube()

# A la función `cmds.move`, se le especifica la posición a donde se debe mover el cubo con las variables `tx`, `ty` y `tz`.
# Además, se pasa el nombre del cubo para especificar que el objeto que hay que mover es este.
cmds.move(tx, ty, tz, cube)
```

## Números con punto flotante o _Floats_, en Inglés

```python
"""
Este ejemplo rota un cubo 33.33 grados en los ejes X, Y y Z.
"""
import maya.cmds as cmds

# La variable con un _float_ que define el ángulo de rotación. El mismo ángulo se va a usar para los 3 ejes por lo que solo se va a usar una variable.
rotation_angle = 33.33

# Se crea el cubo y se guarda el nombre en la variable `cube`.
cube = cmds.polyCube()

# Se rota el cubo, utilizando la variable `rotation_angle` en los 3 ejes. Se especifica el nombre del cubo para que la función sepa que debe rotar este objeto.
cmds.rotate(rotation_angle, rotation_angle, rotation_angle, cube)
```

## Booleanos

```python
"""
En este ejemplo se crea una cadena de 4 joints.
Se detiene la creación de la cadena usando la función `cmds.select` con el parámetro `deselect(d)`.
Deseleccionar los joints simula estripar la tecla "Enter" cuando la cadena de joints se crea manualmente.
"""
import maya.cmds as cmds

# La variable guarda un booleano que le indicara a `cmds.select` que debe deseleccionar los objetos seleccionados, o sea los 4 joints.
deselect = True

# Se crea una cadena de 4 joints.
cmds.joint()
cmds.joint()
cmds.joint()
cmds.joint()

# Se deselecciona la cadena de joints y con esto se detiene la creación de la cadena.
cmds.select(d=deselect)

# Si se comenzara a crear una nueva cadena de joints después de deseleccionar la cadena anterior, la cadena nueva sería una nueva, independiente de la anterior.
```

## Listas

```python
"""
Esta sección tiene 2 ejemplos de listas.
El primer ejemplo usa una lista de nombres para crear 3 cubos y luego mueve los cubos a una posición.
El segundo ejemplo, hace algo similar. Usando la función `cmds.select` con el parámetro `all(a)`, selecciona todo lo que está en la escena.
Luego con la función `cmds.ls` con el parámetro `select(sl)`, lista los objetos seleccionados, o sea, los 3 cubos.
Con esta lista, mueve los cubos a otra posición.
"""

# *********** Ejemplo 1 **************
import maya.cmds as cmds

# La variable guarda una lista con 3 nombres.
cube_names = ["cube1", "cube2", "cube3"]

# Esta es una forma de sacar valores individuales de una lista. Aprenderemos más sobre esto en el módulo 3.
# Por el momento, solo deben entender que `cube_names[0]` devuelve el valor "cube1", `cube_names[1]` devuelve el valor "cube2" y así sucesivamente.
cmds.polyCube(n=cube_names[0])
cmds.polyCube(n=cube_names[1])
cmds.polyCube(n=cube_names[2])

# Se mueven los 3 cubos a la misma posición. La posición es X:1, Y:2, Z:3.
cmds.move(1,2,3,cube_names)

# *********** Ejemplo 2 **************

# Con este parámetro, `cmds.select` selecciona todos los objetos en la escena. O sea, los 3 cubos ya creados.
cmds.select(all=True)

# La función `cmds.ls` se usa para listar objetos. Cuando se usa con el parámetro `sl`, devuelve una lista de los objetos actualmente seleccionados. O sea, los nombres de los 3 cubos.
cubes = cmds.ls(sl=True)

# Se mueven de nuevo los 3 cubos a otra posición. La posición es X:3, Y:2, Z:1.
cmds.move(3,2,1,cubes)
```

## Tuplas

```python
"""
En este ejemplo, se crea un joint en una posición definida por una tupla que representa las coordenadas en los ejes X, Y y Z.
"""
import maya.cmds as cmds

# Esta variable es una tupla que representa las coordenadas en los ejes X, Y y Z.
joint_position = (2,2,2)

# Se crea un joint. Su posición será en X:2, Y:2 y Z:2.
cmds.joint(position=joint_position)
```


