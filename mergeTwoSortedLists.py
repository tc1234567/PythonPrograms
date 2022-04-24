def mergeLists(headA, headB):
    
    #checking if either of the lists are null
    if headA == None:
        return headB
    if headB == None:
        return headA
    
    #checking which is the heads is smaller
    if headA.data <= headB.data:
        head = headA
        headA = headA.next
    else:
        head = headB
        headB = headB.next
    
    current = head
    
    #looping until one of the lists becomes null
    while headA != None or headB != None:
        if headA == None:
            current.next = headB
            break
        if headB == None:
            current.next = headA
            break
        if headA.data <= headB.data:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next
        current = current.next
    return head