import unittest
import sys
import os

sys.path.append(f'../app/')
from Cryptography.Encode import  Encode
from Cryptography.Decode import  Decode

class appTest(unittest.TestCase):

  def test_numberWhitLetter(self):
    with self.assertRaisesRegex(ValueError, "The number must have only integer numbers."):
      Encode().GetCode("14587a")

  def test_numberGreaterThan8(self):
    with self.assertRaisesRegex(ValueError, "The number lenght must be less or equal 8."):
      Encode().GetCode(123456789)


  def test_codeLess6Digit(self):
    with self.assertRaisesRegex(ValueError, "The code lenght must be equal 6."):
      Decode().GetNumber("ertdg")

  def test_codeGreaterThan6Digit(self):
    with self.assertRaisesRegex(ValueError, "The code lenght must be equal 6."):
      Decode().GetNumber("!@fa586")

  def test_codeEmpty(self):
    with self.assertRaisesRegex(ValueError, "The code lenght must be equal 6."):
      Decode().GetNumber("")
  
  def test_codeInvalid(self):
    with self.assertRaisesRegex(ValueError, "The code is invalid."):
      Decode().GetNumber("!!!!!]")

  def test_cryptography(self):

    numbers = [99999999,0,1587,888587]

    for number in numbers:
      code = Encode().GetCode(number)
      decodedNumber = Decode().GetNumber(code) 
      self.assertTrue(number == decodedNumber)


if __name__ == '__main__':
    unittest.main()