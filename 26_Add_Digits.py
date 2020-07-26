class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        num = str(num)
        if len(num) == 1:
            return int(num)
        
        while len(num) != 1:
            total = 0
            for i in str(num):
                total += int(i)
            num = str(total)
            
        return total