from comparable import Comparable

class Card(Comparable):
    """
    This class represents a Comparable playing Card, inheriting from
    the abstract Comparable class,  The number of compares is not 
    kept.  The private instance variables are rank and suit.  The 
    Aces are low and Kings are high.  Both the Rank and Suit within 
    Rank are used for comparison:
    
    Suit: Clubs = 0 
          Diamonds = 1
          Hearts = 2
          Spades = 3
    Rank: Ace = 1
          2-10 = 2-10
          Jack = 11
          Queen = 12
          King = 13 
          
    The instances variables of this class include:
    1. self.__suit: the Card's suit: See above.
    2. self.__rank: the Card's rank: See above. 
    
    The class methods include: 
    a. __init__: This method is the constructor. It initializes 
                 the instance variables with the passed in 
                 parameters.
    b. get_rank: This method returns the Card's rank.
    c. get_suit: This method returns the Card's suit.
    d. compare:  This method compares this Card with another Card
                 passed in.
    e. __str__: This method returns a string representation of the Card, 
                 as rank-suit.  Use a tuple with string representations of the 

    """

    def __init__(self, suit, rank):
    
        """
        Constructor:
        This method is the constructor. It initializes the instance 
        variables with the passed in parameters.
        """
        ## Add your code here ##
        self._suit = suit
        self._rank = rank
        
    def get_rank(self):
        """
        This method returns the Card's rank.
        """
        ## Add your code here ##
        return self._rank

    def get_suit(self):
        """
        This method returns the Card's suit.
        """
        ## Add your code here ##
        return self._suit

    def compare(self, otherCard):
        """
        This method compares this Card with another Card passed in.
        The Cards are first compared by rank, and then by suit within 
        the rank. Aces are low and Kinks are high. The order of the
        suits are from low to high: CLUB, DIAMOND, HEART, SPADE 
        This method returns a positive number if this Card is greater
        than the passed in Card, and a negative number if this Card is
        less than the passed in Card, and 0 if they are equivalent.
        """
        
        ## Add your code here ##
        if otherCard.get_rank() > self._rank:

            return -1

        elif otherCard.get_rank() < self._rank:

            return 1

        else:
            if otherCard.get_suit() > self._suit:

                return -1

            elif otherCard.get_suit() < self._suit:
                return 1

        return 0



        
    def __str__(self):
        """
        This method returns a string representation of the Card, as 
        rank-suit.  Use a tuple with string representations of the 
        Suit, as "C" = Clubs, "D" = Diamonds, "H" = Heats, and
        "S" = Spades.  Use a tuple with string representations of 
        the Rank, as "A" = Aces, "J" = Jacks, "Q" = Queens, and
        K" = Kings.  Let the first element of the tuple be None
        Use the rank and suit of the Card as indexes into the tuples. 
        """
        
        ## Add your code here ##
        suits = ("C", "D", "H", "S")
        ranks = (None, "A", "2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "J", "Q", "K")
        return "{}-{}".format(ranks[self._rank], suits[self._suit])
