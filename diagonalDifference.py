def diagonalDifference(arr):
    # Write your code here
    temp_list = []
    m = len(arr)
    for i in range(m):
        temp_list.append(arr[i][i])
        i+=1

    temp_list2 = []

    for i in range(m):
        temp_list2.append(arr[i][m-1])
        m-=1

    return abs((sum(temp_list)) - sum(temp_list2))