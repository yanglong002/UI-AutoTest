import unittest

from src.case.math_method import MathMethod

class TestMathMethod(unittest.TestCase):


    def setUp(self):
        self.data = [[0,0],[-1,-3],[3,-1]]

    def tearDown(self):
        print("---执行完毕---")

    def test_3_two_zero_add(self):
        res = MathMethod(self.data[0][0], self.data[0][1]).add()
        self.assertEqual(1, res)

        print("两个0相加的结果是：{0}".format(res))

    def test_2_two_negative_add(self):
        res = MathMethod(self.data[1][0], self.data[1][1]).add()
        self.assertEqual(2, res)

        print("两个负数相加的结果是：{0}".format(res))

    def test_1_positive_negative_add(self):
        res = MathMethod(self.data[2][0], self.data[2][1]).add()
        self.assertEqual(3, res)

        print("一正一负相加的结果是：{0}".format(res))

if __name__ == "__main__":
    unittest.main()