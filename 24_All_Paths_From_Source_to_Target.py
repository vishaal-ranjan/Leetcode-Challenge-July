class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        tmp = [0]
        self.backtrack(graph, res, 0, tmp)
        return res
    
    def backtrack(self, graph, res, idx, tmp):
        if idx == len(graph) - 1:
            res.append(list(tmp))
            return
        
        for node in graph[idx]:
            tmp.append(node)
            self.backtrack(graph, res, node, tmp)
            tmp.pop()