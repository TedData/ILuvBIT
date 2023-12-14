#使用自己创建的模块，文件名字不能为数字
import 41#必须为同一目录下
a=' 3213'
print(41.bbb(a))
==============================
#调用当前目录下包内模块的方法
import 包名.文件名
包名.文件名.函数名()

在包内创建文件“__init__.py”
并写入
from . import 包内文件名

之后调用当前目录下包内模块的方式为
import 包名
包名.文件名.函数名()	
==============================
发布模块

与包同一级的目录下建立文件 setup.py
并写入
from distutils.core import setup
setup(name='压缩包的名字', bersion='1.0', description='描述', author='作者', py_modules=['包名.文件名', '包名.文件名'])

在与包同一级目录下用终端执行
python3 setup.py build#构建模块
在与包同一级目录下用终端执行
python3 setup.py sdist#生成压缩包
===============================
安装模块

找到模块的压缩包，并解压
用终端执行
tar -zxvf 压缩包的名字-1.0.tar.gz
进入解压后的文件夹，执行命令
python3 setup.py install
=================================
使用模块
import 包名
包名.文件名.函数名()