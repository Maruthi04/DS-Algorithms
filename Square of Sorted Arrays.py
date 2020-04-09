class Solution:
    def sortedSquares(self, A):
        arr=[]
        for i in A:
            arr.append(i**2)
        print(arr)
        arr.sort()
        return arr
obj=Solution()
arr=[1,2,3,4,5]
obj.sortedSquares(arr)
