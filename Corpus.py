import nltk
#nltk.download()
from nltk import bigrams
from collections import Counter
from nltk.book import *
'''使用concordance搜索指定内容'''
text1.concordance('America')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
'''使用similar查找相似上下文'''
text1.similar('very')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
'''commom_contexts 共用多个词汇的上下文'''
text1.common_contexts(['a','very'])
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
'''dispersion_plot离散图表示词汇分布情况'''
text1.dispersion_plot(["The","Moby","Dick","America"])
'''len 计算词汇长度'''
print(len(text1))

'''词汇表排序'''
print(sorted(set(text1)))

'''词汇表大小'''
print(len(set(text1)))

'''每个词平均使用次数'''
print(len(text1)/len(set(text1)))

'''特定词在文本中出现的次数'''
print(text1.count("smote"))

'''特定词在文本中所占的百分比'''
print(100*text1.count('a')/len(text1))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
'''
    搜索函数FreqDist
'''
fdist1=FreqDist(text1)
print(fdist1)
'''
    指定查找某个词的使用频率
'''
print(fdist1['whale'])
'''
    指定常用词累积频率图
'''
fdist1.plot(50,cumulative=True)
'''
    低频词出现1次查找
'''
print(fdist1.hapaxes())

'''
    细粒度查询
'''
V=set(text1)
longwords=[w for w in V if len(w)> 15]
print(sorted(longwords))
'''
    查找文本中单词长度大于10并且出现次数超过10次
'''
print(sorted(w for w in set(text1) if len(w)>10 and fdist1[w]>10))
'''
    词语搭配和双连词
'''
b=bigrams('This is a test')
print(Counter(b))

'''
    NLTK频率分布类中定义的函数
fdist=FreqDist(Samples),创建包含给定样本的频率分布
fdist.inc(Samples), 增加样本
fdist['monstrous'],计数给定样本出现的次数
fdist.freq('monstrous'),给定样本的频率
fdist.N(),样本总数
fdist.keys(),以频率递减顺序排序样本链表
for sample in fdist , 以频率递减顺序遍历样本
fdist.max(), 数值最大的样本
fdist.tabulate(), 绘制频率分布表
fdist.plot(), 绘制频率分布图
fdist.plot(cumulative=True), 绘制累积频率分布图
fdist1< fdist2, 测试样本在fdist1中出现的频率是否小于fdist2
'''

'''
    词汇比较运算符(s代表字符串)
s.startswith(t) 是否以t开头
s.endswith(t)   是否以t结尾
t in s          s是否包含f
s.islower()所有字符是否都是小写字母
s.isupper()所有字符是否都是大写字母
s.isalpha()所有字符是否都是字母
s.isalnum()所有字符是否都是字母或数字
s.isdigit()所有字符是否都是数字
s.istitle() 所有词首字母都是大写

'''

