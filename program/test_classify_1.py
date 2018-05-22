
import unittest

import classify

class InequalityTest(unittest.TestCase):
	
	def test_equal(self):
		a = classify.getData(open('marks.dat'))
		b = classify.getData(open('marks.dat'))
		self.assertEqual(len(a),len(b))

if __name__ == '__main__':
	unittest.main()
