class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None 

def insertNodeatHead(self, head, data):
        
    if head is None:
        head = SinglyLinkedListNode(data)
        return head
    else:
        temp = head
        head = SinglyLinkedListNode(data)
        head.next = temp
        

