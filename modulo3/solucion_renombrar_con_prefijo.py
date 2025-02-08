prefix = "jnt_"
print("Selecting parent joint")
joints = cmds.ls(sl=True)
cmds.select(joints[0], hi=True)
print("Now selecting the entire joint hierarchy")
joints = cmds.ls(sl=True)

for jnt in joints:
    print("Current joint name: " + jnt)
    new_name = prefix + jnt
    cmds.rename(jnt, new_name)
    print("New joint name: " + new_name)
print("Done renaming the joints")
