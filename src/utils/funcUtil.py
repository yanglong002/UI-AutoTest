# coding:utf-8

import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
from src.utils.logUtil import *
from src.utils.baseUtil import *
import time
import unittest
from BeautifulReport import BeautifulReport
from tomorrow import threads
#实例化Log类对象
log = Log()

"""
  函数说明: 取出excel中数据
  :param:
          fileName excel文件的绝对路径
          sheetNname  excel取数据的当前页名称
 :Usage:
         fileName = os.path.join(cf.data_path, r'testData.xlsx') 
         sheetNname = 'testsheet'
         dic = get_excel_data(fileName, sheetNname)
         print(dic)
"""
def get_excel_data(fileName,sheetName):
    wb = xlrd.open_workbook(fileName)
    sheet = wb.sheet_by_name(sheetName)
    nrows = sheet.nrows
    ncols = sheet.ncols
    # dic_p = {}
    dic_c = {} #用于存放数据的字典
    for x in range(ncols):

        cell = str(sheet.cell(0, x).value).strip()
        if cell == 'CASEID':
            caseId = str(sheet.cell(0, x + 1).value).strip()
            for y in range(nrows):
                paraname = str(sheet.cell(y, x).value).strip()
                #日期 要特殊处理下
                if "日期" in paraname:
                    m = sheet.cell(y, x + 1).value
                    temp = datetime(*xldate_as_tuple(m, 0))
                    # temp格式为2017-05-01 00:00:00
                    paravalue = temp.strftime('%Y-%m-%d')  # 格式化时间
                else:
                    paravalue = str(sheet.cell(y, x + 1).value).strip()
                if paraname == '':
                    break
                if paravalue == '':
                    break
                dic_c[paraname] = paravalue
            # dic_p[caseId] = dic_c
    return dic_c

"""
  函数说明:取出某路径下所有的文件
  :param: 
         path  文件路径
         listFile 存放取出文件的列表  
 :Usage:
         dirName = r'D:\dir'
         list =  getAllFiles(fileName)      
"""
def getAllFiles(path,listFile = []):
    if os.path.isdir(path):
        list = os.listdir(path)
        # global listFile
        for file in list:
            fullPath = os.path.join(path, file)
            if os.path.isfile(fullPath):
                # print(fullPath)
                listFile.append(fullPath) #递归,对文件夹继续查询
            else:
                getAllFiles(fullPath)
        return listFile

"""等待x秒"""
def wait(seconds):
    time.sleep(seconds)

"""
    说明:
    无参的截图装饰器
    Usage:
    @pic_deco
    def test_login(self)
        pass
   
    :param base,base为Base类的实例对象       
"""
def pic_deco(fun):  # 装饰器

    def _pic_deco(self, *args, **kwargs):
        try:
            f = fun(self, *args, **kwargs)  # 中间保留传进来的函数
            return f
        except Exception:

            cls_name = self.__class__.__name__  # 取得当前类的名称
            # print(cls_name)
            fun_name = fun.__name__  # 取得当前方法的名称
            # print(fun_name)
            filename = cls_name + '_' + fun_name
            self.base.take_picture(filename)  # 此处调用截图函数
            log.error(filename+"案例执行失败，已截图")
            self.assertTrue(False,filename+"案例执行失败")
    return _pic_deco

"""
    说明:
    带参数的截图装饰器
    Usage:
    @pic(base)
    def test_login(self)
        pass
   
    :param base,base为Base类的实例对象       
"""
def pic(base):
    def pic_deco(fun):  # 装饰器

        def _pic_deco(self, *args, **kwargs):
            try:
                f = fun(self, *args, **kwargs)  # 中间保留传进来的函数
                return f
            except Exception:
                cls_name = self.__class__.__name__  # 取得当前类的名称
                # print(cls_name)
                fun_name = fun.__name__  # 取得当前方法的名称
                # print(fun_name)
                filename = cls_name + '_' + fun_name
                base.take_picture(filename)  # 此处调用截图函数
        return _pic_deco
    return pic_deco



# 获取路径

def add_case(case_path=cf.case_path, rule="test_math*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover

@threads(3)
def run():
    localtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_name = '自动化测试报告' + localtime
    cases = add_case()
    test_suit = unittest.TestSuite() #创建测试套件
    test_suit.addTest(cases)
    print(cases)
    result = BeautifulReport(test_suit)
    result.report(filename=report_name, description='测试deafult报告', log_path=cf.report_path)
    result.add_test_img()

"""
    说明:
    登录的封装
    Usage:
    base = Base()
    login(base)
    :param base,base为Base类的实例对象       
"""
def login(base,url,username,password):
    try:
        locator_username = ("xpath", "//input[@type='text' and @class='input-inner']")  # 账号输入框
        locator_password = ("xpath", "//input[@type='password' and @class='input-inner']")  # 密码输入框
        locator_vcode = ("xpath", "//input[@id='check']")  # 验证码
        locator_button = ("xpath", "//span[text()='登录']")#登录按钮
        base.open(url)
        base.send_keys(locator_username, username, "账号输入框")
        base.send_keys(locator_password,        password, "密码输入框")
        base.find_element(locator_vcode, "验证码输入框")
        time.sleep(10)
        base.click(locator_button, "登录按钮")
        log.info("登录成功")
    except:
        log.error("登录失败")



if __name__=="__main__":
    # fileName = os.path.join(cf.data_path, r'testData.xlsx')
    # sheetNname = 'testsheet'
    # dic = get_excel_data(fileName, sheetNname)
    # path = r'F:\test'
    # list = getAllFiles(path)
    # print(list)
    # print(dic)
    run()
