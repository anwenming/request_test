import os


# 文件当前路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# excel文件路径
test_path=os.path.join(project_path,'test_data','datathing.xlsx')


# 日志路径
test_report_path=os.path.join(project_path,'reslogging','test_api.html')


# 配置文件
test_confige_path=os.path.join(project_path,'test_data','config')
# print(test_confige_path)
# case_config_path=os.path.join(project_path,'test')