class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming = 0
        
        for _ in range(32):
            
            if (x^y)%2 == 1:
                hamming += 1
            x = x>>1
            y = y>>1
        
        return hamming