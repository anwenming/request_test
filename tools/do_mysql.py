import pymysql
from tools.read_config import ReadConfig
from tools import project_path

class Do_Mysql:


    def do_mysql(self,query,states='all'):
        db_config=eval(ReadConfig().get_config(project_path.test_confige_path,'DB','db_config'))
        cnn=pymysql.connect(**db_config)
        # 游标
        cursor=cnn.cursor()
        # query_sql='select max(MobilePhone) from member where MobilePhone like"138%"'
        cursor.execute(query)
        if states=='all':
            res = cursor.fetchone()
        else:
            res=cursor.fetchall()
        cursor.close()
        cnn.close()
        return res

if __name__ == '__main__':
    query_sql = 'select max(MobilePhone) from member where MobilePhone like"156%"'
    res=Do_Mysql().do_mysql(query_sql)
    print(res)