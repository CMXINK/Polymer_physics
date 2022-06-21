为方便后来者修改此软件,本文件将会介绍我当时写此软件时的环境以供参考
请尽量保证与此文件所说的环境保持一致

1.  本程序使用Pycharm 2020.3.2 x64 编写
2.  本程序采取Python 3.7.9 x64 解释器
3.  本程序采用框架作为PyQt5 5.15.6 GUI框架进行编写(如果你略懂C++ 的qt框架,也可尝试修改)
4.  本程序所用的包已在requirements.txt文件中生成, 你可以使用pip进行一次性安装
5.  本程序采用Qtdesigner作为快速开发软件进行UI界面构建
6.  本程序采取phpstudy中的mysql数据库对数据管理控制, 数据库版本: Mysql 5.7.26
7.  本程序在参考前学长的制作成果独立构建,但某些布局参照了前人的程序,由于前软学长的程序并非使用pyqt完成,此软件仅参考了前软件的部分界面排版，无太大联系，关于前学长的软件,请与董薇老师联系
8.  本程序的qss样式尚未进行提取，分布于设计的模板或者在py文件中,学弟或学妹可进行修改单独写成一个qss文件
9.  本程序采取SQLAlchemy作为orm库进行数据库迁移同步
10. 本程序严格遵守MVC构建方法,请后者也严格遵守MVC方法, 如果结构有变, 请及时更新该文件以便后人修正



-----------------------------------------------------------------------------------
项目结构

Polymer_physics_21.11.14
       control --> 控制器
       exts --> 扩展文件
       models --> 模型  (数据库)
       views --> 视图
                images --> 图片
                ui --> 原Qtdesigner设计的ui界面 以及转成python的对应的文件
       start.py  -->启动文件
       settings.py  -->公共配置文件
       readme.txt --> 即该文件,用于说明

----------------------------------------------------------------------------------
以下介绍control包中各py文件中类对应的作用 (类名即为其对应的文件名首字母大写, 每个文件对应一个相应的界面, 而每个类对应相应的py文件)
    Configs --> 配置类
    Logon ---> 登录类
    Experiment_conditions --> 实验条件类
    Check_medicine --> 选择药品类
    Check_instrument ---> 选择仪器类
    formula_calculate_one --> 计算实验数据1
    formula_calculate_two --> 计算实验数据2
    Install_instrument --> 组装仪器类
    designe_instrument --> 设计实验
    Add_cyclohexane --> 滴加环己烷
    Get_medicine --> 抽取药剂(包括打开搅拌)
    Get_styrene  --> 抽取苯乙烯(抽取正丁基锂...)


-- 此软件已经完成打包并在dist文件夹下生成，请找到dist/start/start.exe 运行
---> 软件运行要求:
    win10及以上版本, 不支持win7
    整个start文件夹, 并非单独的start.exe 文件
    启动请点击start/start.exe 启动
    请不要随意将start文件夹下的文件改变位置或重命名, 以免发生找不到文件位置的错误


