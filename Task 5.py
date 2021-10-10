def substring(l1, l2):
    if(l1 =="a" and l2 == "b"):
        return False
    elif (l1 == "c" and l2 == "d"):
        return False
    elif (l1 == "p" and l2 == "q"):
        return False
    elif(l1 == "x" and l2 == "y"):
        return False
    
    return True


file = open("input5.txt")

strings = file.read().split()

niceStrings = 0


for string in strings:
    prev = string[0]
    count = 0
    nice = False
    double = False
    for i in range(0, len(string)):
        if(string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u"):
            count += 1
        if(i > 0 and i < len(string)-1):
            if(prev == string[i+1]):
                double = True
            else:
                nice = substring(prev, string[i+1])
        
    if(count < 3):
        nice = False
    
    if(nice and double):
        niceStrings += 1

print(niceStrings)
