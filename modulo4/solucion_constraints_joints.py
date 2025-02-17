import maya.cmds as cmds

joints = ["jnt_r_shoulder", "jnt_r_elbow", "jnt_r_wrist"]

print("Creating parent constraints")
for jnt in joints:
    print("Creating constraints for " + jnt.split("_")[2])
    cmds.parentConstraint(jnt + "_ik", jnt + "_bind")
    cmds.parentConstraint(jnt + "_fk", jnt + "_bind")
print("Done")
