import os

"""
os.path.realpath    
即使当前模块被引用,依然得到的是被引用模块的路径

os.path.dirname(文件)  返回文件所在的目录
os.path.sep   文件分隔符
os.path.abspath()  返回文件的绝对路径
os.path.realpath()  返回文件的绝对路径
"""
#取当前文件所在目录,再往上退一级
projectPath = os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"..")
log_path = os.path.join(projectPath, r'log')
driver_path = os.path.join(projectPath, r'driver')
pic_path = os.path.join(projectPath, r'picture')
data_path = os.path.join(projectPath, r'data')
config_path = os.path.join(projectPath, r'config')
configini_path = os.path.join(config_path,r'config.ini')
case_path = os.path.join(projectPath,r'src\case')
report_path = os.path.join(projectPath,r'report')
if __name__ == "__main__":

    print(projectPath)
    print(log_path)
    print(driver_path)
    print(data_path)
    print(config_path)
    print(configini_path)
    print(case_path)
    print(report_path)
    print(projectPath1)


