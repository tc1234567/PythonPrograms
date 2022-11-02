class Solution:
    def guessNumber(self, n: int) -> int:
        
        first, last = 1, n
        while first <= last:
            pick = (first + last)//2
            t = guess(pick)
            if t == 0: return pick
            if t == -1: last = pick - 1
            if t == 1:  first = pick + 1
