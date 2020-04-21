class Solution:
    def myfunc(self,n):
        if n==1:
            return 0
        else:
            if n%2==0:
                return self.myfunc(n/2)+1
            else:
                return min(self.myfunc(n-1)+1,self.myfunc(n+1)+1)
            
    def integerReplacement(self, n):
        return self.myfunc(n)
obj=Solution()
print(obj.integerReplacement(8))