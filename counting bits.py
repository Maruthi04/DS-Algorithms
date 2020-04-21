class Solution:
    def countBits(self, num):
        arr=[]
        for i in range(0,num+1):
            arr.append(self.myfunc(i))
        return (arr)
    def myfunc(self,n):
        s=""
        while(n):
            s=s+str(n%2)
            n=n//2
        print(s)
        return s.count('1')
obj=Solution()
print(obj.countBits(5))