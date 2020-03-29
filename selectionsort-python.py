arr=[]
for i in range(int(input("enter the size of the arr:"))):
    x=int(input("enter the ele"))
    arr.append(x)
for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if(arr[min_index]>arr[j]):
            min_index=j
    arr[min_index],arr[i]=arr[i],arr[min_index]
print(arr)