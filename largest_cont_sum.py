#largest continuous sum

def large_cont_sum(arr):
    temp_list = []
    sum = arr[0]
    for i in range(1, len(arr)):
        sum += arr[i]
        temp_list.append(sum)
    return max(temp_list)

arr1 = list(map(int, input().split()))
print(large_cont_sum(arr1))
