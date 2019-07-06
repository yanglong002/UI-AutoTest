import configparser
from src.utils.logUtil import *

log = Log()
class ConfigAction():

    #初始化对象,并把内容加载到对象所在内存
    def __init__(self):
        self.fileName = cf.configini_path
        self.cfg = configparser.ConfigParser()
        self.cfg.read(self.fileName) #内容加载到对象所在内存


    #取得所有的section
    def get_sections(self):
        return self.cfg.sections()


    #取得某section下的某option的值
    def get_option(self,section,option):
        return eval(self.cfg.get(section,option))


    #添加一个section
    def add_section(self,section):
        if section in self.get_sections():
            log.info(section+"已经存在")
        else:
            self.cfg.add_section(section)

    #删除一个section
    def del_section(self,section):
        if section in self.get_sections():
            self.cfg.remove_section(section)
        else:
            log.info("section"+section+"不存在")

    #删除option
    def del_option(self,section,option):
        try:
            self.cfg.remove_option(section,option)
        except:
            log.error("删除option:"+option+"异常")

    #在某个section下增加一个option
    def add_option(self,section,option,value=''):
        try:
            self.cfg.set(section,option,value)
            log.info("section:"+section+"下添加option:"+option+"成功")
        except:
            if section not in self.cfg.sections():
                log.error("section:"+section+"不存在")
            else:
                pass

    #保存修改后的configini文件
    def save(self):
        fd = open(self.fileName,'w')
        self.cfg.write(fd)
        fd.close()

if __name__=="__main__":
    import config.configInfo as cf
    c = ConfigAction()
    username = c.get_option('STG','username')
    password = c.get_option('STG','password')
    print(username)
    print(password)
