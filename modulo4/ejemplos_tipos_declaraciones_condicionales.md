# Declaraciones condicionales

## If

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

targetJoint = cmds.ls(sl=True)[0]
newControllerName = targetJoint + "_ctrl"
groupName = newControllerName + "_grp"

if(cmds.objExists(newControllerName)):
    print("Reseting things if controller already exists")
    print("Deleting controller " + newControllerName + " and group " + groupName)
    cmds.delete(newControllerName)
    cmds.delete(groupName)

print("Continue with the creation of the FK controller ...")
```

## If/Else

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

objs = cmds.ls(sl=True)

if(len(objs) < 1):
    print("No objects selected, sorry, I can't execute this cool script!")
else:
    print("Awesome! objects are selected. I can execute this cool script!")
```


## If/Elif/Else

```python
"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""

import maya.cmds as cmds

print("Try out different shapes, you can pick circle, square, cube, sphere or set your own shape and see what happens!")
shape = "circle"
print("The selected shape is: " + shape)

if(shape == "circle"):
    print("Creating a circle")
    cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=1, d=3, ut=0, tol=0.1, s=8, ch=1)
elif(shape == "square"):
    print("Creating a square")
    cmds.nurbsSquare(c=(0,0,0), nr=(0,1,0), sl1=1, sl2=1, sps=1, d=3, ch=1)
elif(shape == "cube"):
    print("Creating a cube")
    cmds.polyCube()
elif(shape == "sphere"):
    print("Creating a sphere")
    cmds.polySphere()
else:
    print("Whoops! I didn't recognize the shape, I will create circle by default")
    cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=1, d=3, ut=0, tol=0.1, s=8, ch=1)
```
