a , b = map(int, input().split())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
mi = min(a, b)
ma = max(a, b)
    
if a > b:
    a_lst, b_lst = b_lst, a_lst

result = []
    
for j in range(ma - mi + 1):
    current_sum = 0
    for k in range(mi):
        current_sum += a_lst[k] * b_lst[j+k]
    result.append(current_sum)

print(result)
print("{}".format(max(result)))