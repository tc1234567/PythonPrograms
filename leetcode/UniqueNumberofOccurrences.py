class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
    
        counter = {}

        for item in arr:
            if item not in counter:
                counter[item] = 0
            counter[item] += 1

        temp_list = []

        for k in counter:
            temp_list.append(counter[k])

        temp_list.sort()

        temp_list2 = []

        for i in range(0, len(temp_list)-1):

            if temp_list[i]==temp_list[i+1]:
                temp_list2.append(False)

            temp_list2.append(True)

        return all(temp_list2)
