"""
Rule module
"""
from abc import ABC, abstractmethod

class Rule(ABC):
    """class rule"""
    # @abstractmethod
    @abstractmethod
    def points(self, hand):
        """ points method """


class SameValueRule(Rule):
    """class samevaluerule"""
    def __init__(self, value, name):
        self.value = value
        self.name = name

    def points(self, hand): #1 2 3 4 5
        """ points method """

        total = 0
        for i in hand.to_list():
            if i == self.value:
                total += 1

        return total * self.value

class Ones(SameValueRule):
    """ones class"""
    def __init__(self):
        super().__init__(1, "Ones")


class Twos(SameValueRule):
    """twos class"""
    def __init__(self):
        super().__init__(2, "Twos")

class Threes(SameValueRule):
    """threes class"""
    def __init__(self):
        super().__init__(3, "Threes")

class Fours(SameValueRule):
    """fours class"""
    def __init__(self):
        super().__init__(4, "Fours")

class Fives(SameValueRule):
    """fives class"""
    def __init__(self):
        super().__init__(5, "Fives")

class Sixes(SameValueRule):
    """sixes class"""
    def __init__(self):
        super().__init__(6, "Sixes")

class ThreeOfAKind(Rule):
    """three of a kind class"""
    def __init__(self):
        self.name = "Three Of A Kind"

    def points(self, hand):
        """ points method """
        listem = hand.to_list()
        liste = [1,2,3,4,5,6]
        for i in enumerate(liste):
            if listem.count(i[1]) >= 3:
                return sum(hand.to_list())
        return 0

class FourOfAKind(Rule):
    """four of a kind class"""
    def __init__(self):
        self.name = "Four Of A Kind"

    def points(self, hand):
        """points method"""
        liste = [1,2,3,4,5,6]
        for i in enumerate(liste):
            if hand.to_list().count(i[1]) >= 4:
                return sum(hand.to_list())
        return 0

class FullHouse(Rule):
    """full house class"""
    def __init__(self):
        self.name = "Full House"

    def points(self, hand):
        """ points method """
        liste = [1,2,3,4,5,6]
        val_list = []
        my_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

        for i in liste:
            for j in hand.to_list():
                if i == j:
                    my_dict[j]+=1

        for j in my_dict.values():
            val_list.append(j)

        if 2 in val_list and 3 in val_list:
            return 25
        return 0

class SmallStraight(Rule):
    """small straight class"""
    def __init__(self):
        self.name = "Small Straight"

    def points(self, hand):
        """ points method """
        listex = hand.to_list()
        listex.sort()
        listem = list(dict.fromkeys(listex))
        total = 1
        new_list = []
        for i in range(len(listem[:-1])):
            if listem[i] + 1 == listem[i+1]:
                total += 1
            else:
                new_list.append(total)
                total = 1
        new_list.append(total)
        if max(new_list) == 4:
            return 30

        return 0

class LargeStraight(Rule):
    """large straight class"""
    def __init__(self):
        self.name = "Large Straight"

    def points(self, hand):
        """ points method """
        hand.to_list().sort()
        listem = list(dict.fromkeys(hand.to_list()))
        if len(listem) == 5:
            return 40
        return 0

class Yahtzee(Rule):
    """yahtzee class"""
    def __init__(self):
        self.name = "Yahtzee"

    def points(self, hand):
        """ points method """
        if hand.to_list().count(hand.to_list()[0]) == len(hand.to_list()):
            return 50
        return 0

class Chance(Rule):
    """chance class"""
    def __init__(self):
        self.name = "Chance"

    def points(self, hand):
        """ points method """
        return sum(hand.to_list())
