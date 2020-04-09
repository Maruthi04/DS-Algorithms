class Solution:
    def longestCommonPrefix(self, strs):
        arr=strs
        if(len(arr)==0):
            return ""
        if(len(arr)==1):
            return arr[0]
        arr.sort()
        i=0
        mini=min(len(arr[0]),len(arr[len(arr)-1]))
        while(i<mini and arr[0][i]==arr[len(arr)-1][i]):
                 i+=1
        if(i>0):
                 return arr[0][:i]
        else:
            return ""
obj=Solution()
arr=["flower","flow","flight"]
print(obj.longestCommonPrefix(arr))
