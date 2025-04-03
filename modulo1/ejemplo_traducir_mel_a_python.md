# Ejemplo: Crear manualmente _joints_ y traducir el output de MEL a Python

En este ejemplo se muestra cómo traducir, de MEL a Python, la creación de una cadena de 3 _joints_.
Se asume que el código MEL se obtuvo del _script editor_ luego de haber creado la cadena de _joints_ manualmente.
Ambos ejemplos, el de MEL y el Python, están listos para ser copiados y pegados en el _script editor_ por si desea experimentar con ellos.

**MEL:**
```mel
/*
---- Crear primer joint ----
Se crea el primer joint en la posición (0,0,0). Por defecto, su nombre es `joint1`.
*/
joint -p 0 0 0 ;

/*
---- Crear segundo joint ----
Se crea el segundo joint en la posición (0,0,1). Por defecto, su nombre es `joint2`.
*/
joint -p 0 0 1 ;

/*
---- Joint en modo Edit ----
Se modifica el joint `joint2` para orientarlo hacia el joint `joint1`.
Note el parámetro `-e` que hace que la función de joint funcione en modo "Edit".
---- Orientar joint ----
Para orientar el joint, solamente se especifica el `joint1` pero no el `joint2`.
Eso quiere decir que la función joint usa el joint que esta actualmente seleccionado
como joint que tiene que ser orientado.
Como se acaba de crear el `joint2`, se selecciona automáticamente.
---- Parametros ----
Los valores de los parámetros `-zso`, `-oj`, `-sao` van a depender de las opciones
que se seleccionaron en la menú para crear _joints_. Usen la documentación de la función joint
para conocer mas sobre estos parámetros.
*/
joint -e -zso -oj yzx -sao zup joint1;

/*
---- Crear y orientar tercer joint ----
Se crea y orienta el tercer joint en la posición (0,0,2). Por defecto su nombre es `joint3`.
*/
joint -p 0 0 2 ;
joint -e -zso -oj yzx -sao zup joint2;
```

**Python:**
```python
import maya.cmds as cmds

"""
---- Crear primer joint ----
Note el uso de tuplas para definir la posición del joint.
"""
cmds.joint(p=(0,0,0))

# ---- Crear segundo joint ----
cmds.joint(p=(0,0,1))

"""
---- Orientar segundo joint ----
Note la diferencia entre párametros posicionales y por nombre.
"joint1" es un parámetro posicional que identifica el joint papá.
"""
cmds.joint("joint1", e=True, zso=True, oj="yzx", sao="zup")

"""
---- Crear y orientar tercer joint ----
Se crea y orienta el tercer joint en la posición (0,0,2). Por defecto su nombre es `joint3`.
"""
cmds.joint(p=(0,0,2))
cmds.joint("joint2", e=True, zso=True, oj="yzx", sao="zup")
```
