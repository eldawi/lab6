import unittest
from add import Task

class Testadd(unittest.TestCase):
  def test_add(self):
    result = Task.add(2, 8)
    self.assertEqual(result, 10)

    result = Task.add(4, 4)
    self.assertEqual(result, 8)

    result = Task.add(6, 3)
    self.assertEqual(result, 9)
