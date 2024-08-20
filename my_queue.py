# Queue is first in first out manner

# queue methods are 

#      --> enqueue
#      --> dequeue
#      --> isFull
#      --> isEmpty


# queue implementing on list

# enqueue  --> adding element 
# dequeue   --> removing element from front


# first method

# queue = []

# queue.append(10)

# queue.append(20)
# queue.append(30)

# print(queue)

# print(queue.pop(0))

# print(queue.pop(0))

# print(queue.pop(0))


# # second method

# queue = []

# print(not queue) #is empty
# queue.insert(0,10)
# queue.insert(0,50)
# queue.insert(0,90)
# print(queue[-1])

# print(queue)

# print(queue.pop())
# print(queue.pop())
# print(queue.pop())



# queue implemeting using modules

# first method:
# deque --> collections


# import  collections

# q = collections.deque()
# print(q)

# q.appendleft(10)
# q.appendleft(20)
# q.appendleft(30)

# print(q)

# q.pop()

# q.pop()
# q.pop()
# # q.pop()IndexError: pop from an empty deque




# # second method:

# q.insert(0,10)
# q.insert(0,20)
# q.insert(0,30)
# q.insert(0,40)

# print(q.popleft())
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())
# # print(q.popleft())IndexError: pop from an empty deque



# import queue 



# q = queue.Queue()

# q.put(10)
# q.put(50)
# q.put(30)
# print(q)





# //priority queue//

# q  = []
# q.append(10)
# q.append(40)
# q.sort()
# q.append(20)
# q.sort()
# # print(q) [10, 20, 40]
# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))


import queue

q = queue.PriorityQueue()
q.put(10)
q.put(60)
q.put(20)
q.put(40)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

 