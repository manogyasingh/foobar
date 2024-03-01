def solution(pegs):
    #basically all a[i]-a[i-1] are pairwise sums of radii
    #we try to cancel out and leave just two vars
    #by alternatively adding and subtracting these pairwise sums
    n=len(pegs)
    alt_sum=0
    for i in range(1,n):
        diff=pegs[i]-pegs[i-1]
        if i%2:
            alt_sum+=diff
        else:
            alt_sum-=diff
    #now if n was odd, we have a+e
    #if n was even, we have a-e
    #we can solve these along with the condition that a=2e
    #here a is first radius and e is the last
    if n%2:
        sol=[2*alt_sum,1]
    else:
        if alt_sum%3==0:
            sol=[2*alt_sum/3,1]
        else:
            sol=[2*alt_sum,3]

    #check if any radius is forced to be less than 1
    radius=sol[0]/sol[1]
    for i in range(1,n):
        radius=pegs[i]-pegs[i-1]-radius
        if radius<1:
            return [-1,-1]

    #if all is well, return sol
    return sol

#print(solution([4,17,50]))
