from math import ceil, sqrt

dic, ways = {}, 0

def gcd(a,b): # a, b positive integer
    while b!=0:
        a, b = b, a%b
    return a

def dist(x,y):
    return sqrt(x**2 + y**2)

def store(x,y,dist,isMe):
    global dic, ways

    if x==0 and y==0:
        return
    if x==0:
        y = int(y > 0)
    elif y == 0:
        x = int(x > 0)
    else:
        g = gcd(abs(x),abs(y))
        x, y = int(x//g), int(y//g)

    if x not in dic.keys():
        dic[x] = {}
    if y not in dic[x].keys():
        dic[x][y] = [dist,isMe]
        if not isMe:
            ways += 1
    else:
        if dic[x][y][0] > dist:
            if dic[x][y][1] and not isMe:
                ways += 1
            if isMe and not dic[x][y][1]:
                ways -= 1
            dic[x][y] = [dist,isMe]
            
def solution(dimensions, your_position, trainer_position, distance):
    global dic, ways
    dic, ways = {}, 0

    diag = dist(dimensions[0], dimensions[1])
    nGrid = [int(ceil(float(distance)/dimensions[0])), int(ceil(float(distance)/dimensions[1]))]

    for i in range(-nGrid[0],nGrid[0]+1):
        for j in range(-nGrid[1],nGrid[1]+1):
            x_grid, y_grid = i*dimensions[0], j*dimensions[1]
            d_grid = dist(x_grid, y_grid)

            if d_grid > distance + 2*diag:
                continue

            x_me = x_grid + (your_position[0] if i%2==0 else dimensions[0]-your_position[0])
            x_trainer = x_grid + (trainer_position[0] if i%2==0 else dimensions[0]-trainer_position[0])
            y_me = y_grid + (your_position[1] if j%2==0 else dimensions[1]-your_position[1])
            y_trainer = y_grid + (trainer_position[1] if j%2==0 else dimensions[1]-trainer_position[1])

            x_me = x_me - your_position[0]
            x_trainer = x_trainer - your_position[0]
            y_me = y_me - your_position[1]
            y_trainer = y_trainer - your_position[1]

            disMe = dist(x_me, y_me)
            disTrainer = dist(x_trainer, y_trainer)

            if disMe <= distance:
                store(x_me,y_me,disMe,True)
            if disTrainer <= distance:
                store(x_trainer, y_trainer,disTrainer,False)
    return ways