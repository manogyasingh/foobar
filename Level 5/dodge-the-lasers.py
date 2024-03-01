############################################################################################################################
##  Strategy:                                                                                                             ##
##                                                                                                                        ##
##  We have:                                                                                                              ##
##  func(n)                                                                                                               ##
##  =sum([floor(sqrt(2)*i) for i in range (n)])                                                                           ##
##  =sum([i for i in range(max num in above sequence)])-sum([natural numbers in this range not in above sequence])        ##
##  =nsum(n'th number in sequence)-sum(floor((2+sqrt(2))*i) for in range(greatest natural lower bound of above sequence)) ##
##  {here, nsum is sum of all natural numbers <=n}{2+sqrt(2) is the rayleigh's complement of sqrt(2)}                     ##
##  =nsum(floor(sqrt(2)*n))-sum(2*i for i in range (sqrt(2)*n/(2+sqrt(2))))-func(sqrt(2)*n/(2+sqrt(2)))                   ##
##                                                                                                                        ##
##  this exponentially decreases the length of the loop woth each operation, yeilding a time complexity of O(log(n))      ##
############################################################################################################################

r=4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
r2=14142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

nsum=lambda a: a*(a+1)/2
newlim=lambda t: (t*r)//10**100
ibt=lambda m: (r2*m)//10**100
bt= lambda n: n if n < 2 else nsum(ibt(n))-2*nsum(newlim(n))-bt(newlim(n))

def solution(n):
    return str(int(bt(int(n))))

###################################################     DRIVER CODE     ####################################################
if __name__=="__main__":
    print(solution(10**100))
    
    
    
