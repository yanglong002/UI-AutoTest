import src.page.loginPage as lg
from src.utils.baseUtil import *
from src.utils.funcUtil import *
import unittest
import time

class Login(unittest.TestCase):
    def setUp(self):
       self.base = Base()
       self.base.open(lg.url)

    @pic_deco
    def test_login(self):
        #username11不存在,故意出错,截图
        base = self.base

        try:
            login(base, lg.url, lg.username11, lg.password)
        except:
            log.error("登录失败")
            raise ElementError("定位错误")
    def tearDown(self):
       self.base.quit()

# base =  Base()
# base.open(lg.url)
#
# login(base,lg.url,lg.username1,lg.password)
if __name__ == "__main__":
    unittest.main()

