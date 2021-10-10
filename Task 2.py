def surfacearea(a, b, c):
    area = 2*(a*b + a*c + b*c)
    x = min(a, b)
    y = min(b, c)
    
    if x==y:
        y = min(a,c)

    area += x*y
    return area
def ribbon(a,b,c):
    len = a*b*c
    x = min(a, b)
    y = min(b, c)
    
    if x==y:
        y = min(a,c)
    len += 2*x + 2*y
    return len

file = open("input2.txt")
dim = file.read().split()

totalarea = 0
totallength = 0
for d in dim:
    dimensions = d.split("x")
    a = int(dimensions[0])
    b = int(dimensions[1])
    c = int(dimensions[2])
    totalarea += surfacearea(a,b,c)
    totallength += ribbon(a,b,c)

print(totalarea)

print(totallength)

