class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i, j, k = 0, 0, 0
        final = [1]
        
        while len(final) < n:
            temp1, temp2, temp3 = final[i]*2, final[j]*3, final[k]*5
            nextval = min(temp1, temp2, temp3)
            final.append(nextval)
            if nextval == temp1:
                i += 1
            if nextval == temp2:
                j += 1
            if nextval == temp3:
                k += 1
        
        return final[n-1]