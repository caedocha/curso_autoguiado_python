import maya.cmds as cmds

def resetController(ctrl):
    attrs = cmds.listAttr(ctrl, k=True)
    for attr in attrs:
        default_value = cmds.attributeQuery(attr, node=ctrl, listDefault=True)[0]
        cmds.setAttr(ctrl + "." + attr, default_value)

def main():
    controllers = cmds.ls(sl=True)
    for ctrl in controllers:
        resetController(ctrl)

main()
