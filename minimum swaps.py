def minSwaps(arr): 
    n = len(arr) 
    arrpos = [*enumerate(arr)] 
    print(arrpos)
    arrpos.sort(key = lambda it:it[1]) 
    print(arrpos)
    vis = {k:False for k in range(n)} 
    ans = 0
    for i in range(n): 
        if vis[i] or arrpos[i][0] == i: 
            continue
        cycle_size = 0
        j = i 
        while not vis[j]: 
            vis[j] = True
            j = arrpos[j][0] 
            cycle_size += 1
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    return ans 
	 
arr = [3,4,2,5,1] 
print(minSwaps(arr)) 

# This code is contributed 
# by Dharan Aditya 
