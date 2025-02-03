right_suffix = "_r_"
left_suffix = "_l_"
jnt_name = "jnt"
jnt_number = 0

jnt = jnt_name + left_suffix + str(jnt_number)
cmds.joint(n=jnt, p=(-1,0,0))

jnt_number = jnt_number + 1
jnt = jnt_name + left_suffix + str(jnt_number)
cmds.joint(n=jnt, p=(-2,0,0))

jnt_number = jnt_number + 1
jnt = jnt_name + left_suffix + str(jnt_number)
cmds.joint(n=jnt, p=(-3,0,0))

cmds.select(d=True)

jnt = jnt_name + right_suffix + str(jnt_number)
cmds.joint(n=jnt, p=(1,0,0))

jnt_number = jnt_number + 1
jnt = jnt_name + right_suffix + str(jnt_number)
cmds.joint(n=jnt, p=(2,0,0))

jnt_number = jnt_number + 1
jnt = jnt_name + right_suffix + str(jnt_number)
cmds.joint(n=jnt, p=(3,0,0))
