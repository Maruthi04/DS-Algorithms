class Solution:
    def singleNumber(self, nums):
        x=0
        arr=[]
        dic=dict()
        for i in nums:
            if i in dic:
                dic[i]=-99999
            else:
                dic[i]=i
        
        for i in dic.values():
            if i!=-99999:
                arr.append(i)
        return arr
        
obj=Solution()
print(obj.singleNumber([1,2,1,3,2,5]))