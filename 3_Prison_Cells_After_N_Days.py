class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N == 0:
            return cells
        
        N = N%14 if N%14 != 0 else 14
        
        final = [[0 for _ in range(8)] for _ in range(N+1)]
        final[0] = cells
        
        for i in range(1, N+1):
            for j in range(1, 7):
                if (final[i-1][j-1] == final[i-1][j+1]):
                    final[i][j] = 1
                else:
                    final[i][j] = 0
            final[i][0], final[i][7] = 0, 0

        return final[N]