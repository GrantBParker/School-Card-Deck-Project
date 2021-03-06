class _StackNode():
    """
    This class represents the Node of a Stack implemented as a 
    LinkedList.
    
    The instances variables of this class include:
    1. self.item: holds the item for the StackNode.
    2. self.next: holds the pointer to the next StackNode.
    
    The class methods include: 
    a. __init__: This method is the constructor and it initializes 
                 each instance variable to the passed in parameters.
    """
    
    def __init__(self, item, link):
        """
        This method is the constructor and it initializes each
        instance variable to the passed in parameters.
        """
        
        ## Add your code here ##
        self.item = item
        self.link = link

        
class Stack():
    """
    This Stack class is a singly LinkedList implementation of a Stack.
    
    The instances variables of this class include:
    1. self._top: holds the pointer to the top StackNode of the Stack
    2. self._size: holds the number of StackNode on the Stack.
    
    The class methods include: 
    a. __init__: This method is the constructor and it initializes 
                 the Stack instance variables.
    b. is_empty: This method returns True, if the Stack  is empty or 
                 False otherwise.
    c. __len__: This method returns the number of items in the Stack.
    d. peek: This method returns the top item on the Stack without 
             removing it.
    e. pop: This method removes and returns the top item on the Stack.
    f. push: This method pushes an item onto the top of the Stack.
    g. __str__: This method returns the contents of the Stack as a 
                string. 
    """
    
    def __init__(self):
        """
        This method is the constructor and it initializes the Stack 
        instance variables, creating an empty Stack.
        """
        
        ## Add your code here ##
        self._top = None
        self._size = 0
        
    def is_empty(self):
        """
        This method returns True if the Stack is empty or False 
        otherwise.
        """
        
        ## Add your code here ##
        return self._size == 0

    def __len__(self):
        """
        This method returns the number of items in the Stack.
        """
        
        ## Add your code here ##
        return self._size

    def peek(self):
        """
        This method returns the top item on the Stack without 
        removing it.
        """
        
        ## Add your code here ##
        return self._top.item

    def pop(self):
        """
        This method removes and returns the top item on the Stack.
        """
        
        ## Add your code here ##
        if self._size == 0:
            return None
        node = self._top
        self._top = self._top.link
        self._size -= 1
        return node.item

    def push(self, item):
        """
        This method pushes an item onto the top of the Stack.
        """
        
        ## Add your code here ##
        self._top = _StackNode(item, self._top)
        self._size += 1
        
    def __str__(self):
        """
        This method returns the contents of the Stack as a string
        """
        
        ## Add your code here ##
        current_node = self._top
        item_str = ""
        for d in range(self._size):
           item_str += str(current_node.item) + " "
           current_node = current_node.link
        return item_str
