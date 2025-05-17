"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************

Este ejemplo muestra la solución para crear los constraints entre las cadenas de joints IK y FK y la cadena de bind.
"""
import maya.cmds as cmds

# Se asume que los joints siguen una nomenclatura definida por uno como rigger.
joints = ["jnt_r_shoulder", "jnt_r_elbow", "jnt_r_wrist"]

# Se itera sobre la lista de `joints`.
print("Creating parent constraints")
for jnt in joints:
    # Se divide el nombre del joint por el carácter "_".
    # La nomenclatura que se usa en este ejemplo, dicta que en el índice 2 se guarda la parte del cuerpo.
    # Por ejemplo, shoulder, elbow, wrist.
    body_part = jnt.split("_")[2]
    print("Creating constraints for " + body_part)
    # Se declaran los nombres de los joints IK, FK y bind.
    ik_jnt = jnt + "_ik"
    fk_jnt = jnt + "_fk"
    bind_jnt = jnt + "_bind"
    # Se crea el parent constraint entre IK y bind.
    cmds.parentConstraint(ik_jnt, bind_jnt)
    # Se crea el parent constraint entre FK y bind.
    cmds.parentConstraint(fk_jnt, bind_jnt)
print("Done")
