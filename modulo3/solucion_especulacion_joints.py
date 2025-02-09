import maya.cmds as cmds

number_of_joints = 3
right_suffix = "_r_"
left_suffix = "_l_"
jnt_prefix = "jnt"

print("Creating left joint chain")
for i in range(number_of_joints):
    jnt_pos = (i + 1) * -1
    jnt_name = jnt_prefix + left_suffix + str(i)
    cmds.joint(n=jnt_name, p=(jnt_pos,0,0))
print("Done")

cmds.select(d=True) # Deselect the joints to start a new joint chain.

print("Creating right joint chain")
for i in range(number_of_joints):
    jnt_pos = i + 1
    jnt_name = jnt_prefix + right_suffix + str(i)
    cmds.joint(n=jnt_name, p=(jnt_pos,0,0))
print("Done")
