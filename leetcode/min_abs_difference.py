class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()

        temp_list = []
        temp_list2 = []
        temp_list3 = []

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                
                diff = abs(arr[i] - arr[j])
                temp_list.append(diff)
                temp_list2.append([arr[i],arr[j]])

        for k in range(len(temp_list2)):
            if abs(temp_list2[k][0] - temp_list2[k][1]) == min(temp_list):
                temp_list3.append(temp_list2[k])

        return temp_list3
    
