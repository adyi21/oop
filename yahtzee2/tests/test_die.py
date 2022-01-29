""" Submodule for unittests """
import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    """ Test class for unittests, derives from unittest.TestCase """
    def setUp(self):
        random.seed("haci")

    def test_konstruktorn(self):
        """ testar att skapa ett objekt utan skicka argument """
        my_die = Die() #Act
        self.assertEqual(my_die.get_value(), 6) #Assert

    def test_konst_med(self):
        """ testar att skapa ett objekt med argument """
        my_die = Die(4)
        self.assertEqual(my_die.get_value(), 4)

    def test_konst_med_otillatet(self):
        """ testar att skapa ett objekt med otillåtet argument """
        my_die = Die(100)
        self.assertEqual(my_die.get_value(), 6)

    def test_rolla(self):
        """ testar att rolla """
        my_die_1 = Die(5)
        my_die_1.roll()
        self.assertEqual(my_die_1.get_value(),6)
        my_die_2 = Die(6)
        my_die_2.roll()
        self.assertEqual(my_die_2.get_value(),2)

    def test_get_name(self):
        """ testar get_name returnerar rätt """
        my_die_1 = Die(5)
        self.assertEqual(my_die_1.get_name(), "five")

    def test_str(self):
        """ testar att str returnerar rätt """
        my_die_1 = Die(4)
        self.assertEqual(str(my_die_1), "4")

    def test_eq(self):
        """testar eq """
        my_die_1 = Die(5)
        var_x = 5
        self.assertEqual(my_die_1, var_x)
