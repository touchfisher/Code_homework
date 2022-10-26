'''
Author: 刘博文
Date: 2022-10-14 15:11:12
LastEditTime: 2022-10-26 23:38:02
Description: 无约束最优化问题————0.618法
https://github.com/touchfisher
Copyright (c) 2022 by touchfisher 1632570150@qq.com, All Rights Reserved. 
'''
def f(x):
    return x**2 + 2*x

if __name__ == '__main__':
    e,a,b = map(float,input("请输入精度(如0.02),以及区间的左右端点a和b,全部以空格隔开:").split())
    lambda2 = a + 0.618 * (b-a)
    f2 = f(lambda2)
    lambda1 = a + b - lambda2
    f1 = f(lambda1)
    while(b - a > e):
        if f2 > f1:
            b = lambda2
            lambda2 = lambda1
            lambda1 = a + b - lambda2
            f2 = f1
            f1 = f(lambda1)
        else:
            a = lambda1
            lambda1 = lambda2
            lambda2 = a + b - lambda1
            f1 = f2
            f2 = f(lambda2)
    lambda_finally = (a + b) / 2
    print(f"近似最优解为{lambda_finally},近似最优值为{f(lambda_finally)}")