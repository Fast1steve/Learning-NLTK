import  numpy as np

#numpy的通用方法.universal Function.

'''1-数组中元素的通用函数'''
#对list中所有的数字取倒数,python中的做法如下:
x=[1,2,3,4,5]
result=[1/i for i in x]
print(result)

#在numpy中的做法
x=np.array(x)
print(x)
# 使用1除以一个向量,得到的结果是用1除以每一个向量中的元素得到的结果.
print(1 / x)  # [1.         0.5        0.33333333 0.25       0.2       ]

# 向量除以向量本身,得到全是1的向量
print(x / x)  # [1. 1. 1. 1. 1.]

# 向量的平方是对向量每个元素平方
print(x ** 2)  # [ 1  4  9 16 25]

#向量的三角函数,同理是对每个元素计算
print(np.sin(x))     #支持基本上所有的函数,cos什么的
#指数 以e为底exp   以2为底exp2
print(np.exp(x))
#对数log2 log10   log  注意log == ln
print(np.log(x))
print(np.log2(x))
#换底公式log3 / log4 == log3(4)
#开放 sqrt
print(np.sqrt(x))

#聚合函数
print(np.sum(x))    #所有元素求和
print(np.prod(x))   #所有元素的连乘

#聚合函数argmin和argmax
#argmin和argmax得到的是
# 函数数值最小时和最大时所在函数图像的位置,
# 不是函数的最小值和最大值本身.
# 在向量中使用,我们得到的是最大最小值的'''index(索引)'''
print(np.argmin(x))     #0
print(np.argmax(x))     #4

#基础统计
#均值：mean   标准差：std  方差：var 表示集合中元素的离散度
#协方差： cov     中位数：median
print(np.median(x))
#布尔数组也可以求和什么的
#去重 和集合运算
x = np.array([1,2,2,3,4,3,3,4,5])
y = np.array([1,2,2])
print(np.unique(x))
print(np.setdiff1d(x,y))  # Find the set difference of two arrays
print(np.intersect1d(x,y)) # Find the intersection(交集) of two arrays.
print(np.union1d(x,y))    # Find the union of two arrays

'''广播:让两个数组进行兼容性的匹配'''

a = np.array([0,1,2,3])
b = np.array([2,2,2,2])
print(a+b)      #[2 3 4 5] 对位相加

b=b.reshape(4,1)
print(b)
#结果如下:是变换成二维数组的b的每个元素,
# 分别去同a的每个元素相加,
# 得到了一个二维数组.相当于将a和b都补齐为矩阵后对位相加.
print(a+b)
#广播的形式也有不可行的情况:
# 行和列上的元素(元素也叫后援维度)不为1而且不相等的情况下,
# 广播不成立.
#只有在 两个列表后援维度轴长相等或其中一方长度为1,
# 则广播兼容.广播会在轴长缺失或长度为1的维度上进行.
c=np.arange(6).reshape(2,3)
d=np.arange(6).reshape(2,3)


'''比较掩码'''
np.random.seed(1)
'''
numpy.random.seed()函数可使得随机数具有预见性，
即当参数相同时使得每次生成的随机数相同
'''
x_rd=np.random.randint(1,100,(3,4))
print(x_rd>50)
#得到的结果是x列表中所有值>50的变为True,小于等于50的变为False
x_rd=(x_rd>70)


#可以使用True/False的掩码来提取列表中的元素.
#一个3*3的列表,可以用一个3*3的布尔列表来提取
x=np.arange(12).reshape((3,4))
#此时如果我们想提取x的第二行的第三个元素和第三行的第二个元素,可以用如下办法
print(x[np.array(x_rd)])
#print(x[np.array([[False,False,False],[False,False,True],[False,True,False]])])

#另一种类似的方法是Fancy Index,
# 将一个数组当做另个数组的取值索引

x = np.random.randint(1,100,(10,))
print(x)    #[38 13 73 10 76  6 80 65 17  2]
index = np.array([[0,2,1]])   #取得x数组的第一个,第三个和第二个元素
print(x[index])     #[[38 73 13]]

#使用where函数对数组筛选出的结果进行0/1编码
cond=np.array([[True,False],[True,False]])
#第一个参数为筛选条件,第二个参数为如果判定为True显示为1,
# 第三个参数为判定为False显示为0
#0和1也可以换成其他的数值.
x=np.where(cond,1,0)
print(x)




#排序
x=np.random.randint(1,100,(6,6))
print(x)
print(np.sort(x))





