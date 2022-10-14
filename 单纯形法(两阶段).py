'''
Author: 刘博文
Date: 2022-09-23 21:58:40
LastEditTime: 2022-10-12 22:36:17
Description: 单纯形法自动求解器
https://github.com/touchfisher
Copyright (c) 2022 by touchfisher 1632570150@qq.com, All Rights Reserved. 
'''
from fractions import Fraction as f

print("单纯形法自动求解器")
var_num, func_num = map(int, input("请输入变量个数和约束方程的个数，以空格隔开:\n").split())
s = list(map(int, input("请输入各个变量在目标函数中的系数，以空格隔开:\n").split()))

temp_s = [f(0)] * var_num + [f(1)] * func_num
# print(f'S = {s}')

st = []
for i in range(func_num):
    temp = list(map(f,input(f"请输入第{i+1}行约束方程系数:\n").split()))
    temp += [f(1) if j == i else f(0) for j in range(func_num)]
    b = int(input(f"请输入第{i+1}行约束右端常数项:\n"))
    temp = [f(b)] + temp
    # print(temp)
    # temp += [f(1) if j == i else f(0) for j in temp]
    st.append(temp)

# 给出初始可行基
x_basic = []
add = var_num
for i in range(func_num):
    add += 1
    x_basic.append(add)

# 计算每个变量的检验数
q = []
for i in range(1,var_num+1):
    # 原变量的C都是0
    temp = f(0)
    # C（0）-b（每一个人工变量的b都是1，乘法省略）* st中的对应列
    for j in range(func_num):
        temp -= st[j][i]
    temp = temp_s[i-1] + temp
    q.append(f(temp))

# 补上约束方程个数（人工变量个）的0
q += [f(0)]*func_num

# 把-S算出来加到检验行前面，形成完整的一行
S = f(0)
for i in range(func_num):
    S -= f(st[i][0])
s_q = [S] + q


# 第一阶段迭代
####################################################################
end = False
# 如果一开始检验数均大于等于0，直接停止迭代，此时最优解为
if all(q) >= 0:
    end = True
print('\n第一阶段迭代')
while not end:
    end = True
    for i in s_q:
        print(i,end='\t')
    print()
    for i in st:
        for j in i:
            print(j,end='\t')
        print()
    print(f'基变量为:{[i+1 for i in x_basic]}')
    print('\n===========================================================')
    x_in = -1
    # 判断检验行q中的所有元素是否均大于等于0，如果有小于0的部分则继续迭代
    temp_q_i = []
    for i in range(len(q)):
        if q[i] < 0:
            # 如果某个检验数小于0，将其保存起来，说明还需要继续进行迭代
            temp_q_i.append(i)
            # 按照bland法则，保存最小下标负检验数的位置
            if x_in == -1:
                x_in = i
            end = False
    # 如果所有检验数都大于等于0，此时看是否基变量中存在
    if end == True:
        break
    
    for j in temp_q_i:
        # 对每一个负检验数对应的行来说，如果有大于0的元素，说明可以进行迭代，否则无解
        result_able = [st[i][j+1] for i in range(func_num)]
        if all(result_able) <= 0:
            end = True
    if end == True:
        print("该问题无解")
        break

    temp = []
    for i in range(func_num):
        # 确定出基变量，遍历每一行，如果该行小于等于0说明不能取该行的变量出基
        if st[i][x_in+1]<=0:
            temp.append(f(999))
        else:
            temp.append(st[i][0]/st[i][x_in+1])

    x_out = temp.index(min(temp))
    x_basic[x_out] = x_in

    # print(x_in,x_out)
    归一化倍数 = st[x_out][x_in+1]
    for i in range(len(st[x_out])):
        st[x_out][i] /= 归一化倍数
    for i in range(func_num):
        if i == x_out:
            continue
        beishu = -st[i][x_in+1]
        for j in range(len(st[i])):
            # st[i][j] = st[i][j] + st[i][x_in]*st[x_out][j]
            st[i][j] = st[i][j] + st[x_out][j]*beishu
    beishu  = -s_q[x_in+1]/st[x_out][x_in+1]
    for i in range(len(s_q)):
        s_q[i] += beishu * st[x_out][i]
    q = s_q[1:]


print("\n===========================================================")
print('\n第二阶段迭代')

# 第二阶段迭代
####################################################################
st = [i[:var_num+1] for i in st]

# 计算每个变量的检验数
q = []
for i in range(1,var_num+1):
    # 原变量的C都是0
    temp = s[i-1]
    # C（0）-b（每一个人工变量的b都是1，乘法省略）* st中的对应列
    for j in range(func_num):
        temp -= s[x_basic[j]] * st[j][i]
    q.append(f(temp))

# 把-S算出来加到检验行前面，形成完整的一行
S = f(0)
for i in range(func_num):
    S -= s[x_basic[i]] * st[i][0]
s_q = [S] + q

end = False
while not end:
    end = True
    for i in s_q:
        print(i,end='\t')
    print()
    for i in st:
        for j in i:
            print(j,end='\t')
        print()
    print(f'基变量为:{[i+1 for i in x_basic]}')
    print('\n===========================================================')
    x_in = -1
    # 判断检验行q中的所有元素是否均大于等于0，如果有小于0的部分则继续迭代
    temp_q_i = []
    for i in range(len(q)):
        if q[i] < 0:
            # 如果某个检验数小于0，将其保存起来，说明还需要继续进行迭代
            temp_q_i.append(i)
            # 按照bland法则，保存最小下标负检验数的位置
            if x_in == -1:
                x_in = i
            end = False
    # 如果所有检验数都大于等于0，迭代结束
    if end == True:
        break
    
    for j in temp_q_i:
        # 对每一个负检验数对应的行来说，如果有大于0的元素，说明可以进行迭代，否则无解
        result_able = [st[i][j+1] for i in range(func_num)]
        if all(result_able) <= 0:
            end = True
    if end == True:
        print("该问题无解")
        break

    temp = []
    for i in range(func_num):
        # 确定出基变量，遍历每一行，如果该行小于等于0说明不能取该行的变量出基
        if st[i][x_in+1]<=0:
            temp.append(f(999))
        else:
            temp.append(st[i][0]/st[i][x_in+1])

    x_out = temp.index(min(temp))
    x_basic[x_out] = x_in

    # print(x_in,x_out)
    归一化倍数 = st[x_out][x_in+1]
    for i in range(len(st[x_out])):
        st[x_out][i] /= 归一化倍数
    for i in range(func_num):
        if i == x_out:
            continue
        beishu = -st[i][x_in+1]
        for j in range(len(st[i])):
            # st[i][j] = st[i][j] + st[i][x_in]*st[x_out][j]
            st[i][j] = st[i][j] + st[x_out][j]*beishu
    beishu  = -s_q[x_in+1]/st[x_out][x_in+1]
    for i in range(len(s_q)):
        s_q[i] += beishu * st[x_out][i]
    q = s_q[1:]

print("迭代结束,最优解为X = [",end = '')
res = {}
res_print = []
tmp = 0
for i in x_basic:
    res[i] = st[tmp][0]
    tmp += 1
res_print = [res[i] if i in res else 0 for i in range(var_num)]
'''
for i in range(var_num):
    if i in res:
        print(res[i],end = '')
    else:
        print('0',end = '')
'''
for i in range(len(res_print)):
    print(res_print[i],end = '')
    if i != len(res_print)-1:
        print(',',end = ' ')
print(']')
print('最优值为:',-s_q[0])
