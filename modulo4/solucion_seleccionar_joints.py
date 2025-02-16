import maya.cmds as cmds

joints = []
all_objs = cmds.ls(sl=True)

for obj in all_objs:
    if(cmds.nodeType(obj) == "joint"):
        joints.append(obj)

cmds.select(cl=True) # Clear the original selection.

if(len(joints) > 0):
    cmds.select(joints)
else:
    print("Whoops! There are no joints in the selection.")
