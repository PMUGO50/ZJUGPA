# Readme

yyq26314@outlook.com

此程序根据 stuinfo.csv 中的信息登陆浙江大学 zdbk 爬取**本科生**成绩信息并自动计算均绩

## 程序文件

- 用到的库包括 selenium (3.141.0) 与 pandas (2.0.3)

- auto.py 是函数定义文件

- main.py 是主程序文件

## 数据文件

- label.png 是程序图标

- stuinfo.csv 是学号与密码信息
  
  在 stuinfo.csv 中，请将 stuid, 后的xxxxxxxxxx改为学号，将 password, 后的xxxxxxxx改为密码

- gpa_auto.csv 是爬取后的成绩信息

## 启动程序

向 stuinfo.csv 中键入学号密码信息后，点击 ZJUGPA.exe 并耐心等待，因校网和爬虫不是非常稳定，程序可能会报错退出，重复启动几次直到成功显示均绩即可

**请注意由于各专业的培养方案不同，部分国际化课程、通识课程等可能无法识别是否主修，可以考虑在源代码中加入其是否为主修的判断**

