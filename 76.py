# 76.Minimum Window Subbstring
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = Counter(t)
        t_len = len(t)

        minL, minR = 0, float('inf')

        l = 0
        for r,c in enumerate(s):
            if mem[c] > 0:
                t_len -= 1
            mem[c] -= 1

            if t_len == 0:
                while mem[s[l]] < 0:
                    mem[s[l]] += 1
                    l += 1

                if r - l < minR -minL:
                    minL, minR = 1,r

                mem[s[l]] += 1
                t_len += 1
                l += 1
        return ''if minR == float('inf') else s[minL:minR+1]

# solution 2
    def minWindow2(self,s,t):
        
        count = Counter(t)
        miss = len(t) # recording, the recent window 
        i = m = n = 0
        for j,v in enumerate(s,1): #slide to right
            miss -= (count[v] > 0)
            count[v] -= 1
            if not miss: # recent window meets requirment
                while i < j and count[s[i]] < 0: #left side pull back
                    count[s[i]] += 1 
                    i += 1
                if not n or j-i <= n - m: # renew recent window
                    n,m = j,i
        return s[m:n]


if __name__ == "__main__":
    solu = Solution()
    s, t = 'ADOBECODEBANC', 'ABC'
    print(solu.minWindow(s,t))

