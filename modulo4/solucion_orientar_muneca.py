import maya.cmds as cmds

side = "r"
orientation = "xyz"
secondaryAxisOrient = "zdown"
chain_types = ["ik", "fk", "bind"]
locators = cmds.ls(sl=True)

cmds.select(cl=True)
for type in chain_types: 
    jnts = []
    wrist_jnt = ""
    for loc in locators:
        tx = cmds.getAttr(loc+".tx")
        ty = cmds.getAttr(loc+".ty")
        tz = cmds.getAttr(loc+".tz")
        jnt_pos = (tx, ty, tz)
        jnt_name = "jnt_" + side + "_" + loc + "_" + type
        cmds.joint(n=jnt_name, p=jnt_pos)
        if(not loc == "wrist"):
            jnts.append(jnt_name)
        else:
            wrist_jnt = jnt_name
    # The joint chain has to be fully created in order to orient its joints correctly
    cmds.select(jnts) 
    cmds.joint(edit=True, oj=orientation, secondaryAxisOrient=secondaryAxisOrient, ch=True, zso=True)
    cmds.select(cl=True) # Deselect everything
    cmds.select(wrist_jnt) # Select wrist joint to orient it with "Orient joint to world" option
    cmds.joint(edit=True, oj="none", ch=True, zso=True)
    cmds.select(cl=True) # Deselect everything
