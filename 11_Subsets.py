class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        if not nums:
            return sol
        self.helper(0, nums, [], sol)
        
        return sol
    
    def helper(self, index, nums, current, sol):
        sol.append(list(current))
        for i in range(index, len(nums)):
            current.append(nums[i])
            self.helper(i+1, nums, current, sol)
            current.pop()