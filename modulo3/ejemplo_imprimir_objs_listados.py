"""
****************************************************************************************************
     TODOS LOS EJEMPLOS Y SOLUCIONES ESTÁN LISTOS PARA COPIAR Y PEGARSE EN EL SCRIPT EDITOR
****************************************************************************************************
"""
import maya.cmds as cmds

print("------- Selecting all of the scene's objects --------")
# Selecciona todos los objetos de la escena.
cmds.select(all=True)

# Lista los objetos seleccionados y los guarda en la variable `objs`.
objs = cmds.ls(sl=True)

# Usando el ciclo, se va imprimiendo uno a uno los objetos seleccionados.
for obj in objs:
    print(obj)
print("---------------------- Done -------------------------")
