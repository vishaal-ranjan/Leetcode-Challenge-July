class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        sol = []
        
        for k,v in d.items():
            if v == 1:
                sol.append(k)
                
        return sol