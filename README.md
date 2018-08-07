文件夹简介：
1、bin—>run.py：主函数，运行用例，生成报告发送邮件
2、conf—>path.py：测试用例、日志、报告等所有存放路径配置
3、conf—>setting.py：环境配置，如：邮件、日志、数据库等配置
4、lib—>page—>page.py：各个case的具体实现
5、lib：框架的基本工具
   lib—>log.py：管理日志
   lib—>pyse.py：UI基本操作方法的二次封装，如：单击、双击、捕捉元素、显式等待。。。
   lib—>tool.py：通用工能方法，如图片处理
   lib—>HTMLTestRunner.py：测试报告
   lib—>send_mail.py：发送测试报告邮件
6、log—>test.log：输出的日志
7、page—>page.py：操作页面，对于每个测试页面及页面元素的处理
8、report—>test_report.html：生成的测试报告，可在浏览器中查看
9、report—>picture—>error.jpg：报错页面截图
10、test_case—>xxx.py：组织测试用例

            
需要下载的东西：
1、python
2、python运行环境，如pyCharm



写 case 时，根据自己的需求补充对应的文件：
1、conf—>setting.py：根据自己的修改相关配置
2、page—>pyge.py：根据需求添加要测试的页面及功能方法
3、test_case—>：根据需求组织用例
4、元素定位时，按格式书写：'方法=>'


运行用例
1、运行：bin—>run.py

