# P1       -> P1の一個あたりの利益    2
# P2       -> P2の一個あたりの利益    5
# M1 M2 M3 -> P1を作るのに必要な材料  2 8 3
# M1 M2 M3 -> P2を作るのに必要な材料  6 6 1
# M1 M2 M3 -> 利用可能量            27 45 15

print("製品1の利益:", end=""); P1_pro = int(input())
print("製品2の利益:", end=""); P2_pro = int(input())
print("製品1に必要な材料:", end=""); P1_res = list(map(int, input().split()))
print("製品2に必要な材料:", end=""); P2_res = list(map(int, input().split()))
print("製品1の利益:", end=""); all_res = list(map(int, input().split()))

from pulp import *
m = LpProblem(sense=LpMaximize) # 数理モデル
x = LpVariable('x', lowBound=0) # 変数
y = LpVariable('y', lowBound=0) # 変数
m += P1_pro * x + P2_pro * y # 目的関数
for i in range(len(all_res)):
    m += P1_res[i] * x + P2_res[i] * y <= all_res[i] # 材料iの上限の制約条件

m.solve() # ソルバーの実行
print("製品1を",value(x),"個","製品2を",value(y),"個") # 4, 6
print("総利益",value(x) * P1_pro + value(y) * P2_pro) # 4, 6
