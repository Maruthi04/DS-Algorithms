def mergesort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        mergesort(l)
        mergesort(r)
        i=0
        j=0
        k=0
        while(i<len(l) and j <len(r)):
            if(l[i]<r[j]):
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while(i<len(l)):
            arr[k]=l[i]
            i+=1
            k+=1
        while(j<len(r)):
            arr[k]=r[j]
            j+=1
            k+=1
n=int(input("enter the size"))
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
mergesort(arr)
print(arr)