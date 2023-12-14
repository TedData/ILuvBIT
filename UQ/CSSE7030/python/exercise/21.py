#延迟输出
import time
a=[1,2,3]
b=a[::-1]
print(a[0:2])
time.sleep(3)#延迟3s
print(b)