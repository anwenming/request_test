import unittest
import HTMLTestRunner
from tools.project_path import *
from tools.Testcase import ApiTest



suite=unittest.TestSuite()
# suite.addTest(ApiTest('test_01_joke'))

loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(ApiTest))

suite.addTest(loader.loadTestsFromTestCase(ApiTest))


with open(test_report_path,'w+') as file:
    runner = HTMLTestRunner.HTMLTestRunner(file,verbosity=2,title='测试练习',description='单元测试报告')
    runner.run(suite)
    # file.write(runner.run(suite))





