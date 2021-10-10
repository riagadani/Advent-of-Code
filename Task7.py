file = open("input7.txt")
instructions = file.read(). split("\n")

data = {}
stored = {}
for inst in instructions:

    cmd, res = inst.split("->")
    data[res.strip()] = cmd

def getValue(res):
    try:
        stored[res] = int(res)
        return int(res)
    except ValueError:
            pass
    cmd = data[res].split(" ")
    if( "NOT" in cmd):
        if(cmd[1] in stored):
            stored[res] = ~stored[cmd[1]]
            return ~stored[cmd[1]]
        stored[res] = ~getValue(cmd[1])
        return  stored[res]
    elif ("OR" in cmd):
        if(cmd[0] in stored):
            if(not cmd[2] in stored):
                stored[cmd[2]] = getValue(cmd[2])
        else:
            stored[cmd[0]] = getValue(cmd[0])
            if(not cmd[2] in stored):
                stored[cmd[2]] = getValue(cmd[2])
        
        stored[res] = stored[cmd[2]] | stored[cmd[0]]
        return stored[res]
    elif ("AND" in cmd):
        if(cmd[0] in stored):
            if(not cmd[2] in stored):
                stored[cmd[2]] = getValue(cmd[2])
        else:
            stored[cmd[0]] = getValue(cmd[0])
            if(not cmd[2] in stored):
                stored[cmd[2]] = getValue(cmd[2])
        stored[res] = stored[cmd[2]] & stored[cmd[0]]
        return stored[res]
    elif ("LSHIFT" in cmd):
        if(not cmd[0] in stored):
            stored[cmd[0]] = getValue(cmd[0])
        return stored[cmd[0]] << int(cmd[2])
    elif ("RSHIFT" in cmd):
        if(not cmd[0] in stored):
            stored[cmd[0]] = getValue(cmd[0])
        return stored[cmd[0]] >> int(cmd[2])
    else:
        if(not cmd[0] in stored):
            stored[cmd[0]] = getValue(cmd[0])
        return stored[cmd[0]]

data["b"] = str(getValue("a"))
stored = {}
print(getValue("a"))
