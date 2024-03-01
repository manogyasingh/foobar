def solution(inp,exits,cap):
    n,e,x=map(len,(cap,inp,exits))
    p=n-e-x
    #store direct inputs and outputs seperately. this helps avoid
    #confusions due to multiple input and exit rooms
    dirin=[sum([cap[j][i+e] for j in inp]) for i in range(p)]
    direx=[sum([cap[i+e][j] for j in exits]) for i in range(p)]
    #i don't expect this to be needed,
    #but since we're throwing away some parts of the map
    #we must make sure to account for all edge cases
    ans=0
    for i in inp:
        for j in exits:ans+=cap[i][j]
    #basically im trying to trim the data here
    #so that im only left with intermediate paths
    #and two seperate lists of total inout and output capacity
    #of each room
    cap=cap[e:-x]
    for i in range(p):
        cap[i]=cap[i][e:n-x]

    order,flow,seen=[],[],set()
    #what this alg does is:
    #0. keep a log of maximum num of bunnies which are still on the path
    #1. enter new room if possible
    #2. if can exit from this room, do so, and restart step 0 with a fresh batch of bunnies
    #3. if cannot, see if can go deeper and back to 2
    #4. if cannot, go up one step, go back to step 1
    #5. if 1 is not possible, ie, newroom foes not exist
    #which will happen when you've seen all enterable rooms
    #and cant exit from any in any path,
    #we just return the answer
    # Basically, this is a dfs greedy algorithm
    while True:
        if len(order):
            if direx[order[-1]]:
                flow.append(direx[i])
                minflow=min(flow)
                ans+=minflow
                for i in range(len(order)-1):
                    cap[order[i]][order[i+1]]-=minflow
                dirin[order[0]]-=minflow
                direx[order[-1]]-=minflow
                order,flow,seen=[],[],set()
                continue
            for i in range(p):
                if cap[order[-1]][i] and i not in seen:
                    flow.append(cap[order[-1]][i])
                    order.append(i)
                    seen.add(i)
                    break
            else:
                order.pop(-1)
                flow.pop(-1)
        else:
            for i in range(p):
                if dirin[i] and i not in seen:
                    order.append(i)
                    flow.append(dirin[i])
                    seen.add(i)
                    break
            else:
                  return ans     

if __name__ == "__main__":
    print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
