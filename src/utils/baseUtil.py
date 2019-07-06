
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time,os,random
import src.utils.logUtil
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import config.configInfo as cf
from src.utils.errorClass import *

log = src.utils.logUtil.Log()
class Base(object):
    """
    基于原生的selenium框架做了二次封装.
    """
    def __init__(self,browserName="chrome"):
        #将路径写入环境变量
        #如果在环境变量中已配置,就不需要下面这句代码
        # os.environ['PATH'] = os.environ['PATH'] + ';' + cf.driver_path
        try:
            if browserName.lower() == "chrome":
                self.driver = webdriver.Chrome()
            elif browserName.lower() == "firefox":
                self.driver = webdriver.Firefox()
            elif browserName.lower() == "ie":
                self.driver = webdriver.Ie()
            log.info(browserName.lower()+"启动浏览器成功")

        except:
                log.error('无' + browserName.lower() + '类型浏览器')
                raise NameError('请指定浏览器类型：chrome firefox ie')




    #跳转链接、窗口最大化
    def open(self, url, t='', timeout=10):
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(t))
            log.info("跳转链接"+url+"成功")
            log.info("跳转后的title为:"+self.driver.title)
        except :
            log.error("跳转链接"+url+"失败,请确认！")

            print("open %s title error" % url)


    """截图
       给截图命名,不命名默认为以时间戳命名
    """
    def take_picture(self, filename=''):
        try:
            localtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
            pic_path = cf.pic_path
            if filename =='':
                pic_name  = os.path.join(pic_path,localtime + '.png')
            else:
                pic_name = os.path.join(pic_path, filename + '.png')
            self.driver.get_screenshot_as_file(pic_name)
        except:
            log.error("截图失败")



    '''
    定位元素，参数locator是元组类型
        Usage:
        locator = ("id","xxx")
        driver.find_element(locator)
        loc_name 元素的别名,如"百度输入框"
        
        by_id= "id"
        by_xpath = "xpath"
        by_link_text = "link text"
        by_partial_text = "partial link text"
        by_name = "name"
        by_tag_name = "tag name"
        by_class_name = "class name"
        by_css_selector = "css selector"
    '''
    def find_element(self, locator,loc_name='',timeout=10):

        try:
            element = WebDriverWait(self.driver, timeout, 1). \
                until(EC.presence_of_element_located(locator))
            if loc_name == '':
                log.info("匿名元素定位成功")
            else:
                log.info("\""+loc_name+"\""+'定位成功')
            return element
        except:
            if loc_name == '':
               log.info("匿名元素定位失败")
            else:
                # log.error(str(10) + '秒内未等到元素'  + loc_name+'出现')
                log.error("10秒内未等到元素{}出现".format(loc_name))
                raise ElementError('元素定位错误')

    """鼠标悬停在某元素上"""

    def move_to_element(self, locator, ele_name=''):
        element = self.find_element(locator, ele_name)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)


    """
        说明:打开另一个浏览器窗口
        :param url: url地址
        :Usage:
        browser.open_win('http://www.xxx.com')
    """

    def open_window(self, url):
        js = 'window.open("' + url + '")'
        self.driver.execute_script(js)
        log.info('成功打开网址' + url)

    """
        说明:选择下拉框定位
        :param 
            locator，定位元素,如locator=("id","kw")
            eleName, 日志中元素别名,如"百度首页-输入框"
            type， 选值的类型,有index,value,text三种,如果type为空,则随机选取一个
        :Usage:
            base.select(locator_select,type="index",value=1,eleName="搜索网页格式") #按照index选择
            base.select(locator_select,type="text",value="微软 Word (.doc)",eleName="搜索网页格式") #按照text选择
            base.select(locator_select,type="value",value="xls",eleName="搜索网页格式") #按照value选择
            base.select(locator_select,eleName="搜索网页格式")#随机选择+元素取别名
            base.select(locator_select)#随机选择
    """
    def select(self,locator,eleName='',type='',value=''):

        ele = self.find_element(locator,eleName)
        if type == "text":
            Select(ele).select_by_visible_text(value)
        elif type == "value":
            Select(ele).select_by_value(value)
        elif type == "index":
            Select(ele).select_by_index(value)
        else:
            eles = Select(ele).options  #返回的是一个列表
            rand_num = random.randint(0,len(eles)-1)
            print('随机数为:'+ str(rand_num))
            Select(ele).select_by_index(rand_num)




    """
        说明:
        清除输入框内容
        Usage:
        base.clear(locator)
        :param locator,locator = ("id","kw")
               
     """
    def clear(self,locator):
        element =  self.find_element(locator)
        element.clear()

    """提交表单"""
    def submit(self,locator,loc_name=''):
        element = self.find_element(locator,loc_name)
        element.submit()




    """
        说明:
        随机点击元素数组中的一个元素
        Usage:
        clickRandomElement(eleList)
        :param eleList 元素组成的数组  
    """
    def find_elements(self, locator,eleNames='',timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
            if eleNames == '':
                return elements
            else:
                log.info(eleNames+"元素组定位成功")
                return elements
        except:
            if eleNames == '':
                log.error("匿名元素定位失败")
            else:
                log.error(eleNames+"元素组定位失败")

    '''
        说明:
        随机点击元素数组中的一个元素
        Usage:
        clickRandomElement(eleList)
        :param eleList 元素组成的数组         
    '''
    def clickRandomElement(self,eleList):
        try:
            randNum = random.randint(0,len(eleList)-1)
            eleList[randNum].click()
            log.info("点击随机元素成功")
        except:
            log.error("点击随机元素失败")


    """单击"""
    def click(self, locator,ele_name=''):
        element = self.find_element(locator,ele_name)
        element.click()
        if ele_name=='':
            log.info("点击匿名元素成功")
        else:
            log.info("点击"+"\""+ele_name+"\""+"成功")

    """输入框输入内容"""
    def send_keys(self, locator, text,loc_name=''):
        element = self.find_element(locator,loc_name)
        element.send_keys(text)



    '''返回true、false'''

    def is_text_in_element(self, locator, text, timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except TimeoutException:
            print("元素没定位到：" + str(locator))
            return False

    def is_title(self, title, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(
            EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(locator))
        return result

    def is_clickabke(self, locator, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return result



    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def get_title(self):
        return self.driver.title

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def get_attribute(self, locator, name):
        element = self.find_element(locator)
        return element.get_attribute(name)

    """执行js"""
    def js_excute(self,js):
        self.driver.execute_script(js)

    def js_focus_element(self, locator):
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def js_scroll_shuzi(self, shuzi):
        js = 'window.scrollTo(0,' + str(shuzi) + ')'
        self.driver.execute_script(js)


    def is_visibility_by_loc(self, locator):
        try:
            self.find_element_loc(locator)
            return True
        except:
            return False


if __name__ == '__main__':
   base = Base()
   driver = base.driver
   # driver.get(r"https://www.baidu.com")
































