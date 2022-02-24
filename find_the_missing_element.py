#find the missing element

def finder(arr1, arr2):
    diff = sum(arr1)-sum(arr2)
    for i in arr1:
        if i==diff:
            return str(i) + ' is the missing number'

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(finder(arr1,arr2))