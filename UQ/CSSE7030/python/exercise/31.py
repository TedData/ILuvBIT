class aa(object):
	name='xxx'
	def test1(self):
		self.name='nnn'
		aa.name='zzz'
		print('1'*10)
	@classmethod#类方法一定要在方法的上面加上一个修饰器
	def test2(cls):#类方法的参数cls，代表当前的类
		cls.name='mmm'
		print('2'*10)
	@staticmethod#静态方法，属于类，没有默认传递参数
	def test3():
		print('3'*10)
a=aa()
a.test1()
a.test2()
aa.test2()
a.test3()
print(aa.name)
print(a.name)

'''
属性叫法---变量叫法---描述
类属性-----类变量----所有对象共享同一份类属性
实例属性---成员变量---每个不同对象，有不一样值的实例属性
'''	
	'''
方法类别------语法------描述
类方法----@classmethod-第一个形参cls，默认传递
静态方法--@staticmethod-没有默认传递的形参
对象方法---def 方法名()--第一个形参self，默认传递

'''	
	'''
你好，boyi，我想跟你核对一下我们之前的谈话记录：
2020年1月3日，你给我承诺，一个浮动贷款利率，还有4000cash back
1月8日，你给我发微信说：贷款已经弄好，4000cash之后会进贷款账户
1月12日，我问你，我的账户只收到了2000现金，为什么另外2000现金没有收到。你解释：一个是手动的，自动的那个会慢一点，一般一个月内会收到。
1月22日，我再次问你，为什么我还是没有收到第二笔2000现金。你的回答是：需要30天左右。
2月6日，我去银行找你，已经一个月了，为什么我还是没有收到第二笔2000现金。你的回答是：你会帮我催促，60天之内也是正常的。
2月11日，我再次问你，为什么我还是没有收到第二笔2000现金。你的回答是：他们说从settlement要up to 60天，我的大部分客户都30天左右收到cash back了，我会帮你催促他们，但我无法给你确切的时间。我的回复是：之前不是一直说30天会都收到cash back嘛，现在又改称60天，OK，我相信你，但是如果超过了60天，我还是没有收到，千万不要让我再多等一个月了

我现在想让你回答我两个问题：
第一，你对我上述我们之间的谈话，是否有异议？如果有请明确说明。
第二，我的第二笔2000现在，你们到底打算怎么处理。

我已经等你们三个月，我现在对你们很失望，请尽快回复。

Hello, boyi, I'd like to check our previous conversation with you.

On January 3, 2020, you promised me a floating loan rate and 4000 cash back
On January 8th, you gave me send WeChat messages and said: the loan has been completed, and 4000 cash will be put into the loan account
On January 12, I asked you, I only received 2000 cash in my account, why the other 2000 cash was not received. You explain: one is manual, the automatic one will be a little slower, generally within a month will receive.
On January 22, I asked you again why I still didn't receive the second 2000. Your answer: about 30 days.
On February 6th, I went to the bank to ask you, it has been a month, why I still haven't received the second 2000 cash. Your answer is: you will help me urge, within 60 days is normal.
On February 11th, I asked you again why I still didn't receive the second 2000. Your answer is: they said it would take up to 60 days from the settlement. Most of my clients have received cash back in about 30 days. I will help you to urge them, but I cannot give you the exact time. My reply is: before, you always said that I would receive cash back within 30 days, but now you change it to 60 days, OK, I believe you, but if it is more than 60 days, I still haven't received it, please don't make me wait another month.

I want you to answer two questions:
First, do you have any objection to my conversation with you? If so, please specify.
Second, what are you going to do with my second 2000 cash?

I have been waiting for you for three months, I am very disappointed with you now, please reply as soon as possible.
'''
