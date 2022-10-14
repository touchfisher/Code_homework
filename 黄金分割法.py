'''
Author: 刘博文
Date: 2022-10-14 15:11:12
LastEditTime: 2022-10-14 15:17:07
Description: 单纯形法自动求解器
https://github.com/touchfisher
Copyright (c) 2022 by touchfisher 1632570150@qq.com, All Rights Reserved. 
'''
def f(x):
    return x**2 + 2*x

if __name__ == '__main__':
    e,a,b = map(float,input().split())
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
    lambda_finally = round((a + b) / 2, 6)
    print(f"最优点为{lambda_finally},最优值为{round(f(lambda_finally))}")