class Solution:
    def merge(self, intervals):
        fin=[]
        arr=intervals
        if(len(arr)==1):
            return intervals
        c=0
        c1=[]
        arr=sorted(arr,key=lambda x: x[0])
        for i in range(len(arr)-1):
            if(arr[i+1][0]>=arr[i][0] and arr[i+1][0]<=arr[i][1]):
                c1.append(i)
                c1.append(i+1)
                if(arr[i+1][1]<=arr[i][1]):
                    fin.append([arr[i][0],arr[i][1]])
                    arr[i+1]=[arr[i][0],arr[i][1]]
                    arr[i]=None
                elif(arr[i+1][1]>=arr[i][1]):
                    c=1
                    fin.append([arr[i][0],arr[i+1][1]])
                    arr[i+1]=[arr[i][0],arr[i+1][1]]
                    arr[i]=None
        arr1=[]
        for i in arr:
            if(i is not None):
                arr1.append(i)
                
        return arr1
obj=Solution()
arr=[[1,3],[2,6],[8,10],[15,18]]
print(obj.merge(arr))