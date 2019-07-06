import unittest
from src.utils.ExcelData import *

from src.case.math_method import MathMethod
from config import configInfo as cf
import os

from ddt import ddt, data
file_name = os.path.join(cf.data_path, 'python.xlsx')
sheet_name = 'test'
cases = DoExcelData(file_name, sheet_name).get_data2()
print(cases)



@ddt
class TestMathMethod3(unittest.TestCase):

    def setUp(self):
        self.t = DoExcelData(file_name, sheet_name)


    @data(*cases)
    def test_13_two_zero_add(self,case):
        res = MathMethod(case.a, case.b).add()
        try:
            self.assertEqual(res, case.expected)
            TestResult = 'Pass'
        except AssertionError as e:
            TestResult = 'Failed'
            print('断言出错了,错误是:{}'.format(e))
        finally:
            self.t.write_back(case.case_id+1, 6, res) #写入指定的第6列
            self.t.write_back(case.case_id+1, 7, TestResult) #写入指定的第7列

        print("{0}+{1}结果是：{2}".format(case.a, case.b, int(case.a + case.b)))


if __name__ == "__main__":
    unittest.main()