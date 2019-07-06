
import src.page.loginPage as lg
from src.utils.baseUtil import *
from src.utils.funcUtil import *
import time
loator_DM = ("xpath","//span[text()='数字化营销']")
locator_strategy = ("xpath","//a[text()='公司战略']")
# locator_addStrategy = ("xpath","//span[contains(text(),'添加战略')]")
# //span[contains(text(),'添加战略')]/../../button
locator_addStrategy = ("xpath","//span[contains(text(),'添加战略')]")
locator_hospLev = ("xpath","//input[@placeholder='请选择医院级别']")
locator_threeBest = ("xpath","//*[text()='一级甲等']")
locator_scroll = ("xpath","//div[contains(@class,'is-vertical')][1]")
base =  Base()
base.open(lg.url)

login(base,lg.url,lg.username1,lg.password)
"""数字化营销页"""
base.move_to_element(loator_DM,"数字化营销")
base.click(locator_strategy,"公司战略")
js='document.getElementsByClassName("el-button el-button--primary")[3].click()'#普通方法点击不到"添加战略"
base.driver.execute_script(js)
# base.click(locator_addStrategy, "添加战略")  #普通的方法点击不到

# base.click(locator_addStrategy,"添加战略")
# base.js_focus_element(locator_addStrategy)
# base.click(locator_addStrategy, "添加战略")
"""点击医院级别输入框"""


"""去掉readonly属性"""
# js1 = 'document.querySelectorAll('+"\"input[placeholder='请选择医院级别']\""+")[0].removeAttribute('readonly');"
# base.driver.execute_script(js1)
# js2 = 'document.querySelectorAll('+"\"input[placeholder='请选择医院级别']\""+")[0].value='三级甲等';"
# base.driver.execute_script(js2)


# """css方法进行定位操作，可以操作,但是无反应"""
# js3 = 'document.querySelectorAll('+"\"input[placeholder='请选择医院级别']\""+")[0].click();"
# base.driver.execute_script(js3)

# """xpath方法定位进行操作"""
js4='document.getElementsByClassName("el-input__icon el-icon-caret-top")[4].click();'
base.js_excute(js4)
wait(5)
base.move_to_element(locator_threeBest)

"""滚动条"""
# document.getElementsByClassName("el-scrollbar__thumb")[11].
js5='document.getElementsByClassName("el-scrollbar__thumb")[11].style="transform: translateY(50%); height: 46.7391%;"'
base.js_excute(js5)
