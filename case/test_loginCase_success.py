import src.page.loginPage as lg
from src.utils.baseUtil import *
from src.utils.funcUtil import *
import unittest
import time

class Login(unittest.TestCase):


    def setUp(self):
        self.base = Base()

    @pic_deco
    def test_login_success(self):
        self.base.open(lg.url)
        base = self.base
        try:
            login(base, lg.url, lg.username1, lg.password)
        except:
            self.assertTrue(False, "登录失败")
    # @pic_deco
    # def test_login_fail(self):
    #     self.base.open(lg.url)
    #     # username11定位元素故意错误,为了截图
    #     base = self.base
    #     login(base, lg.url, lg.username1, lg.password)


    # def test_login(self):
    #     self.base.open(lg.url)
    #     base = self.base
    #     login(base, lg.url, lg.username1, lg.password)
    #
    # def test_open_baidu(self):
    #     self.base.open_window(r"https://www.baidu.com")
    #     wait(5)
    # def test_open(self):
    #     self.base.open_window("https://www.cnblogs.com/yoyoketang/")

    def tearDown(self):
      self.base.quit()



# base =  Base()
# base.open(lg.url)
#
# login(base,lg.url,lg.username1,lg.password)
if __name__ == "__main__":
    unittest.main()

