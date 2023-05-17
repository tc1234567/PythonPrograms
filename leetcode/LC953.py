class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        list1 = []
        list1[:0] = order

        alphabets = 'abcdefghijklmnopqrstuvwxyz'

        list2 = []
        list2[:0] = alphabets

        d = dict(zip(list1, list2))

        lst=[]
        sorted_i=''

        for i in words:
            for j in i:
                j=d[j]
                sorted_i+=j
            lst.append(sorted_i)
            sorted_i=''
            
        if lst == sorted(lst):
            return True
        else:
            return False
