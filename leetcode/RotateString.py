class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        lst=list(s)
        lst1=list(goal)
        flag=''
        for i in lst:
            lst.append(lst[0])
            lst.pop(0)
            if lst==lst1:
                flag=True
                break
            else:
                flag=False
                continue

        return flag
