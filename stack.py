# stack
#    -> stack is a user defined data structure
#    --> last in first out manner


# #push  --> append
# pop ---> remove

# stack implemeting using list

# stack = []
# def push():
#     element = input("enter the Element")
#     stack.append(element)
#     print(stack)

# def pop():
#     if not stack:
#         print("stack is empty")
#     else:
#         e = stack.pop()
#         print("remved element :",e)
#         print(stack)
# while True:
#     print("select the opertaion 1. push 2.pop 3.quit")
#     choice  = int(input())
#     if choice  == 1:
#         push()
    
#     elif choice == 2:
#         pop()
#     elif choice == 3 :

#         break





# stack implementing using modules

# --> collections module  -- there is an class called deque


# import collections
# stack =  collections.deque()
# print(stack)
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# stack.pop()
# stack.pop()
# print(stack)
# stack.pop()
# print(not stack)  # this find stack is empty or not

# print(stack[-1])  # this gets peak element from the stack




# using queue module from lifoqueue


import queue

stack =  queue.LifoQueue(3)  #--> maximum size is 3

stack.put(10)
stack.put(20)
stack.put(30)
# stack.put(40,timeout = 1)  ==> it returns error stack is empty

print(stack.get())
print(stack.get())
print(stack.get())
# print(stack.get(timeout= 1))  ==> it return error stack is empty






