def cross(arr,l,m,h):
    left=-1000
    sum1=0
    for i in range(m,l-1,-1):
        sum1=sum1+arr[i]
        if(sum1>left):
            left=sum1
    right=-1000
    sum2=0
    for i in range(m+1,h+1,1):
        sum2=sum2+arr[i]
        if(right<sum2):
            right=sum2
    return left+right
def maxsubarray(arr,l,h):
    if(l==h):
        return arr[l]
    m=(l+h)//2
    return max(maxsubarray(arr,l,m),maxsubarray(arr,m+1,h),cross(arr,l,m,h))
    

arr=[-2,1,-3,4,-1,2,1,-5,4]

print(maxsubarray(arr,0,len(arr)-1))