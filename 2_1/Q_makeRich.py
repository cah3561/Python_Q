


# 일자 받기
n = int(input("예측할 일수를 입력해주세요."))

nlist = []
for i in range(n):
    s= int(input(f"{i+1}일의 매매가를 입력해주세요."))
    nlist.append(s)
# nlist = list(map(int,input().split()))
    
max_va = nlist[-1]
profit = 0

for j in range(n-2,-1,-1):

    if max_va < nlist[j]:
        max_va = nlist[j]
    else: 
        profit += max_va - nlist[j]
print(profit)