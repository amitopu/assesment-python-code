import random

class Node:
    """
        This class is used to create a node for linked list
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """
        This Queus class is used to generate and implement
        queue data structure using linked list. 
        Time complexity for peek() is O(1), for enqueue() is O(1)
        for dequeue() is O(1) and for is_empty() is O(1)
    """
    def __init__(self):
        # initialize an empty queue
        self.front = None
        self.back = None

    def __str__(self):
        # if the queue is empty
        if self.front == None:
            return '[empty]'
        
        # if the queue is not empty
        output = ''
        front = self.front
        while front:
            if front.next == None:
                output += str(front.value)
                front = front.next
            else:
                output += str(front.value) + ' | '
                front = front.next
        output = '[ front-->' + output + '<--back ]'
        return output

    def enqueue(self, item):
        # create a new node with item value
        node = Node(item)
        # if the queue is empty add the node to both front and back of the queue
        if self.front == None:
            self.front = node
            self.back = node
            return
        # if at least one element remains in the queue
        # then the front and back of the queue is not empty
        # add the new node to the next to the current back and
        # refer the back of the queue to the new node added and
        # keep the front of the queue unchanged.
        if self.back:
            self.back.next = node
            self.back = node
            return

    def dequeue(self):
        # if the queue is empty, print 'The queue is empty'
        # and return 
        if self.front == None:
            print('The queue is empty')
            return
        # if there is at least one element in the queue, take the value
        # of the element and make both the front and the back to None
        # return the value of the element
        if self.front.next == None:
            front_value = self.front.value
            self.front = None
            self.back = None
            return front_value
        # if there are more than one element then take the front value,
        # keep the next of the current front to a temporary variable which
        # will be the new front
        # and return the front value.
        # The back will be remain unchanged
        front_value = self.front.value
        new_front = self.front.next
        self.front = new_front
        return front_value
    
    def peek(self):
        # if the queue is empty
        if self.front == None:
            print('The queue is empty')
            return
        else:
            # if the queue is not empty, return front value
            return self.front.value
        
    def is_empty(self):
        # return if the front is None or not None which indicates 
        # if the queue is empty or not.
        return  self.front == None


# ---implementation of the queue---
# this section is for testing the resulting queue generated from queue class.
# first a queue is created and pushed variable number of times with random numbers.
# then random number of different operations are carried out 
# and resulting queue is printed out after each operation.
# change values of start, end, num_of_initial_elements, num_of_operations variables
# to demonstrate the above code.

start = 45
end = 890
num_of_initial_elements = 5
num_of_operations = 10
if __name__ == "__main__":
    my_queue = Queue()
    for i in range(num_of_initial_elements):
        my_queue.enqueue(random.randrange(start, end))
    print(my_queue)
    print('--------------')
    for j in range(num_of_operations):
        operation = random.randint(0,3)
        if operation == 0:
            print('peek() --> ', my_queue.peek())
            print('current queue --> ', my_queue)
            
        elif operation == 1:
            num = random.randrange(50, 100)
            my_queue.enqueue(num)
            print('enqueue({})'.format(num))
            print('current queue --> ', my_queue)
        elif operation == 2:
            print('dequeue() --> ', my_queue.dequeue())
            print('current queue --> ', my_queue)
        else:
            print('is_empty() --> ', my_queue.is_empty())
            print('current queue --> ', my_queue)
    print('--------------')