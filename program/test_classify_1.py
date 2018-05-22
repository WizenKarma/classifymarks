
import unittest

import classify

class TestListSize(unittest.TestCase):
	
	def test_equal(self):
		a = classify.getData(open('marks.dat'))
		self.assertEqual(len(a),6)

if __name__ == '__main__':
	unittest.main()
