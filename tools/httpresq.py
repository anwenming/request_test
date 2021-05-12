import requests
from tools.do_excel import Do_excle
from tools.do_mylog import My_Logger
my_loge=My_Logger()

class HttPRequest:

    def httprequest(self,url,data,method,cookie=None):
        try:
            if str(method).upper()=='GET':
                res=requests.get(url,data,cookies=cookie)
            elif str(method).upper()=='POST':
                res = requests.post(url,data,cookies=cookie)
            else:
                my_loge.info("请求方法有错误")
        except Exception as e:
            my_loge.error("请求报错了：{0}".format(e))
            raise e
        return res
if __name__ == '__main__':
    data_1 = Do_excle().get_information('../test_data/datathing.xlsx')
    print(data_1)
    ht=HttPRequest()
    for i in data_1:
        print(i)
        res=ht.httprequest(i['url'],eval(i['data_2']),i['method'])
        print(type(res.json()))
        print(type(i['sheet_name']),type(i['case_id']))
        Do_excle.write_information('../test_data/datathing.xlsx',i['sheet_name'],i['case_id'],str(res.json()),'789')

