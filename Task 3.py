#starting position is (0,0)
#keep track of coordinates in dictionary with key x coordinate and list of y coordinates
file = open("input3.txt")
directions = file.read()

x_coordinate = 0
y_coordinate = 0

coordinateDict = {0:{0}}

for direction in directions:
    if(direction == ">"):
        x_coordinate += 1
    elif(direction == "<"):
        x_coordinate -= 1
    elif(direction == "^"):
        y_coordinate += 1
    elif(direction == "v"):
        y_coordinate -= 1
    
    if(x_coordinate in coordinateDict):
        coordinateDict[x_coordinate].add(y_coordinate)
    else:
        coordinateDict[x_coordinate] = {y_coordinate}

keys = coordinateDict.keys()

totalHouses = 0
for x in keys:
    totalHouses += len(coordinateDict[x])

#print(totalHouses)
coordinateDict = {0 : {0}}
x_coordinate = 0
y_coordinate = 0
rx_coordinate = 0
ry_coordinate = 0
for x in range(0, len(directions)):
    direction = directions[x]
    if ( x % 2 == 0):   #santa indices
        if(direction == ">"):
            x_coordinate += 1
        elif(direction == "<"):
            x_coordinate -= 1
        elif(direction == "^"):
            y_coordinate += 1
        elif(direction == "v"):
            y_coordinate -= 1
        if(x_coordinate in coordinateDict):
            coordinateDict[x_coordinate].add(y_coordinate)
        else:
            coordinateDict[x_coordinate] = {y_coordinate}
    else:
        if(direction == ">"):
            rx_coordinate += 1
        elif(direction == "<"):
            rx_coordinate -= 1
        elif(direction == "^"):
            ry_coordinate += 1
        elif(direction == "v"):
            ry_coordinate -= 1
        if(rx_coordinate in coordinateDict):
            coordinateDict[rx_coordinate].add(ry_coordinate)
        else:
            coordinateDict[rx_coordinate] = {ry_coordinate}

k1 = coordinateDict.keys()

totalHouses = 0
for k in k1:
    totalHouses += len(coordinateDict[k])


print(totalHouses)
