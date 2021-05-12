# import pymysql
# from tools.read_config import ReadConfig
# from tools import project_path
#
# cloc=eval(ReadConfig.get_config(project_path.test_confige_path,'DB','db_config'))
# print(cloc)
# res=pymysql.connect(**cloc)
# cursor=res.cursor()
# sql_1='select max(MobilePhone) from member where MobilePhone like"138%" '
# cursor.execute(sql_1)
# res_1=cursor.fetchall()
# print(res_1)
# cursor.close()
# res.close()
