
from src.utils.configInfo import *

c = ConfigAction()
url = c.get_option('STG','url')
username = c.get_option('STG', 'username')
password = c.get_option('STG', 'password')
username1 = c.get_option('STG', 'username1')
locator_username = ("xpath","//input[@type='text' and @class='input-inner']") #账号输入框
locator_password = ("xpath","//input[@type='password' and @class='input-inner']") #密码输入框
locator_vcode = ("xpath","//input[@id='check']")#验证码
locator_button = ("xpath","//span[text()='登录']")

if __name__=="__main__":
    print(url)
    print(username)
    print(username1)
    print(password)

