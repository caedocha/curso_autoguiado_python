import maya.cmds as cmds

# Initial 3 joints
shoulder_joint = "jnt_r_shoulder_ik"
elbow_joint = "jnt_r_elbow_ik"
wrist_joint = "jnt_r_wrist_ik"

# Name of the controllers and the controllers' groups
pole_vector_controller = "poleVector_r_ctrl"
pole_vector_controller_group = pole_vector_controller + "_grp"
ik_controller = "ik_r_ctrl"
ik_controller_group = ik_controller + "_grp"

print("Creating IK handle")
ik_handle = cmds.ikHandle( sj=shoulder_joint, ee=wrist_joint)[0]
print(ik_handle)

print("Creating pole vector controller")
cmds.spaceLocator(n=pole_vector_controller)

print("Grouping pole vector controller")
cmds.group(em=True, n=pole_vector_controller_group)
cmds.parent(pole_vector_controller, pole_vector_controller_group)

print("Positioning pole vector controller")
pointConst = cmds.pointConstraint(elbow_joint, pole_vector_controller_group, weight=1)[0]
cmds.delete(pointConst)
cmds.move(0,0,-2, pole_vector_controller_group, relative=True)

print("Creating pole vector constraint")
cmds.poleVectorConstraint(pole_vector_controller, ik_handle)

print("Creating IK controller")
cmds.circle(c=(0,0,0), nr=(1,0,0), r=1, d=3, ut=0, tol=0.1, s=8, ch=1, name=ik_controller)

print("Grouping up IK controller")
cmds.group(em=True, n=ik_controller_group)
cmds.parent(ik_controller, ik_controller_group)

print("Positioning IK controller")
pointConst = cmds.parentConstraint(wrist_joint, ik_controller_group, weight=1)[0]
cmds.delete(pointConst)

print("Parenting IK handle to IK controller")
cmds.parent(ik_handle, ik_controller)

print("Done")
