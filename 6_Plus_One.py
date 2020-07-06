class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numstr = ''
        for i in digits:
            numstr += str(i)
        
        actual = int(numstr) + 1
        numstr = str(actual)
        out = []
        
        for i in numstr:
            out.append(int(i))
        return out