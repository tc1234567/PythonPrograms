class Solution:
    def lengthOfLongestSubstring(self, word: str) -> int:

        temp_set = set()
        x = 0
        result = 0

        for i in range(len(word)):
            
            while word[i] in temp_set:
                temp_set.remove(word[x])
                x += 1
                
            temp_set.add(word[i])
            result = max(result, i-x+1)
            
        return result