class Solution:
    def hammingWeight(self, n):
        s=""
        while(n):
            s=s+str(n%2)
            n=n//2
        s=s[::-1]
        return s.count('1')
            
obj=Solution()
print(obj.hammingWeight(00000000000000000000000000001011))