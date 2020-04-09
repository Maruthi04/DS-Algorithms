class Solution:
    def twoSum(self, nums,target):
        arr=[]
        s=set()
        for i in range(len(nums)):
            temp=target-nums[i]
            if(temp in s):
                arr.append(nums.index(temp))
                arr.append(i)
            s.add(nums[i])
        return arr
arr=[2,7,11,15]
obj=Solution()
print(obj.twoSum(arr,int(input("Enter the Target"))))
