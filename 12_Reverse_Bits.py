class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for _ in range(32):
            tmp = (n&1)
            res = res|tmp
            n = n>>1
            res = res<<1
        res = res>>1
            
        return res