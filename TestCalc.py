import unittest
from calc_unit import credit
#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestCalc(unittest.TestCase):
  def setUp(self):
    self.credit = credit()

  def test_anyitent(self):
    self.assertEqual(self.credit.anyitent(1000000,5,25), 5845.9)

  def test_deff(self):
    self.assertEqual(self.credit.deff(1000000,5,25), 1627083.3)
if __name__ == "__main__":
  unittest.main()