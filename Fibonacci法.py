'''
Author: 刘博文
Date: 2022-10-14 13:28:40
LastEditTime: 2022-10-14 16:11:46
Description: 无约束最优化问题————Fibonacci法
https://github.com/touchfisher
Copyright (c) 2022 by touchfisher 1632570150@qq.com, All Rights Reserved. 
'''
def f(x):
    return x**2 + 2*x

if __name__ == '__main__':
    e,a,b = map(float,input("请输入精度(如0.02),以及区间的左右端点a和b,全部以空格隔开:").split())
    Fibonacci = [1,1]
    Fibonacci_next = Fibonacci[0] + Fibonacci[1]
    while(Fibonacci_next < (b-a)/e):
        Fibonacci[0] = Fibonacci[1]
        Fibonacci[1] = Fibonacci_next
        Fibonacci_next = Fibonacci[0] + Fibonacci[1]
    lambda2 = a + Fibonacci[1] / Fibonacci_next * (b-a)
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
    # 最优点默认保留6位小数，最优值默认保留到整数，如需显示更高精度可去掉round函数
    lambda_finally = round((a + b) / 2, 6)
    print(f"最优点为{lambda_finally},最优值为{round(f(lambda_finally))}")
