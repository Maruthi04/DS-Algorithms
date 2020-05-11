def kthsmallest(arr,l,r,k):
    if k>0 and k<=r-l+1:
        n=r-l+1
        median=[]
        i=0
        while i<n//5:
            median.append(findmedian(arr,l+i*5,5))
            i+=1
        if i*5<n:
            median.append(findmedian(arr,l+i*5,n%5))
            i+=1
        if i==1:
            medofmed=median[i-1]
        else:
            medofmed=kthsmallest(median,0,i-1,i//2)
        pos=partition(arr,l,r,medofmed)
        if pos-l==k-1:
            return arr[pos]
        if pos-l>k-1:
            return kthsmallest(arr,l,pos-1,k)
        return kthsmallest(arr,pos+1,r,k-pos+l-1)
    return 99999
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
def findmedian(arr,l,r):
    lis=[]
    for i in range(l+r):
        lis.append(arr[i])
    lis.sort()
    return lis[r//2]
def partition(arr,l,r,k):
    for i in range(l,r):
        if arr[i]==k:
            swap(arr,i,r)
            break
    k=arr[r]
    i=l
    for j in range(l,r):
        if arr[i]<=k:
            swap(arr,i,j)
            i+=1
    swap(arr,i,r)
    return i
arr=[7,6,5,8,9,2,1]
print(kthsmallest(arr,0,len(arr)-1,3))

    
            