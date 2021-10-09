# -*- codeing = utf-8 -*-
# @Author:彭柏霖pepinot
# @File_name:循环语句训练3.py
# @Software:PyCharm
# @Time:2021/10/9-10:57
# 任务描述
# 本关任务：求区间[a,b]中质数的数量。
# 输入2个正整数a和b，输出答案。（保证a≤b）
# 特别的，注意1不是质数！
# 相关知识
# 考虑最直接的做法，首先写一个for循环，从a到b。然后对其中的每一个数判断是否为质数
# 。而判断质数又需要一个循环，因此需要写一个双重循环。
# 编程要求
# 在右侧编辑器Begin-End处补充代码，求区间[a,b]中质数的数量。
# 测试说明
# 平台将对你编写的代码进行评测：
# 测试输入：2 100
# 预期输出：25
a,b = map(int,input().split())
count = 0
for num in range (a,b+1):
    if num > 1:
        for i in range (2,num):
            if (num % i == 0):
                break
        else:
            count += 1
print(count)