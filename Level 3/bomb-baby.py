def solution(m,f):
    sol=(int(m),int(f))
    
    cgen={(1,1)}
    cgenbutbetter=set()
    ngen=set()
    gens=0

    while (len(cgen)):
        #print(cgen)
        #remove cases which are already larger than what we want
        for i in cgen:
            if i[0] <= sol[0] and i[1] <= sol[1]:
                cgenbutbetter.add(i)
        cgen=cgenbutbetter
        cgenbutbetter=set()        
        #check if solved
        if sol in cgen:
            return str(gens)

        #recreation or something
        for i in cgen:
            ngen.add((i[0],i[1]+i[0]))
            ngen.add((i[0]+i[1],i[1]))

        #prepare for next cycle
        cgen=ngen
        ngen=set()
        gens+=1
    
    return "impossible"

print(solution(4,7))
