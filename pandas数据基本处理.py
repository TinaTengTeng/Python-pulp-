import pandas as pd
import numpy as np
import pulp
import warnings
warnings.filterwarnings('ignore')
# mathmodel04_v1.py
# Demo01 of mathematical modeling algorithm
# Solving linear programming with PuLP.
# Copyright 2021 Youcans, XUPT
# Crated：2021-05-28

import pulp
MyProbLP = pulp.LpProblem("LPProbDemo1", sense=pulp.LpMaximize)  # 求最大值
x1 = pulp.LpVariable('x1', lowBound=0, upBound=7, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, upBound=7, cat='Continuous')
x3 = pulp.LpVariable('x3', lowBound=0, upBound=7, cat='Continuous')
MyProbLP += 2*x1 + 3*x2 - 5*x3  	# 设置目标函数
MyProbLP += (2*x1 - 5*x2 + x3 >= 10)  # 不等式约束
MyProbLP += (x1 + 3*x2 + x3 <= 12)  # 不等式约束
MyProbLP += (x1 + x2 + x3 == 7)  # 等式约束
MyProbLP.solve()  # youcans@xupt
print("Status:", pulp.LpStatus[MyProbLP.status]) # 输出求解状态
for v in MyProbLP.variables():  # youcans
    print(v.name, "=", v.varValue)  # 输出每个变量的最优值
print("Max F(x) = ", pulp.value(MyProbLP.objective))  #输出最优解的目标函数值
