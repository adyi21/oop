"""
hand module
"""
from src.die import Die

class Hand():
    """A hand class."""

    def __init__(self, values = None):
        self.dice = []
        if values is not None:
            for j in values:
                self.dice.append(Die(j))
        else:
            die1 = Die()
            die2 = Die()
            die3 = Die()
            die4 = Die()
            die5 = Die()
            self.dice = [die1, die2, die3, die4, die5]

    def roll(self, indexes = None):
        """Roll function."""
        if indexes is None:
            for i,j in enumerate(self.dice):
                self.dice[i].roll()
        else:
            for i,j in enumerate(indexes):
                self.dice[j].roll()

    def __str__(self):
        """str function."""
        str_name = ""
        for i in self.dice:
            str_name += str(i.get_value()) + ", "
        return str_name[:-2]

    # @staticmethod
    def to_list(self):
        """to list method"""
        listem = []
        for i in self.dice: #die list i is die
            listem.append(i.get_value())
        return listem
