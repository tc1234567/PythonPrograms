class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        s = list(s)

        d = {}

        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1

        d_keys = []

        for i in d.keys():

            if d[i]==1:
                d_keys.append(i)

        if not d_keys:
            return -1

        return s.index(d_keys[0])
