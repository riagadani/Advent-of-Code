def stringValues(s):
    stringcode = 0
    memorycharacters = 0
    orig = len(s)
    stringcode = len(s) + 4
    memorycharacters = len(s)-2
    mem = s[1:len(s)-1]
    for i in range(0, mem.count("\\")):
        stringcode += 2
        if(i == len(mem)-1 or len(mem) == 0 or mem.count("\\") == 0):
            break
        if (mem[mem.index("\\")+1] == "\""):
            memorycharacters -= 1
            mem = mem[mem.index("\\\"")+2 :]
        elif (mem[mem.index("\\")+1] == "\\"):
            memorycharacters -= 1
            mem = mem[mem.index("\\\\")+2 :]
        elif (mem[mem.index("\\")+1] == "x"):
            memorycharacters -= 3
            stringcode -= 1
            mem = mem[mem.index("\\x")+4 : ]


    # if ("\"" in mem):
    #     for i in range(0, mem.count("\"")):
    #         memorycharacters -= 1
    # if ("\\\\" in mem and mem[mem.index("\\") + 1] != "\\" and mem[mem.index("\\") + 1] != "\""):
    #     for i in range(0, mem.count("\\\\")):
    #         memorycharacters -= 1

    # if ("\\x" in mem):
    #     print(mem.count("\\x"))
    #     for i in range(0, mem.count("\\x")):
    #         memorycharacters -= 3
    print(stringcode)
    return stringcode - orig

file = open("test.txt")

strings = file.read().split("\n")

total = 0
for s in strings:
    total += stringValues(s)

print(total)