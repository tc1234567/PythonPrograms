def minimumAbsoluteDifference(arr):
      
    arr.sort()

    temp_list = []
    temp_list2 = []

    mindiff = 10000000
    for i in range(len(arr)-1):
        if abs(arr[i+1]-arr[i]) < mindiff:
            mindiff = abs(arr[i+1]-arr[i])
                
            temp_list.append(mindiff)
            
    return min(temp_list)