'''
Author: 刘博文
Date: 2022-10-26 15:19:21
LastEditTime: 2022-10-26 15:21:35
FilePath: \YunChouXue\梯度下降法.py
Description: 梯度下降法——例题4-14
https://github.com/touchfisher
Copyright (c) 2022 by touchfisher 1632570150@qq.com, All Rights Reserved. 
'''
import numpy as np
n = 3
x = np.array([4,4],dtype=np.float64)
while n:
    print(n)
    n -= 1
    x1,x2 = x[0],x[1]
    p = np.array([2*x1,4*x2],dtype=np.float64)
    Q = np.array([[2,0],[0,4]],dtype=np.float64)
    _lambda = p.dot(p.T) / (p.T.dot(Q)).dot(p)
    print(_lambda)
    x = x - _lambda * p
    print(x)