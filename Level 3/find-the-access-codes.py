def solution(l):
    triplets=0
    n=len(l)
    faxx=[0]*n
    for j in range(n):
        for i in range (j):
            if l[j]%l[i]==0:
                faxx[j]+=1
                triplets+=faxx[i]
    return triplets

print(solution([1,1,1]))
