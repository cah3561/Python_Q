# 최대값 구하기
# N 개의 숫자로 구성된 숫자열 ai 와 M:bj 가 있음
# 서로 이동하여 위치 변경 가능
# 서로 마주보는 숫자들을 곱한 뒤 모두 더한 최대값을 구하라
import queue

n = [1,3,5]
m = [3,6,7,5,8]
if len(n) > len(m):
    n,m = m,n
a = len(n)
b = len(m)
ans =[]
d= 0
# if a<b :
for i in range(b-a+1):
    for j in range(a):

        d += m[j+i] * n[j]
        print(d)
    ans.append(d)
    d =0
    print(ans)
            
# else:
#         for i in range(a-b+1):
#             for j in range(b):

#                 d += m[j] * n[j+i]
#                 print(d)
#             ans.append(d)
#             d=0
#             print(ans)
                

print(max(ans))
