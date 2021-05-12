import unittest
from tools.httpresq import HttPRequest
from tools.do_excel import Do_excle
from ddt import ddt,data
from tools.project_path import *
from tools.do_mylog import My_Logger
my_loge=My_Logger()
# 从文件中拿到数据



data_1=Do_excle.get_information(test_path)

# print(data_1)

@ddt
class ApiTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    @data(*data_1)
    def test_01_joke(self,item):
        res = HttPRequest().httprequest(item['url'],eval(item['data_2']),item['method'])
        try:
            self.assertEqual(str(item['res']),res.json()['resultcode'])
            TestResult='Pass'
        except Exception as e:
            TestResult='False'
            raise e
        finally:
            Do_excle.write_information(test_path,item['sheet_name'],item['case_id'],str(res.json()),TestResult)
            my_loge.info("获取到的结果是{}".format(res.json()))






