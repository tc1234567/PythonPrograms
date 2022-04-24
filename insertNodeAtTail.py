class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        
def insertNodeAtTail(head, data):
    
    node = SinglyLinkedListNode(data)
    
    #two cases 
    
    #1 - if linked list is empty - add elements to it
    if head == None:
        head = node
    #2 - if linked list has elements add new element at the end
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
            
        temp.next = node
        
    return head