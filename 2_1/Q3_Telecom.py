def select_E(p, q, r, s, w):
    # A사
    E_a = w * p 
    # B사
    if w <= r: # 기본요금
        E_b = q 
    else: # 초과 요금
        E_b = s * (w - r) + q
    # 비교 
    if E_a < E_b: 
        print(f"A사: {E_a}")
    else:
        print(f"B사: {E_b}")
# 각 값 입력 받기        
select_E(*map(int, input("P, Q, R, S, W 순으로 입력: ").split()))



