#Ejemplos de funciones de las listas

## range

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra cómo se usa la función `range` para crear una fila de cubos.
"""
import maya.cmds as cmds

# Este ciclo itera 10 veces. La variable "x" guarda el número de la iteración, comenzando en 0.
# La variable "x" va a tener los valores: 0,1,2,3,4...
for x in range(10):
    # Se crea el cubo.
    cmds.polyCube()
    # El cubo se mueve usando la variable "x".
    # Como "x" aumenta en cada iteración, se usa para mover, poco a poco, cada cubo nuevo.
    # El valor de "x" se multiplica por 2 para crear espacio entre los cambios.
    # De lo contrario, quedarían pegados.
    cmds.move(x*2,0,0)
```

## append

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra cómo se usa la función `append` para crear una cadena de joints y orientarlos.

IMPORTANTE:
La función para orientar los joints se consiguió al orientar manualmente los joints y revisar
el output del script editor.
"""

# La variable donde se guardan los nombres de los joints.
joints = []
# Las variables para orientar los joints.
orientation = "yxz"
secondaryAxisOrient = "xup"

# Se crea la cadena de joints y se guardan los nombres de los joints.
for i in range(3):
    jnt = cmds.joint(position=(i,0,0))
    joints.append(jnt)

# Los joints se seleccionan para poder ser orientados.
# No se pueden orientar los joints individualmente. La cadena ya debe estar completa.
cmds.select(joints) 
# Para orientar los joints, se ejecuta la funcion joint en modo "edit".
# Los demás parámetros dependen de las opciones que se seleccionaron en el menú para orientar joints.
cmds.joint(edit=True, oj=orientation, secondaryAxisOrient=secondaryAxisOrient, ch=True, zso=True)
```
