class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        arr.sort()
        if 0 in arr:
            arr.remove(0)
        flag = ''
        for i in range(len(arr)):
            if 2*arr[i] in arr:
                flag=True
                break
            else:
                flag=False

        return flag
