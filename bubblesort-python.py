arr=[]
for i in range(int(input("enter the size of the arr"))):
    x=int(input("enter the element"))
    arr.append(x)
n=len(arr)
for i in range(n):
    for j in range(n-i-1):
        
        if(arr[j]>arr[j+1]):
            print(i,j)
            arr[j],arr[j+1]=arr[j+1],arr[j]
        else:
            print("else:",i,j)
print(arr)
        
    
