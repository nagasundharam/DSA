# LinkedList :
# linked list contains node

#  Each  node contains  data and next  or reference to the next node
  

# we dont need to store a specific part of the memory or contagious memory allocation

# linked list it is dynamic memory allocation 


# advantages:
#     - dynamic
#     - easily insertable or deletable
#     - you can implement stack , queue and graph
#     it is used in web browser  and as well as  memory
# real time usage  -- we browser 
                    # -- music Player
                    # -- Image viewer


# disadvantages
       
    #    -- Needs extra memory
    #   --  Random access not possible
    

# LINKEDLIST TYPES:
    #  --- Singly LinkedList
    #  --- doubly LinkedList
    #  --- circular LinkedList

# Singly Linked List

# Add/Insertion
#   --> Begin
#   --> end
#   --> inbetween   


# Linked list creating

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    # traversal operation
    def print_LL(self):
        if self.head is None:
            print("list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,'--->',end='')
                n = n.ref
    
    #adding into the element in the begin

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref  is not None:
                n = n.ref
            n.ref = new_node

    def after_node(self,data,x):

        n = self.head
        while n is not None:
            if (n.data == x):
                break
         
            n = n.ref

        if (n is  None):
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def before_node(self,data,x):
        if self.head is None:
            print("Linked List is Empty")
            return

        if self.head.data  == x :
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        else:
            n = self.head
            while n is not None :
                if (n.ref.data == x):
                    break
                n = n.ref
            if n.ref is None:
                print("we didnt find any value")
                return
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

        

        

        


         






    #
   
       

ll1 = LinkedList()
ll1.insert_empty(10)
ll1.insert_empty(20)
# ll1.after_node(80,100)

ll1.print_LL()
    

   

# node1 = Node(10)
# print(node1)  #<__main__.Node object at 0x00000145081561B0>



  




