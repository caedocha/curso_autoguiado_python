import maya.cmds as cmds
  
targetJoint = cmds.ls(sl=True)[0]
newControllerName = targetJoint + "_ctrl"
groupName = newControllerName + "_grp"

print("================ Create controller for joint " + targetJoint)
cmds.circle(c=(0,0,0), nr=(0,0,1), r=1, d=3, ut=0, tol=0.1, s=8, ch=1, name=newControllerName)

print("Grouping up controller")
cmds.group(em=True, n=groupName)
cmds.parent(newControllerName, groupName)

print("Positioning controller")
pointConst = cmds.parentConstraint(targetJoint, groupName, weight=1)[0]
cmds.delete(pointConst)

print("Rotate controller's vertices")
cmds.select(cl=True)
cmds.select(newControllerName + ".cv[0:7]")
cmds.rotate(0,0,90,r=True, eu=True, fo=True)
cmds.select(cl=True)

print("Parenting joint to controller")
cmds.orientConstraint(newControllerName, targetJoint)
