
class BinarySearchTree:
    """
        This class creates a BST
    """
    
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        

    # finds the minimum value of a BST by going to the left until None
    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    # if BST is empty then insert a node to it.
    # otherwise compare current node's value to new node value
    # insert the new node to left or to right to maintain BST properties
    # time complexity is O(log(n))  and space complexity is O(1) in average case
    # in worst case time complexity is O(n) and space complexity is O(1)
    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BinarySearchTree(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BinarySearchTree(value)
                    break
                else:
                    current_node = current_node.right
        return self
        
    # time complexity is O(log(n)) and space complexity is O(1) in average case
    # and in worst case time complexity is O(n), space complexity is O(1)
    def delete(self, value, parent_node = None):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.delete(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right   
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break
        return self
    
    # check if the value is in the BST
    # time complexity is O(lon(n)) and space complexity is O(1) in average case.
    # in worst case time complexity is O(n) and space complexity is O(1)
    def search(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False
    

    # size() method returns the number of elements in the tree.
    # using in order traversal of the BST all the elements are 
    # collected in an array and then return the length of the array.
    # time complexity is O(n)
    # space complexity is O(d) where d is the depth of the tree
    # in average case d is equivalent to log(n) and in worst case
    # d is equivalent to n. so in worst case space complexity is O(n)
    # and in average case space complexity is O(log(n))
    def size(self):
        stack = []
        array = []
        if self is not None:
            current = self
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            array.append(current.value)
            current = current.right
        return len(array)
    

if __name__ == "__main__":
    bst = BinarySearchTree(10)
    bst.insert(5)
    bst.insert(7)
    bst.insert(8)
    bst.insert(4)
    bst.insert(1)
    bst.insert(2)
    bst.insert(11)
    bst.insert(15)
    bst.insert(12)
    bst.insert(25)
    bst.insert(0)
    print(bst.size())
    bst.delete(96)
    bst.delete(45)
    print(bst.size())
    bst.insert(36)
    print(bst.search(2))
    print(bst.search(100))
    bst.delete(1)
    print(bst.search(7))
    bst.delete(7)
    print(bst.search(7))
    bst.delete(9)
    print(bst.size())
