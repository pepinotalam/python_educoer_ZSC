# -*- codeing = utf-8 -*-
# @Author:彭柏霖pepinot
# @File_name:循环语句训练2.py
# @Software:PyCharm
# @Time:2021/10/9-10:48
# 任务描述
#
# 本关任务：给定2个正的int，求其最大公约数。
# 相关知识
#
# 所谓a和b的最大公约数，就是既是a的因子、也是b的因子，而且是所有满足该条件数中最大的。
#
# 例如12和8的公因子有1/2/4，因此4是12和8的最大公约数。
# 编程要求
#
# 在右侧编辑器Begin-End处补充代码，求给定2个数的最大公约数。
# 测试说明
#
# 平台将对你编写的代码进行评测：
#
# 测试输入：12 8
#
# 预期输出：4
# 开始你的任务吧，祝你成功！
a,b = map(int,input().split())
list = []
for i in range (1,100):
    if (a % i==0) and (b % i==0):
        list.append(i)
print(max(list))
