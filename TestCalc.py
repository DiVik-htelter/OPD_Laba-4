import unittest
import requests
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

  def test_url(self):
    page = requests.get('http://127.0.0.1:5000')
    self.assertEqual(page.status_code,200)
#https://ya.ru/


if __name__ == "__main__":
  unittest.main()