import unittest
from src.case.test_math_method import *
from src.case.test_math_method1 import *
from src.case import test_math_method1
from src.case.test_math_method3 import *

from src.utils.funcUtil import *

# 方法一:单个用例添加
# suite = unittest.TestSuite()
# suite.addTest(TestMathMethod('test_3_two_zero_add'))
# suite.addTest(TestMathMethod('test_2_two_negative_add'))
#
# runner = unittest.TextTestRunner()
# runner.run(suite)


# 方法二:从类中加载测试用例


# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))
# suite.addTest(loader.loadTestsFromTestCase(TestMathMethod1))
#
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 方法三:从模块中添加
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_math_method1)) # 从模块中添加
# runner = unittest.TextTestRunner()
# runner.run(suite)

# run()


# 方法一:单个用例添加



from config import configInfo as cf

# 1.通过封装的DoExcelData来获取数据


# 2.各种数据测试某一条测试用例,加入suite
suite = unittest.TestSuite()
loader = unittest.TestLoader()

# 测试类使用的是ddt
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod3))

print(suite)
# 3.生成测试报告
@threads(3)
def run(suite):
    localtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_name = '自动化测试报告' + localtime
    result = BeautifulReport(suite)
    result.report(filename=report_name, description='测试deafult报告', log_path=cf.report_path)
    result.add_test_img()


run(suite)