import unittest
from facade import PointWrapper

class TestPointWrapper(unittest.TestCase):
    def test_initialization(self):
        point = PointWrapper(10, 20)
        self.assertEqual(point.x, 10)
        self.assertEqual(point.y, 20)

    def test_move(self):
        point = PointWrapper(10, 20)
        moved_point = point.move(5, -3)
        self.assertEqual(moved_point.x, 15)
        self.assertEqual(moved_point.y, 17)

    def test_move_in_place(self):
        point = PointWrapper(10, 20)
        point.move_in_place(-2, 4)
        self.assertEqual(point.x, 8)
        self.assertEqual(point.y, 24)

    def test_repr(self):
        point = PointWrapper(10, 20)
        self.assertEqual(repr(point), "PointWrapper(x=10, y=20)")

if __name__ == '__main__':
    unittest.main()