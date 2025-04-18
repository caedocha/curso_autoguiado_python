# Ejemplos de Tipos de Variables

## Suma
```python
"""
En este ejemplo se crea un cubo y se mueve en el eje X. Luego a ese valor se le suma otro para moverlo un poco más.
"""
import maya.cmds as cmds

# Se crea el cubo y se selecciona automáticamente.
cmds.polyCube()

# Se define una variable que guarda el cantidad que se va a mover el cubo en el eje X.
pos_x = 1

# Los valores de los ejes Y y Z se dejan en 0 porque no se van a usar en este ejercicio.
cmds.move(pos_x, 0, 0)

# Se sobreescribe el valor de `pos_x` con la suma de `pos_x` más 5. O sea, la suma es 1 + 5.
pos_x = pos_x + 5

# Se mueve de nuevo el cubo a la nueva posición.
cmds.move(pos_x, 0, 0)
```

## Resta
```python
"""
Este ejemplo es similar al del de suma, se crea un cubo y se mueve. La diferencia es que se movera hacia atras ya que se resta el valor de la posicion.
"""

import maya.cmds as cmds

# Se crea el cubo y se selecciona automáticamente.
cmds.polyCube()

# Se define una variable que guarda el cantidad que se va a mover el cubo en el eje X.
pos_x = 10

# Los valores de los ejes Y y Z se dejan en 0 porque no se van a usar en este ejercicio.
cmds.move(pos_x, 0, 0)

# Se sobreescribe el valor de `pos_x` con la resta de `pos_x` menos 9. O sea, la resta es 10 - 9.
pos_x = pos_x - 9

# Se mueve de nuevo el cubo a la nueva posición.
cmds.move(pos_x, 0, 0)
```

## División
```python
"""
En este ejemplo, se crea un cubo. Luego se agranda y encoge usando la division.
Corra este script en 2 partes para ver los efectos de los cambios de escala.
"""
import maya.cmds as cmds

# ************** Parte 1 ************** 
# Se crea el cubo y se selecciona automáticamente.
cmds.polyCube()

# La variable guarda el valor de agrandamiento.
scale = 20

# Cuando se escala el cubo, se usa la misma escala en los ejes X, Y y Z para mantener la uniformidad.
cmds.scale(scale, scale, scale)

# ************** Parte 2 ************** 

# Se divide el valor actual de `scale` por 10. O sea, se divide 20 / 10.
scale = scale / 10

# Se encoje el cubo.
cmds.scale(scale, scale, scale)
```

## Multipliación
```python
"""
Este ejemplo es similar al de la división. Se crea un cubo, se agranda y luego se vuelve a agrandar usando la multiplicación.
Corra este script en 2 partes para ver los efectos de los cambios de escala.
"""
import maya.cmds as cmds

# ************** Parte 1 ************** 
# Se crea el cubo y se selecciona automáticamente.
cmds.polyCube()

# La variable guarda el valor de agrandamiento.
scale = 20

# Cuando se escala el cubo, se usa la misma escala en los ejes X, Y y Z para mantener la uniformidad.
cmds.scale(scale, scale, scale)

# ************** Parte 2 ************** 

# Se multiplica el valor actual de `scale` con 10. O sea, se multipla 20 * 10.
scale = scale * 10

# Se agranda otra vez el cubo.
cmds.scale(scale, scale, scale)
```
