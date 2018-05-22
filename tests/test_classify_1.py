
import unittest

import classify

class InequalityTest(unittest.TestCase):
	
	def test_equal(self):
		a = len(classify.getData('marks.dat'))
		b = len(classif.getData('marks.dat'))
		self.assertEqual(a,b)
		


if __name__ == '__main__':
	unittest.TestClassify()
