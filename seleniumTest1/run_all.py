import unittest
from common import htmlTestRunner_cn
casePath="F:\pythonDemo\seleniumTest1\\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)
reportPath="F:\pythonDemo\seleniumTest1\\report\\"+"report.html"
fp=open(reportPath,"wb")#二进制方式写入
runCaseReport=htmlTestRunner_cn.HTMLTestRunner(stream=fp,title="测试报告",description="输出用例执行结果",retry=3)
runCaseReport.run(discover)
fp.close()