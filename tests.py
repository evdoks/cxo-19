import unittest

from  my_math.quadratic import quadratic_eq


class TestQuadraticEq(unittest.TestCase):

    def test_quadratic_eq_discr_positive(self):
    	""" Test quadratic_eq() for solving a quadratic
    	equation with positive discriminant
    	"""
    	x1, x2 = quadratic_eq(1, 3, -4)
    	self.assertListEqual([x1, x2], [1.0, -4.0])
    
    def test_quadratic_eq_discr_zero(self):
    	""" Test quadratic_eq() for solving a quadratic
    	equation with zero discriminant
    	"""
    	x1, x2 = quadratic_eq(1, 2, 1)
    	self.assertListEqual([x1, x2], [-1, -1])

    def test_quadratic_eq_discr_negative(self):
    	""" Test quadratic_eq() for solving a quadratic
    	equation with negative discriminant
    	"""
    	x1, x2 = quadratic_eq(2, 1, 1)
    	self.assertListEqual([x1, x2], [None, None])


if __name__ == '__main__':
    unittest.main()