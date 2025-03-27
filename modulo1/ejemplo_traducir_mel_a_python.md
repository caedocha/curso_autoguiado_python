# Ejemplo: Crear manualmente _joints_ y traducir el output de MEL a Python

**MEL:**
```mel
// Crea el primer joint. Por defecto, su nombre es `joint1`
joint -p 0 0 0 ;

// Crea el segundo joint. Por defecto, su nombre es `joint2`
joint -p 0 0 1 ;

// Modifica joint `joint2` para orientarlo hacia el joint `joint1`.
// Para orientar el joint, solamente se especifico en la función el `joint1` pero
// no el `joint2`. Eso quiere decir que la función `joint` usó el joint que estaba actualmente seleccionado
// como joint hijo. Como el `joint2` estaba recién creado, ya estaba seleccionado.
// Note el parámetro `e=True` que hace que la función de joint funcione en modo "Edit".

joint -e -zso -oj yzx -sao zup joint1;

// Occure lo mismo que en el caso del joint "joint2". Crea un tercer joint y lo orienta hacia el joint "joint2".
joint -p 0 0 2 ;
joint -e -zso -oj yzx -sao zup joint2;
```

**Python:**
```python
import maya.cmds as cmds

cmds.joint(p=(0,0,0))
cmds.joint(p=(0,0,1))
cmds.joint("joint1", e=True, zso=True, oj="yzx", sao="zup")
cmds.joint(p=(0,0,2))
cmds.joint("joint2", e=True, zso=True, oj="yzx", sao="zup")
```
