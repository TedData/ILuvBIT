DB=数据库(BataBase)
DBMS=数据管理系统(DataBase Management System)
SQL=sequel

进入MySQL：mysql -u root -pgfeeq8023@
密码：gfeeq8023@
如果密码不对
1:进入终端输入  cd /usr/local/mysql/bin/
2:回车后 登录管理员权限  sudo su
3:输入密码:gfeeq8023@
4:回车后输入以下命令来禁止mysql验证功能
  ./mysqld_safe --skip-grant-tables &
5:输入命令  ./mysql

概念：
表(table)包括行(字段名称·字段数据类型·字段约束·字段长度)、列(字段Column)、主键


sql的分类
	数据查询语言(DQL-Data Query Language)
		代表关键词：select
	数据操纵语言(DML-Data Manipulation Language)针对table数据
		代表关键词：insert，delete，update
	数据定义语言(DDL-Data Definition Language)针对table结构
		代表关键词：create，drop，alter
	事务控制语言(TCL-Transactional Control Language)
		代表关键词：commit，rollback
	数据控制语言(DCL-Data Control Language)
		代表关键词：grant，revoke


mysql常见命令
1:show databases;  #必须以‘;’结尾 
2:use 库名;   #进入文件
3:show tables;	#显示文件里面的表
4:show tables from mysql;	#显示其他库(mysql)下的表
5:select database();	#显示当前在哪个库里
6:create table 表名(
	id int,
	name varchar(20));	#创建一个表，一个类为id，类型为int，一个类为name，类型为字符串
7:desc 表名;		#查看表的结构
8:select * from 表名;	#查看表里的数据
9:insert into 表名 (id,name) values(1,'john');	#增加信息
10:update 表名 set name='lily' where id=1;	#修改信息
11:delete from 表名 where id=1;	#删除信息
12:select version();	#查看MySQL版本
13:create database 库名;	#创建一个数据库
14:Ctrl+C	#退出mysql
15:\c	#结束语句
16:show create table 表名;	#查看表的创建语句
17:drop database 库名;	#删除数据库
18:drop table if exists 库名	#如果存在删除，不存在不报错
19:source 路径	#可导入.sql文件的数据
20:create index 索引名字 on 表名(字段名称);	#建立索引


mysql的语法规范
	1.不区分大小写，但建议关键字大写，表名、列名小写
	2.每条命令用分号（;）结尾
	3.每条命令根据需要，可以进行缩进或换行
	4.注释。 单行注释：#注释文字
			多行注释：/*注释文字*/
	5.字符串用''括起来

mysql数据库中的数据类型:
	int			整数型
	varchar 	字符串(可变长度)
	char		定长字符串
	date 		日期类型
	double		浮点型


查询语句(DQL)
	select ename(字段名称) from emp(表名);
	多段查询 (,隔开)
		select empno, ename from emp;
	字段上可以写出数学表达式
		select enpno,ename,sal*12 from emp;
	查询修改显示字段名(不更改原始数据)
		select empno,ename,sal*12 as(可以省略) year_sal from emp;
	条件查询
		select
		empno,ename,sal
		from
		emp
		where
		sal=5000;
	between and 如果是int，左右结为闭合
		select empno,ename,sal from emp where sal between 3000 and 5000;
	between and 如果是carchar,左闭右开
		select ename from emp where ename between 'a' and 'k';
	and 优先级高于 or
		select ename,job from emp where job='salesman' or job='manager';
		select ename,sal,deptno from emp where sal>1800 and (deptno=20 or deptno=30);
	in ('','')不是区间，就是值
		select ename,job from emp where job in ('manager','salesman');
		select ename,sal from emp where sal in (1500,5000);
	like 模糊查询 %(代表任意长度字符) _(代表任意1个字符)
		select ename from emp where ename like '%C%';
		select ename from emp where ename like 'S%';
		select ename from emp where ename like '__A%';
	order by 排序 asc 默认(升序) desc(降序)
		select ename,sal from emp order by sal;
		select
			ename,sal
		from
			emp
		order by
			sal desc,ename;
		相当于：select ename,sal from emp order by 2 desc,1;
	
	常用条件
		=
		>	>=
		<	<=
		<>	!=
		between (小值) and (大值)	>= and <= 
		is null  (空)
		and 
		or 
		in
		not
		like

	数据处理函数/单行处理函数
		lower	转换小写
			select lower(ename) ename from emp;
		upper	转换大写
		substr	截取长度，(substr(被截取的字符串,起始下标,截取的长度))
			select substr(ename,2,3) from emp;
			select ename from emp where substr(ename,2,1)='a';
			select ename from emp where ename like '_a%';
		length	取长度
		trim	去空格
		round	四舍五入(round(数字,保留小数点后几位))
			select round(153.46,-2)
		rand()	生成随机数
		ifnull	将null转换成一个具体值
			select ename,ifnull(comm,0) from emp;
			null参加任何运算结果都为null(0)
	
	分组函数/多行处理函数	(自动忽略null)
		count	取得记录数
		sum		求和
		avg		取平均
		max		取最大值
		min 	取最小值
		分组函数不能直接使用在where语句中
		分组函数必须在分组完成后执行，而分组需要group by，而group by在where后执行
	MYSQL中的日期处理
		1.每一个数据库处理日期的时候，采用的机制是不同的，日期处理都有自己的一套机制。
			所以在实际的开发中，表中的字段定义为DATE类型，这种情况很少。
			因为一旦使用日期类型，那么java程序将不能够通用。在实际开发中，一般会使用
			‘日期字符串’来表示日期。
		2.日期是数据库本身的特色，也是数据库本身机制中的一个重要内容，所以还是需要掌握
	MYSQL数据库管理系统中对日期的处理提供了两个重要的函数
		1.str_to_date
		2.date_format
	str_to_date
		1.该函数的作用是：将‘日期字符串’转换成‘日期类型’数据。(varchar-date)
		2.该函数的执行结果是DATE类型
		3.该函数的使用格式:str_to_date('日期字符串','日期格式')
		4.mysql中的日期格式:(区分大小写)
			%Y 		年	
			%m 		月
			%d 		日
			%H		时
			%i 		分
			$s 		秒
		5.查询出1980-12-17入职的员工
			select ename,hiredate from emp where hiredate='1980-12-17';
				mysql默认的日期格式:%Y-%m-%d,以上的日期字符串若与默认日期格式一致，自动将日期字符串转换成了日期类型
			正确语句
			select ename,hiredate from emp where hiredate=str_to_date('17/12/1980','%d/%m/%Y');
	date_format
		1.该函数的作用是:将日期类型date转换成具有特定格式的日期字符串(date-varchar)
		2.该函数的运作结果是:varchar
		3.该函数的语法格式:date_format(日期类型数据,'日期格式');
		4.查询员工的入职日期，并以21/05/1990的格式显示
			select ename,date_format(hiredate,'%d/%m/%Y') from emp;
	去重查询 distinct 
		select distinct job from emp;
		必须在字段名称的最前面,将后面的字段名称看成一个整体
		select distinct deptno,job from emp;
		统计一共有多少个工作岗位
		select count(distinct job) from emp;
	分组查询:
		1.group by
			案例:每个岗位的最高薪水
				select job,max(sal) from emp group by job;
			语句中若有group by，那么select关键字后面只能跟参与分组的字段和分组函数。

			以下语句毫无意义，分组数据跟分组函数不能与其他数据不匹配，ename与job,sal数据不匹配
				select ename,job,max(sal) from emp group by job;
			案例:每个部门的平均薪水
				select round(avg(sal),-1),deptno from emp group by deptno;
			案例:计算不同部门不同工作岗位的最大薪水
				select deptno,job,max(sal) from emp group by deptno,job;
				select deptno,job,max(sal) from emp group by 2,1;
			group by 后面的字段看成一个整体
			案例:除manager以外，各工作岗位的最高薪水
				select job,max(sal) from emp where job !='manager' group by job order by sal;
			
		2.having
			having和where功能相同，都是为了完成数据的过滤。
				where和having后面都是添加条件
				where在group by之前完成过滤
				having在group by之后完成过滤
			案例:显示平均薪水大于1500的每个工作岗位的平均薪水
				select job,avg(sal) from emp group by job having avg(sal)>1500 order by 2;
			原则:尽量在where中过滤，无法过滤的数据，通常都是需要先分组之后再过略的，这个时候可以选砸使用having。效率问题。
	一个完整的DQL语句总结
		select
			...
		from
			...
		where
			...
		group by
			...
		having
			...
		order by
			...
		
		以上的关键字顺序不能变
		
		执行顺序：
			1:from ... 		从某张表中检索数据
			2:where ... 	经过某条件进行过滤
			3:group by ... 	然后分组
			4:having ... 	分组之后不满意再过滤
			5:select ...	查询出来
			6:order by ... 	排序输出

	连接查询
		- 查询的时候只从一张表检索数据，被称为单表查询
		- 在实际的开发中，数据并不是存储在一张表中的，是同时存储在多张表中
			这些表和表之间存在关系，我们在检索的时候通常是需要将多张表联合起来取得有效数据
			这种多表查询被称为连接查询或者叫做跨表查询
		
		连接查询分类
			- SQL92
			- SQL99
			DBA:DataBase Administrator
		
		连接查询根据连接方式可以分为:
			- 内连接==A表和B表能够完全匹配的记录查询出来
				* 等值连接
				* 非等值连接
				* 自连接
			- 外连接==A表和B表能够完全匹配的记录查询出来之外，将其中一张表的记录无条件的完全查询出来，对方表没有匹配的记录，会自动模拟出NULL
				* 左外连接
				* 右外连接
			- 全连接
		- 若两张表进行连接查询的时候没有任何条件限制，最终的查询结果总数是两张表记录条数成绩
			这种现象被称为笛卡尔积现象
		- 在连接查询的时候虽然使用了限制条件，但是匹配的次数没有减少，，只不过这一次的结果都是有效记录。
		案例:显示每一个员工对应的部门名称
		SQL92语法，内连接中的等值连接
			select e.ename,d.dname from emp e,dept d where e.deptno=d.deptno;
		SQL99语法，内连接中的等值连接
			select e.ename,d.dname from emp e inner join dept d on e.deptno=d.deptno; #inner可以省略
			99语法优点，表连接独立，结构清晰。
				from后直接加表连接操作，若有条件查询可直接加where
		案例:找出每一个员工对应的工资等级，要求显示员工名，工资，工资等级
		SQL99语法，内连接中的非等值连接
			select e.ename,e.sal,s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal;
		案例:找出每一个员工的上级领导，要求显示员工名以及对应的领导
		SQL99语法，内连接中的自连接
			select a.ename,b.ename from emp a join emp b on a.mgr=b.empno;
		案例:找出每一个员工对应的部门名称，要求部门名称全部显示
		SQL99语法，外连接中的右外连接
			select a.ename,b.dname from emp a right outer join dept b on a.deptno=b.deptno order by a.empno;#outer可以省略
		左连接
			select e.ename,d.dname from dept d left join emp e on e.deptno=d.deptno;
		案例:找出每一个员工对应的领导名，要求显示所有的员工
			select a.ename empname,b.ename leadername from emp a left join emp b on a.mgr=b.empno;
		案例:找出每一个员工对应的部门名称，以及该员工对应的工资等级
			select e.ename,d.dname,s.grade from emp e join dept d on e.deptno=d.deptno join salgrade s on e.sal between s.losal and s.hisal;
				select
					xxx
				from
					a
				join
					b
				on
					a与b的条件
				join
					c		
				on
					a与c的条件
				;

	子查询-select语句嵌套select语句
		where .. (select ..)
		from .. (select ..)
		select .. (select ..)
		案例:找出比公司平均薪水高的员工，要求显示员工名和薪水
			select ename,sal from emp where sal>(select avg(sal) from emp);
		案例:找出每一个部门的平均薪水，及薪水等级
			select e.*,s.grade from (select deptno,round(avg(sal)) avgsal from emp group by deptno) e join salgrade s on e.avgsal between s.losal and s.hisal;
				avg在SQL语句中有特殊含义，不能直接用，要重命名
	union 将两个结果合并,要求字段个数必须一致	
		select ename, job from emp where job='manager'
		union 
		select ename ,job from emp where job='salesman'
		;
		select ename enamedname from emp union select dname from dept;

	limit-用来获取一张表中的某部分数据
			只有在mysql数据库中存在，不通用，是mysql数据管理系统的特色
		案例:找出员工表中前5条记录
			select * from emp limit 0,5;#起始下标可以省略，5为长度
			select * from emp limit 5;
		案例:找出公司中工资排名在前5名的员工
			select ename,sal from emp order by sal desc limit 5;
		案例:找出工资排名在3-9名的员工
			select * from emp order by sal desc limit 2,7;
		mysql中通用的分页sql语句
			每页显示pageSize条记录
				第pageNo页: limit (pageNo-1)*pageSize,pageSize

表-table
	表格table，用来存储数据，表格式一种结构化文件
	表格行被称为记录(表中的数据)，表格列被称为字段
	表格的字段属性包括:字段名称、字段数据类型、字段长度、字段约束
	创建表
		create table tableName(
			字段名称 数据类型(长度),
			columnName dataType(length)
		);
	mysql数据库中的数据类型
		-varchar 	可变长度字符串
		-char		定长字符串
		-int 		整数型
		-bigint 	长整型
		-float		浮点型单精度
		-double 	浮点型双精度
			double(7,2)		表示7个有效数字，2个小数位
		-date 		日期类型
			日期类型一般不使用，采用字符串代替日期
		-blob		binary large object		二进制大对象
			专门存储图片，声音，图像等数据
		-clob		character large object	字符大对象
			可以存储比较大的文本，超大字符串可以储存
		-其他
	建表语句
		create table t_student(
				no int(10),			int-长度可不写
				name varchar(32),	varchar-必须写长度
				sex char(1),
				birth date,			月日0可以不用写
				email varchar(128)
			);
	删除表格
		drop table if exists t_student;	#如果存在就删除，不存在不报错，但只用于mysql语句
	插入数据-insert 
		DML语句包括- insert, update, delete
		句法格式	
			insert into tableName(columnName1, columnName2, ...) values(value1, value2, ...);
				字段和值必须一一对应，个数必须相同，数据类型必须一致，顺序可以调整
		insert into t_student(no,name,sex,birth,email) values(1,'zhangsan','m','1990-05-21','peng.yu1@uqconnect.edu.au');

		insert into t_student(no,name) values (3,'wangwu');
			默认情况下：当一张表被创建之后，没有指定约束的话，可以为null，
			并且没有任何默认值的话，默认值就是null，这里的默认值null表示：
			若插入数据的时候没有给该字段制定任何数据，默认插入null值。
		insert into t_student values(5,'lily','F','1995-3-5','331047908@163.com');
			insert 语句可以省略字段名字，但要将表中所有的字段都要写上
			省略之后程序不健壮，无法修改表结构，可能导致insert语句执行失败
	创建表时添加默认值
		create table t_student(
			no int(10),
			name varchar(32),
			sex char(1) default 'm'
			);
			默认值为'm'

		获取当前时间- select now();
		create table t_organizaton(
			code char(10),
			name varchar(32),
			createTime date
			);
		insert into 
			t_organizaton (code,name,createTime) 
		values 
			('111','athor',now());
	复制一张表
		create table emp1 as select * from emp;
	将查询结果当做一张表创建
		create table emp2 select empno,ename,sal from emp;
	将查询结果插入到某张表中
		insert into emp2 select * from emp2 where sal=3000;

增/删/改 表的结构[DDL语句]
	增
		alter table t_student add tel varchar(10);
	改	
		alter table t_student modify tel varchar(20) unique;
	删
		alter table t_student drop tel;

增/删/改 表的数据[DL语句]
	增
		insert into tableName (字段名称) values (字段值)；
	改-	update语句格式
		update tableName set 字段名=字段值,字段名=字段值 where 条件;
			注意:update语句若无条件限制，会将表中所有数据全部更新
		名字中含有o的员工名修改为lisi
		update emp_bak set ename='lisi' where ename like '%o%';
		工作岗位是manager和salesman的员工工资上涨10%
		update emp_bak set sal=sal*1.1 where  job in ('manager','salesman');

	删- delete语句格式
		delete from tableName where 条件;
			注意:若没有限制，会将这张表中所有的记录全部删除
		delete from t_student where no=4;
		将20部门中的manager删除
			delete from emp_bak where deptno=20 and job='manager';


约束(constraint)
	- 非空约束(not null)
	- 唯一约束(unique)
	- 主键约束(primary key)-pk
	- 外键约束(foreign key)-fk
	- 检查约束(mysql不支持，oracle支持)
		
	非空约束(not null)
		create table t_student(
			no int,
			name varchar(32) not null,
			sex char(1) 
			);

	唯一约束(unique)==字段值不可重复,null不算重复
		create table t_user(
			id int, 
			name varchar(32), 
			email varchar(64) unique
			); #列级约束

		create table t_user(
			id int, 
			name varchar(32), 
			email varchar(64), 
			unique(email)
			); #表级约束
		
		create table t_user(
			id int, 
			name varchar(32), 
			email varchar(64), 
			unique(name,email)
			);#表示name与email两个字段联合唯一

	表级约束可以改约束名字
		create table t_user(
			id int,
			name varchar(32),
			email varchar(64),
			constraint t_user_email unique(email)
			);

	查询约束的名字
		use information_schema;
		desc table_constraints;
		select * from table_constraints where table_name='t_user';

	主键约束(primary key)-pk
		-主键约束
		-主键字段
		-主键值
			表中的某个字段添加主键约束之后，
			该字段被称为主键字段，主键字段中
			出现的每一个数据都被称为主键值。
			==============================
			给某个字段添加主键约束之后primary key之后，
			该字段不能重复，并且不能为空。效果和‘not null 
			unique’约束相同，主键约束除了可以做到‘not null
			unique’之外，主键字段还会默认添加‘索引-index’
			==============================
			一张表应该有主键字段，若没有，表示这张表是无效的。
			‘主键值’是当前行数据的唯一标识。
			==============================
			给一个字段添加主键约束，被称为单一主键。
			给多个字段联合添加一个主键约束，被称为复合主键。
			无论是单一主键还是复合主键，一张表主键约束只能有一个。

		-自然主键
			* 主键值若是一个自然数，这个自然数和当前表的业务
				没有任何关系，这种主键叫做自然主键。
		-业务主键
			* 主键值若和当前业务紧密相关的，那么这种主键值被称为
				业务主键，当业务数据发生改变的时候，主键值通常会受到影响。

		单一主键
			create table t_user(
				id int primary key,
				name varchar(32)
				);

		复合主键
			create table t_user(
				id int,
				name varchar(32),
				email varchar(128),
				primary key(id,name)
				);

		在mysql数据库管理系统中提供了一个自增的数字，专门用来自动生成主键值。
			主键值不需要用户维护，也不需要用户提供了，自动生成的。这个自增的数字
			默认从1开始，以1递增:1,2,3,4,5,6......
				
				create table t_user(
					id int primary key auto_increment,
					name varchar(32)
					);
			输入数据时不用在添加id内容
			删掉之后不会重复使用

	外键约束(foreign key)-fk
		-外键约束
		-外键字段
		-外键值
			某个字段添加外键约束之后，该字段称为外键字段，
			外键字段中的每一个数据都是外键值。
			============================
			一个表中可以有多个外键字段
			外键值可以为null
			外键被引用的字段必须具有唯一性
			外键约束没有列级约束，只有表级约束
			============================
			被引用的表为父表，外键的表为子表
			先创建父表，再创建子表
			先向父表中插入数据，再向子表中插入数据
			先删除子表中的数据，再删除父表中的数据
			============================
			单一外键-给单一字段添加一个外键约束
			复合外键-给多个字段添加一个外键约束
			============================
			一对多的设计，在多的一方加外键。


		create table t_class(
			cno int primary key,
			cname varchar(128) not null unique
			);
		create table t_student(
			sno int primary key auto_increment,
			sname varchar(32) not null,
			classno int,
			constraint t_student_classno_fk foreign key(classno) references t_class(cno)
			);
			#给约束起名字方便删除
级联更新和级联删除
	-在更新父表中数据的时候，级联更新子表中的数据
	-在删除父表中数据的时候，级联删除子表中的数据
	on update cascade
	on delete cascade

	删除主键约束
		alter table t_class drop primary key;
	删除外键约束
		alter table t_student drop foreign key t_student_classno_fk;
	添加外键约束,级联更新
		alter table t_student add 
		constraint t_student_classno_fk 
		foreign key (classno) references t_class(cno) on update cascade;
