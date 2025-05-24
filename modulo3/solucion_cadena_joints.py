"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Esta solución muestra cómo crear 3 cadenas de joints IK, FK y BIND en la misma posición de 3 locators creados previamente.
Este script asume que los locators están seleccionados antes de correr el script.
"""
import maya.cmds as cmds

# Las variables que se van a usar para crear y orientar las 3 cadenas de joints.
side = "r"
orientation = "xyz"
secondaryAxisOrient = "yup"
chain_types = ["ik", "fk", "bind"]

# Se listan los locators seleccionados.
locators = cmds.ls(sl=True)

# Se deseleccionan los objetos seleccionados para comenzar desde cero la creación de las cadenas.
cmds.select(cl=True)

# Se van a usar 2 ciclos: El ciclo interior itera sobre cada uno de los locators para ir creando
# los joints. El ciclo exterior itera sobre la lista `chain_types` para crear 3 cadenas iguales
# utilizando el valor de la lista para nombrarlas diferentemente.
for type in chain_types: 
    # La lista vacía `jnts` se usa para guardar los joints recién creados de cada cadena para luego
    # orientarlos al final de la iteración.
    jnts = []
    for loc in locators:
        # Se toman los atributos de translación del locator `loc`.
        tx = cmds.getAttr(loc+".tx")
        ty = cmds.getAttr(loc+".ty")
        tz = cmds.getAttr(loc+".tz")
        # Se crea una tupla con esos valores.
        jnt_pos = (tx, ty, tz)
        # Se crea el nombre del joint.
        jnt_name = "jnt_" + side + "_" + loc + "_" + type
        # Se crea el joint.
        cmds.joint(n=jnt_name, p=jnt_pos)
        # Se agrega el joint recién creado a la lista de joints que van a ser orientados al final del ciclo interior.
        jnts.append(jnt_name)
    # Se seleccionan los joints de la lista `jnts`.
    cmds.select(jnts) 
    # Se orientan los joints. Como una prueba, puede orientar manualmente los joints teniendo el script editor abierto
    # para ver este mismo código.
    cmds.joint(edit=True, oj=orientation, secondaryAxisOrient=secondaryAxisOrient, ch=True, zso=True)
    # Se deselecciona todo para comenzar desde cero en la siguiente cadena de joints.
    cmds.select(cl=True)
