def solution(a,b):
    a,b,c=int(a),int(b),-1
    if a<b:a,b=b,a
    while(b):
        c+=a//b
        a,b=b,a%b
    return c if a==1 else "impossible"

#print(solution(4,7))
