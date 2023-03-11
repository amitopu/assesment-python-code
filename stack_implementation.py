#  This implementation of stack data structure is implemented using linked list
# and python 3.10. To run the program open your terminal and write 'Python ./<file_name>.py'.
# To run the program from terminal python should be in the path of the system. This can be also
# run from any ide. Just copy and paste the code to the editor and run using python environment 
# intigrated with IDE


import random

class Node:
    """
        This class is used to create a node for linked list
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """
        This Stack class is used to generate and implement
        stack data structure using linked list. 
        Time complexity for peek() is O(1), for push() is O(1)
        for pop() is O(1) and for is_empty() is O(1)
    """
    def __init__(self):
        self.top = None

    # string represent of the stack
    def __str__(self):
        if self.top == None:
            return '[empty]'
        else:
            output = ''
            current = self.top
            while current:
                output =  " | " + str(current.value) + output
                current = current.next
        
            return "[ " + output + ' ]'

    def push(self, data):
        node = Node(data)
        # if the stack is empty
        # make the new node to top node
        if self.top == None:
            self.top = node
            return
        
        # if the top node is not empty
        # make the current top node to the next node of new node
        # and make the new node to top node
        current_top = self.top
        node.next = current_top
        self.top = node
        return
    
    def pop(self):
        # if the stack is empty, show the message 'The stack is empty'
        # and return 
        if self.top == None:
            print('The stack is empty')
            return
        
        # if only one item left in the stack
        # return the value of the item and make top node to none
        if self.top.next == None:
            value = self.top.value
            self.top = None
            return value
        
        # if there are more than one element in the stack
        # make the next node of the current top node to top node
        # and return the value of the current top node
        value = self.top.value
        new_top = self.top.next
        self.top = new_top
        return value
    
    def peek(self):
        # if the stack is empty, print 'The stack is empty' and return
        if self.top == None:
            print('The stack is empty')
            return
        
        # if the stack is not empty return the top value
        return self.top.value


    def is_empty(self):
        return self.top == None
    

# ---implementation of the stack---
# this section is for testing the resulting stack generated from Stack class.
# first a stack is created and pushed variable number of times with random numbers.
# then random number of different operations are carried out 
# and resulting stack is printed out after each operation.
# change values of start, end, num_of_initial_elements, num_of_operations variables
# to demonstrate the above code.


start = 45
end = 99
num_of_initial_elements = 1
num_of_operations = 50
if __name__ == '__main__':
    my_stack = Stack()
    for i in range(num_of_initial_elements):
        my_stack.push(random.randrange(start, end))
    print('New stack is created: ')
    print(my_stack)
    print('--------------')
    for j in range(num_of_operations):
        operation = random.randint(0,3)
        if operation == 0:
            print('peek() --> ', my_stack.peek())
            print('current stack --> ', my_stack)
            
        elif operation == 1:
            num = random.randrange(50, 100)
            my_stack.push(num)
            print('push({})'.format(num))
            print('current stack --> ', my_stack)
        elif operation == 2:
            print('pop() --> ', my_stack.pop())
            print('current stack --> ', my_stack)
        else:
            print('is_empty() --> ', my_stack.is_empty())
            print('current stack --> ', my_stack)
    print('--------------')