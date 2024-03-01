xtill=lambda x: [x,1,x+1,0][x%4] 

def solution(start, length):
    coolcode=0
    for i in range(0,length):
        coolcode^=xtill(start+i*length-1)
        coolcode^=xtill(start+i*length+length-i-1)
    return coolcode
