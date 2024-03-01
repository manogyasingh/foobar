from math import atan2

# Reflect the given value 'v' taking 'l' and 'r' as left and right mirrors respectively
# only till a maximum distance 'm'
# only reflevts in 1D. for 2D, since the room is rectangular, reflect if in both axes
# and then take the product

def reflect(v,l,r,m):
    g,r2=2*(r-l),r*2
    return set([(r2-v+i*g) for i in range(-((r2+m-v)//g),(m-r2+v)//g+1)]+[v+i*g for i in range(-((m+v)//g),(m-v)//g+1)])

# Approach
# Basic strategy is to assume the bullet as a light ray travelling in infinite space
# "You" is the origin, obviously will lie in all its rays
# enemy is the target we want to hit, this can be understood as the light ray moving
# in a straight line and passing through their reflected image (or their real self)
# 
# Obviously, the game ends when the bullet touches the first object, regardless of the direction it has been thrown in
# so we only consider the first image in every direction
# 

def solution(room, you, opp, dist): 
    #It's easier if you make yourself the origin since all distances and directions
    #will have to be measured relative to you
    opp=(opp[0]-you[0],opp[1]-you[1])
    walls={
        "u":room[1]-you[1],
        "d":-you[1],
        "r":room[0]-you[0],
        "l":-you[0]
    }
    you_all_x=reflect(0,walls["l"],walls["r"],dist)
    you_all_y=reflect(0,walls["d"],walls["u"],dist)
    opp_all_x=reflect(opp[0],walls["l"],walls["r"],dist)
    opp_all_y=reflect(opp[1],walls["d"],walls["u"],dist)

    you_all_polar={}
    done_angles=set()
    
    #since we only use dist to compare to other distances, we'll save some effort by
    #not calculating distance and instead leaving it on square of the distance
    d2=dist*dist

    #make a dict of distances of your closest image in every direction it exists in
    for x in you_all_x:
        for y in  you_all_y:
            rad2=x*x+y*y
            if rad2 and rad2<d2:
                ang=atan2(y,x)
                if (ang not in you_all_polar or you_all_polar[ang]>rad2):
                    you_all_polar[ang]=rad2
    
    for x in opp_all_x:
        for y in opp_all_y:
            rad2=x*x+y*y
            if rad2<=d2:
                ang=atan2(y,x)
                if ang not in done_angles:
                    if ang not in you_all_polar or you_all_polar[ang]>rad2:
                        done_angles.add(ang)
                        
    return len(done_angles)
