def compareTriplets(a, b):

    temp_lista = []
    temp_listb = []
    temp_list = []

    for k in range(0, len(a)):
        initial = 1
        
        if a[k] > b[k]:
            
            temp_lista.append(initial)
            initial +=1

        elif a[k] == b[k]:
            pass
        
        else:
            temp_listb.append(initial)
            initial +=1
            
    x = sum(temp_lista)
    y = sum(temp_listb)
    temp_list.insert(0, str(x))
    temp_list.insert(1, str(y))

    return (temp_list)
