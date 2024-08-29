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
                        while n is not None:
                                print(n.data,'-->',end ='')
                                n = n.next
                        

        def Print_DLL_rev(self):
              
                
                if self.head is None:
                        print("Linked List is empty")
                
                else:
                        n = self.head
                        while n.next is not None:
                                
                                n = n.next
                        
                        while n is not None:
                                print(n.data,'-->',end ="")
                                n = n.prev
                
        def insert_empty(self,data):
                if self.head is None:
                        new_node = Node(data)
                        self.head = new_node
                else:
                        print("allready something there")
                
        def add_begin(self,data):
                new_node = Node(data)
                if self.head is None:
                        
                        self.head = new_node
                else:
                        
                        new_node.next = self.head
                        self.head.prev = new_node
                        self.head = new_node
                
        def add_end(self,data):
                if self.head is None:
                        print("there is no data there")
                else:
                        new_node = Node(data)
                        n = self.head
                        while n.next is not None:
                                n = n.next
                        n.next = new_node
                        new_node.prev = n
        def add_before(self,data,x):
                if self.head is None:
                        print("ll is empty")
                else:
                        if self.head.data == x:
                                self.add_begin(data)
                        else:
                                n = self.head
                                while n is not None:
                                        if (n.data == x):
                                                break

                                        n = n.next
                                if n is None:
                                        print("there is no element")
                                else:
                                        new_node = Node(data)
                                        new_node.next = n
                                        new_node.prev = n.prev
                                        n.prev.next = new_node
                                        n.prev = new_node
        
        def add_after(self,data,x):
                if self.head is None:
                        print("there is no element in ll")
                else:
                        n = self.head

                        while n is not None:
                                if n.data == x :
                                        break
                                n = n.next
                        if n is None:
                                print("Not Found")
                        else:
                                new_node = Node(data)
                                new_node.next = n.next
                                new_node.prev = n
                                if n.next is not None:
                                        n.next.prev =new_node
                                n.next = new_node

                                




        


        


dl1 = DoublyLL()
dl1.insert_empty(30)

dl1.add_begin(40)
dl1.add_begin(50)
dl1.add_end(100)
dl1.add_before(45,50)
dl1.add_after(105,100)
dl1.Print_DLL()
        





        

