import unittest
from src.utils.ExcelData import *

from src.case.math_method import MathMethod
from config import configInfo as cf
import os

class TestMathMethod2(unittest.TestCase):

    def __init__(self, case_id, title, a, b, expected, methodName):
        super(TestMathMethod2, self).__init__(methodName)
        self.case_id = case_id
        self.title = title
        self.a = a
        self.b = b
        self.expected = expected


    def setUp(self):
        file_path = os.path.join(cf.data_path, 'python.xlsx')
        self.t = DoExcelData(file_path,'test')

    def tearDown(self):
        print('--测试完毕--')

    def test_13_two_zero_add(self):
        res = MathMethod(self.a, self.b).add()
        try:
            self.assertEqual(res, self.expected)
            TestResult = 'Pass'
        except AssertionError as e:
            TestResult = 'Failed'
            print('断言出错了,错误是:{}'.format(e))
        finally:
            self.t.write_back(self.case_id+1, 6, res) #写入指定的第6列
            self.t.write_back(self.case_id+1, 7, TestResult) #写入指定的第7列

        print("{0}+{1}结果是：{2}".format(self.a, self.b, int(self.a + self.b)))


if __name__ == "__main__":
    unittest.main()