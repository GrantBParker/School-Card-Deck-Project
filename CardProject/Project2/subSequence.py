from copy import deepcopy
from linkedList import LinkedList

class SubSequence(LinkedList):
    """
    This class represents a SubSequence of Cards from the Deck.
    This class inherits from the LinkedList class.

    The CardSorter holds a Python list of these SubSequence objects.

    There are no instance variables for this class, except for those
    inherited from the LinkedList class.

    The class methods include 
    a. __init__: This method calls the LinkedList constructor 
                 using super()
    b. first_card: This method returns a reference to the Card at 
                   the head of the LinkedList without removing it.
    c. add_card: This method adds a Node to the front of the 
                 LinkedList containing the passed in Card.
    d. contains_card: This method searches the LinkedList for the 
                      passed in Card and returns true if Card is in 
                      this SubSequence, or False if not.               
    e. clone_subseq: This method returns a deep copy of this 
                     SubSequence. It traverses this SubSequence and 
                     adds a deepcopy of every Node at the end of the 
                     new SubSequence being returned.
    f. reverse_subseq: This method reverses this SubSequence in place.  
                       It uses three Node pointers: a current_node to 
                       walk the SubSequence, a prev_node to follow the 
                       current_node, and a next_node to grab the Node 
                       in front of current_node, as it walks the
                       LinkedList.
    g. __str__ : This method returns a string of the Cards in the 
                 SubSequence.                  
    """
    
    def __init__(self):
        """
        This method is the SubSequence constructor.  Call the
        LinkedList constructor using super()
        """
        
        ## Add your code here ##
        super().__init__()
        
    def first_card(self):
        """
        This method returns a reference to the Card at the head 
        of the LinkedList without removing it.
        """
        
        ## Add your code here ##
        return self._head.data
        
    def add_card(self, card):
        """
        This method adds a Node to the front of the LinkedList 
        containing the passed in Card
        """
        
        ## Add your code here ##
        card = self._head.data

    def contains_card(self, card):
        """
        This method searches the LinkedList for the passed in Card 
        and returns true if Card is in this SubSequence, or False
        if not.
        """
              
        ## Add your code here ##
        current_node = self._head
        while current_node is not None:
            if current_node.data.compare(card) == 0:
                return True

            current_node = current_node.next
        return False

    def clone_subseq (self):
        """
        This method returns a deep copy of this SubSequence.  
        It traverses this SubSequence and adds a deepcopy of every 
        Node ( deepcopy is a method in the Python copy module. ).
        Add the copied Node at the END of the new SubSequence 
        being returned.
        """
        
        ## Add your code here ##
        new_clone = SubSequence()
        current_node = self._head
        while current_node is not None:
            new_clone.add_last(deepcopy(current_node.data))
            current_node = current_node.next
        return new_clone

        
    def reverse_subseq (self):
        """
        This method reverses this SubSequence in place.  It uses 
        three Node pointers: a current_node to walk the SubSequence,
        a prev_node to follow the current_node, and a next_node to
        grab the Node in front of current_node, as it walks the
        LinkedList. 
        """
        
        prev_node = None
        current_node = self._head
        for n in range(self.get_size()):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self._head = prev_node

    def __str__(self): 
        """
        This method returns a string containing the Cards
        in this SubSequence. 
        """
        
        ## Add your code here ##
        data_str = ""
        current = self._head

        for i in range(self.get_size()):
            data_str += str(current.data) + " "
            current = current.next

        return data_str
    
       
