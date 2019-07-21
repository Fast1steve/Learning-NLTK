#   numpy开始一点点找回感觉
#代码如下：

import numpy as np
#import normal
# The underlying numpy is implemented using C.
# The computational efficiency is very good.
# numpy can replace python's native array.

############## Array creation ###########
# 1.0- using list
x1=np.array([1,2,3])  #x1 = np.ndarray([1,2,3])两者相同.只不过是别名
print (type(x1))    #<class 'numpy.ndarray'>
x2=np.array([[1,2,3],[2,3,4]])  #(3,) (2, 3),shape函数显示的是列表中每个对象包含的元素书构成的tuple,有几个数字代表数组就是几纬的.
print(x1,x2)
'''z=np.array([[1,2]])
print(z.shape)
'''
print (x1.shape,x2.shape)
'''
x[1,2]的shape值(2,)，意思是一维数组，数组中有2个元素

y[[1],[2]]的shape值是(2,1)，意思是一个二维数组，每行有1个元素

z [[1,2]]的shape值是（1，2），意思是一个二维数组，每行有2个元素
'''
# 当x1是一个二维数组的时候,打印出的shape是(1,3)
# sklearn中很多时候要的都是[[1,2,3]]这种形式的数组


#1.1-打印数组的维度
x1= np.array([[1,2,3]])
num=x1.ndim
print(num)

##1.2-ndarra中所有的元素要求类型相同,可以通过dtype来查看ndarray中的元素类型.
print(x1.dtype) #int32,int32是所有int形数据的默认值
x3=np.array(['1','2','3'])
print(x3.dtype)     #<U1


#1.3-可以手动改变dtype
print (x1)
x1.dtype= 'float32'
print(x1.dtype,x1)
#float64 [[4.9e-324 9.9e-324 1.5e-323]],可以看到,
#当改变一个数组的类型时,其存储数据的方式也会相应改变
#改变数据的类型需要类型之间可以转换,如果用字符串转为数字则会报错,如下两行代码.
# x3.dtype = 'int64'
# print(x3.dtype,x3)


#2.0-numpy还帮助我们封装了方便的创建一些demo数组的方法.
#2.1-生成一个全零的列表.使用方法zeros
print(np.zeros((2,3)))#该方法的参数为一个元组(shape)

#2.2生成一个全1的列表.使用np.ones()
print(np.ones((2,3,4)))
#结果如下,生成了4列3行的2个list组成的对象.元素值全部为1.
'''
[[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]
 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]]
'''

#2.3-构建任意形状,元素值统一为一个任意值的list,使用np.full
#第一个参数为shape值,指定生成list的形状,第二个参数为每个元素要指定的值.
print(np.full((3,2),444))

#2.4-生成一个线性增长的list.元素值为0,2,4,6...此方法在机器学习使用graid_search调参的时候经常用到.

#第一个参数为起始值,第二个参数为终止值,第三个参数为step,step默认值为1.取值范围左闭右开不包含20.第一个和第三个参数不写的时候默认值为0和1print(np.arange(2,20,2))
#第一个参数为起始值,第二个参数为终止值,第三个参数为要的元素个数

#2.5-指定起始值和终止值,生成固定个数元素的列表
print(np.linspace(0,1,20))
print(np.linspace(0,1,20).shape) #第一个参数为起始值,第二个参数为终止值,第三个参数为要的元素个数

'''###############################生成随机数列表#######################'''

#1.0-生成一个0到1之间随机数组成的list,可以指定形状
print(np.random.random((3,3)))

#1.1-生成正太分布(高斯分布)的小工具.可以指定均值和方差.
print(np.random,np.random.normal(loc=3,scale=4,size=(2,3)))#loc : 均值   scale : 方差  size : 形状,需要是元组.

#1.2- 生成随机整数
#参数1:起始值  参数2:终止值  参数3:形状
print(np.random.randint(0,10,(3,3)))


#1.3-生成单位矩阵(对角线全部为1,其他全部为0的方阵).....需要注意:单位矩阵的生成直接在np的方法里,不是在np.random中.
# 单位矩阵一定是2维的,行列相等,想要10*10的单位矩阵,只需要传递参数10即可
print(np.eye(10))


#1.4-生成未初始化矩阵. 创建出来直接打印,一般都是有值的.
#创建的empty矩阵只是在内存中标记了要使用哪些内存地址.内存地址中允许存在原来废弃的数据,用的时候再清理/更改为要存储的值
print(np.empty((3,2)))

'''##########################
#######数组的属性###############
######################'''
x1=np.random.randint(10,size=6)
x2=np.random.randint(10,size=(3,4))
x3=np.random.randint(10,size=(3,4,5))

print(x3)
#1.0-统计数组中的元素个数 x.size
print(x3.size)  #其实就是各个维度数相乘

#1.1-列表的维度 ndim
print(x3.ndim)

#1.2- 列表的形状shape
print(x2.shape)

#1.3-列表数据的类型:data_type   使用dtype
print(x1.dtype)

#1.4-每个元素占的字节数
print(x1.itemsize)
#1.5-list 一共占多少内存
print(x1.nbytes)

'''重要:#####################
############数组的索引######
###############################'''
print(x2)

#1.0 取第一行
print(x2[0])
#1.1取第一行第二个元素
print(x2[0][1])
#取m行第n个元素
#print(x2[0][1]) ==print(x2[0,1])
print(x2[0,1])
#1.2-取x2的第一列(每行的第一个元素).
print(x2[:,1])  #所有元素会组成一个list返回.
#":"前是行的取值范围,后边是列的取值范围.当取值范围为空的时候为取全集.
print(x2[:0])       #结果为空,必须使用坐标表示法
#1.3-每隔n个取一个元素x2[start:end:step],不写时为默认的start和end
print(x2[::2])   #从第0个元素开始,每2个元素取后边的一个.
#从第0个元素开始,每2个元素取后边的一个.之后再取每隔元素的第二个元素
print(x2[::2,1])
#1.4 -取第二行的第三个元素和第三行的第四个元素
##a.将两个元素单独取出，拼成list返回
print(np.array((x2[1,2],x2[2,3])))
##b.坐标取法
print(x2[[1,2],[2,3]])

#1.5-使用负数索引取值
print(x2[-1])   #取得x2的最后一个元素
#1.6-使用负数step取值
print(x2[::-1])#将x2逆向打印，先打印最后一个元素，然后倒数第二个元素
print(x2[::-1,::-1])#取得x2的镜像数组
print(np.transpose(x2))#取得x2的转置

#1.7-列表调整形状
x=np.arange(1,13)
print(x)
#reshape是将列表的所有元素取得之后,按照新的形状组合,生成一个新的列表返回,不改变原始列表的内容.原始列表和新形状的列表元素必须相同.
x_r=x.reshape((3,4))
print(x_r)

print(x_r[::-1,::-1])

'''重要::::在numpy中,所有切片出来的数组,都是源数组的镜像.
改变视图中的值,源数组响应改变,reshape不会.
python原生的数组整好相反,切片出来的是新数组,不影响原数组'''

'''####################
####数组变形##############
#########################'''
# 通过reshape函数可以将任意两个总元素个数相同的列表相互转换
'''######################
###数组的拼接和分裂#########
##########################'''
x_origin=np.arange(1,4)
y_origin=np.arange(4,7)
print(x_origin,y_origin)
#将两个独立的数组拼接为一个大数组
x_y_splice=np.concatenate([x_origin,y_origin])
print(x_y_splice)
'''在原生的python列表中,可以直接使用"+"来解决
numpy不使用加号是因为在直觉上要保持向量的加法.'''
print(x_origin + y_origin)
x = [1,2,3]
y = [4,5,6]
print(x+y)  #[1, 2, 3, 4, 5, 6]
'''
#当x和y是二维数组的时候,组合出的新数组的维度为 x的维度+y的维度.
此时axis = 0在外层融合.
当axis = 1时,是相同Index(索引)的元素相加,是内层对位融合.
'''
x = [[1,2,3],[4,5,6]]
y = [[4,5,6],[1,2,3]]
print(np.concatenate([x,y]))
print(np.concatenate([x,y],axis=0))
print(np.concatenate([x,y],axis=1))
#另外,当concatenate函数axis = 0时,相当于vstack((x,y))函数,
#当concatenate函数axis = 1时,相当于hstack((x,y))函数.四者等价
# 数组的分裂
x = [1,2,3,4,5,6,7,8,9,0]
#传入的参数[3,5]相当于在x的第三个和第五个元素前切了两刀,
#分成了三个list.也可以多切几刀.
x1,x2,x3=np.split(x,[3,6])
print(x1,x2,x3)

#vsplit 用来横向切多维数组的.
x=np.arange(16).reshape(4,4)
print(x)
uper,lower=np.vsplit(x,[3])
print('uper：',uper,'\n','lower:',lower)


#hsplit 用来纵向切多维数组,
# 单纯的像切韭菜一样的切.切下来的合并为一个整体
x=np.arange(16).reshape(4,4)
print(x)
left,right=np.hsplit(x,[3])
print('left:','\n',left,'\n','right:','\n',right)


