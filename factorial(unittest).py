import unittest
import factorial

class TestFactorialMethods(unittest.TestCase):
  def test_normal_values(self):
   self.assertEqual(fact(2),2)
   self.assertEqual(fact(7),5040)
   self.assertEqual(fact(9),362880)
  def test_except_ValueError(self):
   with self.assertRaises(ValueError):
    fact(-1)
   with self.assertRaises(ValueError):
    fact(-0.5)
  def test_except_TypeError(self):
   with self.assertRaises(TypeError):
    fact(0.2)
   with self.assertRaises(TypeError):
    fact([0,2,7,9])
   with self.assertRaises(TypeError):
    fact('listik')
