u=20231

prime=[None,None]+[True]*(u-1)

for i in range(2,len(prime)):
    if prime[i]:
        for j in range(i,u//i+1):
            prime[i*j]=False

phrase="".join([str(i) for i in range(u+1) if prime[i]])

def solution(n):
    return phrase[n:n+5]

#print(solution(0))
