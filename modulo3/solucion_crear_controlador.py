import maya.cmds as cmds

targetJoint = cmds.ls(sl=True)[0]

print("================ Create controller for joint " + targetJoint)
newControllerName = targetJoint + "_ctrl"
groupName = newControllerName + "_grp"

print("Positioning controller")
newController = cmds.circle(c=(0,0,0), nr=(0,1,0), r=1, d=3, ut=0, tol=0.1, s=8, ch=1)[0]
pointConst = cmds.pointConstraint(targetJoint, newController, offset=(0,0,0), weight=1)[0]
cmds.delete(pointConst)

print("Setting up controller")
cmds.rename(newController, newControllerName)
cmds.makeIdentity(newControllerName, apply=True, t=1, r=1, s=1, n=0, pn=1) # FREEZE TRANSFORM
cmds.delete(newControllerName, constructionHistory=True) # CLEAR HISTORY

print("Grouping up controller")
cmds.group(em=True, n=groupName)
cmds.parent(newControllerName, groupName)
cmds.xform(groupName, cp=1) # CENTER PIVOT

print("Orienting group with joint")
parentConst = cmds.parentConstraint(targetJoint, groupName)[0]
cmds.delete(parentConst)

print("Parenting joint to controller")
cmds.orientConstraint(newControllerName, targetJoint)
