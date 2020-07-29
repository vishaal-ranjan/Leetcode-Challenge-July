class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_map = [0]*26
        for task in tasks:
            char_map[ord(task)-ord('A')] += 1
        
        char_map.sort()
        maxval = char_map[-1] - 1
        
        idle_slots = maxval*n
        
        for i in range(24, -1, -1):
            idle_slots -= min(char_map[i], maxval)
            
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)