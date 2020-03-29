def binarysearch(arr,k,l,r):
    if(l<r):
        mid=(l+r)//2
        #print("mid",mid)
        if(k<arr[mid]):
            #print("less",k,l,mid)
            return binarysearch(arr,k,l,mid)
        elif(k>arr[mid]):
            #print("more",arr[mid],k,mid,r)
            return binarysearch(arr,k,mid,r)
        elif(arr[mid]==k):
            #print("mid",arr[mid],mid)
            return "the element is found in ",mid
    
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
k=int(input("enter hte element to be searche dfor"))
print(binarysearch(arr,k,0,len(arr)-1))