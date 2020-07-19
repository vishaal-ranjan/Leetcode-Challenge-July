class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum1 = 0
        sum2 = 0
        cnt = 0
        
        for i in reversed(a):
            sum1 += (2**cnt)*int(i)
            cnt += 1
        
        cnt = 0
        for i in reversed(b):
            sum2 += (2**cnt)*int(i)
            cnt += 1
            
        total = sum1 + sum2
        
        return str(bin(total))[2:]