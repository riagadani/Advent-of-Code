input = open("input1.txt","r")
apt = input.read()

floor = 0
ct = 0
for x in apt:
    if x == '(':
        floor += 1
    else:
        floor -= 1
    ct += 1
    if(floor == -1):
        break
    
print(ct)