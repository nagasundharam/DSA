# Doubly LinkedList
        #  contains

        # node contains previous link and next link

        # prev.link refers prev data 

        # next.link refers next data

# Doubly linked list Traversal

class Node:
        def __init__(self,data):
                self.data = data
                self.prev = None
                self.next = None
                
class DoublyLL:
        def __init__(self):
                self.head = None

        def Print_DLL(self):
                
                if self.head is None:
                        print("Linked List is empty")
                
                else:
                        n = self.head
                        while n.next is not None:
                                print(n.data,'-->',end ='')
                                n = n.next
                        

        def Print_DLL_rev(self):
              
                
                if self.head is None:
                        print("Linked List is empty")
                
                else:
                        n = self.head
                        while n.next is not None:
                                
                                n = n.next
                        
                        while n.prev is not None:
                                print(n.data,'-->',end ="")
                                n = n.prev
                
                

dl1 = DoublyLL()
dl1.Print_DLL()
        





        

