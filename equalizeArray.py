def equalizeArray(arr):
    d = {i: arr.count(i) for i in arr}

    val_list = []

    for j in d.values():
        val_list.append(j)
    
    return sum(val_list) - max(val_list)