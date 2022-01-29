"""
Die class
"""
import random

class Die(): #Class
    """ Test class for unittests, derives from unittest.TestCase """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6
    def __init__(self, value = None):
        if value is not None:
            if value > self.MAX_ROLL_VALUE:
                self._value = self.MAX_ROLL_VALUE
            elif value < self.MIN_ROLL_VALUE:
                self._value = self.MIN_ROLL_VALUE
            else:
                self._value = value
        else:
            self._value = random.randint(1,6)

    def get_name(self):
        """Get_name function."""
        values_to_str = {
    		1: 'one',
    		2: 'two',
    		3: 'three',
    		4: 'four',
    		5: 'five',
    		6: 'six',
}
        return f'{values_to_str.get(self._value)}'

    def get_value(self):
        """get_value function."""
        return self._value

    def roll(self):
        """roll function"""
        self._value = random.randint(1,6)

    def __str__(self):
        """str function."""
        return str(self._value)

    def __eq__(self, helt = None):
        """eq method"""
        if isinstance(helt, Die):
            if helt.get_value() == self.get_value():
                return True
        elif isinstance(helt, int):
            if helt == self.get_value():
                return True

        return False
