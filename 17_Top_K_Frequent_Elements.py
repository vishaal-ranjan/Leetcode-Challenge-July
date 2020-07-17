from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        
        return heapq.nlargest(k, d.keys(), key = d.get)