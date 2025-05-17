"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Esta solución muestra cómo orientar el joint de la muñeca usando la opción "Orient joint to world".
"""
import maya.cmds as cmds

# Las variables para crear y orientar los joints.
side = "r"
orientation = "xyz"
secondaryAxisOrient = "zdown"
chain_types = ["ik", "fk", "bind"]

# Lista los locators seleccionados.
locators = cmds.ls(sl=True)

# Limpia la selección de objetos.
cmds.select(cl=True)

# Itera sobre cada tipo de cadena para ir creando una por una.
for type in chain_types:
    # La variable `non_wrist_joints` va a guardar la lista de joints que no son el de la muñeca.
    # La variable `wrist_jnt` va a guardar el nombre del joint de la muñeca.
    non_wrist_joints = []
    wrist_jnt = ""
    # Itera sobre cada uno de los joints para ir creando los joints en la misma posición de cada locator.
    for loc in locators:
        # Obtiene los valores de traslación del locator.
        tx = cmds.getAttr(loc+".tx")
        ty = cmds.getAttr(loc+".ty")
        tz = cmds.getAttr(loc+".tz")
        # Crea una tupla con los valores de traslación para pasarselo al parámetro de posición de `cmds.joint`.
        jnt_pos = (tx, ty, tz)
        # Crea el nombre del joint que va a ser creado.
        jnt_name = "jnt_" + side + "_" + loc + "_" + type
        # Crea el joint.
        cmds.joint(n=jnt_name, p=jnt_pos)
        # Valida si el locator NO es el de la muñeca. Si es True, guarda el nombre del joint en la lista de joints
        # que no son de muñeca.
        if(loc != "wrist"):
            non_wrist_joints.append(jnt_name)
        else:
            # Si es False, guarda el nombre del joint en otra variable para saber fácilmente cuál es el joint que hay
            # que orientar con la opción de "Orient joint to world".
            wrist_jnt = jnt_name
    # Selecciona los joints no-muñeca.
    cmds.select(non_wrist_joints) 
    # Orienta los joints con el orden de rotación especificado.
    cmds.joint(edit=True, oj=orientation, secondaryAxisOrient=secondaryAxisOrient, ch=True, zso=True)
    # Limpia la selección para orientar el joint de muñeca.
    cmds.select(cl=True)
    # Selecciona el joint de muñeca.
    cmds.select(wrist_jnt)
    # Orienta el joint de la muñeca con la opción de "Orient joint to world".
    cmds.joint(edit=True, oj="none", ch=True, zso=True)
    # Limpia la selección.
    cmds.select(cl=True)
