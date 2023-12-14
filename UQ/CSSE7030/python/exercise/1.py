ls -l(详细)ah(单位) [?-?]
pwd
clear
cd
touch
more
gedit
mkdir
rmdir
rm  -r
ln
ln -s
cat >  >>
grep -niv '^?$' name
name --help
find ./ -name '1'
cp name name -r
mv
tar -c/xvf name.tar *
tar -zc/xvf name.tar.gz *
gzip name.tar
gzip -d name.tar.gz
zip name *
unzip -d ./ name.zip
ifconfig | more
ssh 用户名@ip地址
who
useradd name -m -d /home/name
出现Permission denied，需要sudo + 命令
passwd name
su (-)(s) name
userdel (-r) name
cat /etc/group      groupmod +Tab Tab Tab
groupadd name
groupdel name
groupmod -g 组 用户名  （g为主组）
groups 用户名
usermod -a -G 组 用户名  （G为副组）
sudo usermod -a -G adm 用户名
sudo usermod -a -G sudo 用户名
r - read --------->4
w - write--------->2
x - execute------->1
- - 无
u - user
g - group
o - other
a - all
d(文件夹)rwx(user)rwx(group)r--(other)
chmod 用户+/-/=命令 name -R(修改文件夹里面所有文件的权限)
chmod 752 name == rwxr-x-w-
chown 用户名 name
chgrp 组 name
cal
date MMDDhhmmYYYY.ss
ps -aux
top
kill
reboot  重启
shutdown -h now/20:25/+10(分钟)
init 0  关机
init 6  重启
df
du                          O
vi      切换编辑模式   I    i | a     A
 	 	切换命令模式  exc     o
         退出 Shift+zz  :wq/x 保存退出   :q! 不保存退出
Ctrl + n  快速补全
j-->下   k-->上  l-->右  h-->左
行数 yy 复制 
行数 dd 剪切
q  粘贴
u  撤回
Ctrl + r 反撤销
行数 dd 删除
G 到最后一行
数字+G  到某一行
gg  到第1行
{  按段上移
}  按段下移
Ctrl+d  向下翻半屏
Ctrl+u  向上翻半屏
Ctrl+f  向下翻一屏
Ctrl+d  向上翻一屏
x-->Del
X-->Backspace
.  重复上一个命令
r  替换
v  上下移动可选定行数
/+内容   =搜索内容   n  下一个
:%s/abc/123/g   将所有的abc替换成123
:1,10s/abc/123/g   将第1行至第10行之间的abc替换成123
:w  保存
:wq  :x  Shift+zz  保存退出
:q!  不保存退出
FTp--File Transfer Protocol
安装文件   sudo apt-get install 文件名
#注释
'''注释'''
Numbers-----------数字
int---------------有符号整型
long--------------长整型
float-------------浮点型
complex-----------复数
String------------字符串
List--------------列表
Tuple-------------元祖
Dictionary--------字典
Set---------------集合
查找关键字   ipython3---->import keyword---->keyword.kwlist
输出   print('\n换行+\tTab'+str(变量),end='')
print("My name is %s, I am %s"%(name,age))
python3-------->name = input('')  提取数据
int(num)------->将变量变为整数
if :
elif :
else :
提取随机整数  import random    a = random.randint(0,2)
while :
	break
	continue
len(name)---->取name字符串长度
name[0:-1:1]
name.find('')
name.rfind(' ')------>查找内容在第几位
name.count('a',3,23)---->查找个数
name.replace("a","A")---->替换
name.split('')------>切割
name.startswith("A")------>是否以A开始
name.endswith("b")-------->是否以b结尾
name.lower()------------->全变小写
for str in name:
	print(str)
name.append( )------->末尾添加
name.insert(0, )----->第0位添加
name[0]=' '---------->更改第0位
del name[0]---------->删除第0位
name.pop()----------->删除最后一位
name.remove(' ')------>移除某一位
name.index(' ')-------->查看在第几位
name.sort()------------>从小到大排序
元组(Tuple)  name()====()里的内容跟[]list 一样
字典(dict)   name{1:"a","c":2} （1和"c"为不可变类型）
name.get()	显示要求的数据
name.clear
name.keys()
name.values()
name.items()
name[' ']=' '
集合--set====(没有先后顺序，没有下标位，内容不可重复，可以修改)
name={}
name.add()---添加
name.pop()---删除第一位
name.remove(' ')---删除' '内容


del name[' ']
定义函数   def 函数名():
			函数代码
返回值		return ' '/ /( )/[ ]/{ }

调用函数   函数名()

全局变量在def里不能修改，非要改：global name
不定长参数   def test(a,b,*args,**kwargs)
			   			()     {}
id()  内存地址
可变内存地址数据类型：list dict
不可内存地址变类型： int str tuple
a=a+a----> a的内存地址被更改
a+=a-----> a的内存地址不变====>如果a为可变内存地址数据类型，可更改函数外的a的数据
import time ========   time.sleep(1) ------->延迟1秒
匿名函数   lambda a,b:a+b		相当于：  def test(a,b):
调用  name= lambda a,b:a+b		  	return a+b
      print (name(3,4))			  print(test(3))

在函数里更改全局变量：global name

list里dict排序：	a=[{'a':1, 'b':11},{'a':12, 'b':21},{'a':11, 'b':43}]
		  		a.sort(key=lambda x:x['b'])
打开文件		f=open('test.txt','w/r/a')
			r---->只读方式打开，可以不写
 			w---->如果没有以创建的方式打开写入；如果有，以覆盖的方式打开写入
			a---->如果没有，创建；如果有，在末尾写入
关闭文件		f.close()
			f.read()--------->只读一次
		f.readlines()---->只读显示换行
		f.readline()----->只读显示一行
	    str.splitlines()---->换行
	    f.write('内容')
	    f.tell()------------>获取当前位（int）
        f.seek(数字,0/1/2)---->数字为移动几位；0为文件头，1为文件当前位置，2为文件尾
import os ====> os.remove('name')----->删除文件
 	  ====> os.rename('name','newName')---->文件重命名
	  ====> os.listdir('./') ----------->获取当前目录所有文件名字
	  ====> os.chdir('./文件夹')---->修改路径
	  ====> os.mkdir('name')------->创建文件夹
	  ====> os.rmdir('name')------->删除文件夹

name=input('what is your name?')
print('hello\n'+name+'! Have a nice day.')

print('hello\n',name+'! Have a nice day.')

#'+'无缝连接，','相当于' '
print('hello',name,sep='')#将连接处设为''
print('hello {0}! Have a nice day.'.format(name))
x=y=123,#x=123,y=123
a,b,c=4,5,6#a=4,b=5,c=6
	a,b=1,2
	a,b=b,a
	print(a,b)
round(3.14)=3
round(3.64)=4
round(-3.14)=-3
round(-3.64)=-4

a = 'I\'m a teacher'
b = 'my name is "gaoqi"'

print('aa',end='\n')
a=a.replace('c',"nihao")

import time
time1=time.time()#以秒为单位当前时间

a = 'to be or not to be'
a.split()
['to','be','or','not','to','be']
a.split('be')
['to',' or not to ','']
a=['sxt','sxt100','sxt200']
'*'.join(a)
'sxt*sxt100*sxt200'

a='abcdefghijklmnopqrstuvwxyz'
len(a)#长度
a.find('h')#找h的位置，正向搜索
a.rfind('h')#找h的位置，反向搜索
a.count('x')#x出现过几次
	'  s x t  '.strip()#去除首尾空白符
	's x t'
	'*s*x*t*'.strip('x')#去首尾除*
	's*x*t'
	a='name:{0},age is {1}'
	a.format('gaoqi',18)
	b='name:{name},age is {age}'
	b.format(age=18, name='gaoqi')
	c='name:{0},age is {1:!^8}'
	c.format('gaoqi',18)
	'name:gaoqi,age is !!!18!!!'
import io
s = 'Hello, sxt'
sio = io.StringIO(s)
	sio.getvalue()
	'Hello, sxt'
sio.seek(7)
7
sio.write('gfhx')
4
sio.getvalue()
'Hello, gfhx'


x=[1,2,3]
y=['a','b','c']
y.append('d')
y=['a','b','c','d']
y.extend(x) 相当于 y += iterable(x)
y=['a', 'b', 'c', 'd', 1, 2, 3]
y.insert(4,'e')
y=['a', 'b', 'c', 'd', 'e', 1, 2, 3]
y.remove(1)
y=['a', 'b', 'c', 'd', 'e', 2, 3]
y.remove(y[5])
['a', 'b', 'c', 'd', 'e', 3]
y.pop()=3
y=['a', 'b', 'c', 'd', 'e']
del y[4]
y=['a', 'b', 'c', 'd']
y.index('d') = 3
y.sort()#排序
重要的
i=[1,2,3]
j=i	#此时，i,j若更改一个，另一个也会被更改
j=i[:] #这样i,j会分开，互不影响
max(x)
min(x)
sum(x)


a = [x * 2 for x in range(5)]
a = [0,2,4,6,8]
a = [x * 2 for x in range(10) if x % 3 == 0]
a = [0,6,12,18]

tuple
a=(10,20,30)
a+=(40,)
a=tuple('abc')
a=tuple(range(3))
a=tuple([2,3,4])
del a

dict#
key:#int,str,tuple,float
d = {'name':'gaoqi','age':18}
d = dict(name='gaoqi',age=18)
d = [('name','gaoqi'),('age',18)]
	k=['name','age']
	v=['gaoqi',18]
	d=dict(zip(k,v))

a.get('name')='gaoqi'
a.get('sex','bucunzai')
a.keys()
a.values()
a.items()
del(d['name'])
b = d.pop('name')#删除name，把值赋给b

with open(文件名) as fd:
	code
	#不用写fd.close()

class aaa(object):
	def __init__(self):
		pass
	def __repr__(self):
		return 123

b=aaa()#b的值为123


