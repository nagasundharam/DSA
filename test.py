class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None
    

class LinkedList():
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print("there is no element in ll")
        else:
            n = self.head
            while n is not None:
                print(n.data,'--->',end='')
                n = n.next
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node

    def  add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        if self.head is None:
            add_begin(data)
        else :
            n = self.head
            while n.next is not None:
                n = n.next

            new_node = Node(data)
            n.next = new_node
    
    def before_node(self,data,x):
        if self.head is None:
            print("LL is empty")
        if self.head  == x :
            new_node = Node(data)
            new_node.next =  self.head.next
            self.head = new_node
        
        else :
            n = self.head
            while n.next is not None:
                if n.next.data == x :
                    break
                n = n.next
            if n.next is None:
                print("there is no element LL ")
            else :
                new_node = Node(data)
                new_node.next  = n.next
                n.next = new_node
            
    def after_node(self,data,x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data  == x:
            new_node = Node(data)
            new_node.next = self.head.next
            self.head.next  = new_node
        else:
            n = self.head
            while n is not None:
                if n.data == x :
                    break
                n =  n.next
            if n is None:
                print("there is no element in LL")
            else:
                new_node= Node(data)
                new_node.next = n.next
                n.next = new_node

    def delete_begin(self):

        if self.head is None:
            print("there is no element in LL")
        else:
            self.head =  self.head.next
    
    def delete_end(self):

        if self.head is None:
            print("there is no element in LL")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            
            n.next = None
    
    def delete_between(self,x):
        if self.head is None:
            print("there is no element in LL")
        else:
            if (self.head.data == x):
                self.delete_begin()
            else:
                n =  self.head
                while n.next is not None:
                    if (n.next.data == x):
                        break
                    n = n.next
                
                n.next = n.next.next
                
                

 

    

        
    
name = {
    "name":"naga",
    "profession":"pyhton developer",
    "life":"changed",
    "work":"need"
}

ll1 = LinkedList()
ll1.insert_empty(name)
ll1.add_begin(5)
ll1.add_begin(7)
ll1.add_begin(9)
ll1.add_begin(11)
ll1.add_end(23)
ll1.add_end(25)
ll1.before_node(24,25)
ll1.delete_begin()
ll1.delete_end()
ll1.delete_between(9)

ll1.print_LL()






            
    

        