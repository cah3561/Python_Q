import numpy as np

# 1. 원소가 모두 5인 (3, 4, 5) 형태의 numpy.array 출력
array_5 = np.full((3, 4, 5), 5)
print("1. 원소가 모두 5인 (3, 4, 5) 형태의 numpy.array:")
print(array_5)

# 2. -30 ~ 30 범위의 난수로 이루어진 (4, 5) 형태의 numpy.array 출력
np.random.seed(0)  # For reproducibility
array_random = np.random.randint(-30, 31, (4, 5))
print("\n2. -30 ~ 30 범위의 난수로 이루어진 (4, 5) 형태의 numpy.array:")
print(array_random)

# 행을 기준으로 오름차순 정렬한 결과
sorted_by_row = np.sort(array_random, axis=1)
print("\n행을 기준으로 오름차순 정렬한 결과:")
print(sorted_by_row)

# 전체 배열을 1차원 배열로 변경하여 오름차순 정렬한 결과
flattened_sorted = np.sort(array_random.flatten())
print("\n전체 배열을 1차원 배열로 변경하여 오름차순 정렬한 결과:")
print(flattened_sorted)

# 3. 주어진 배열을 행을 기준으로 3개의 배열로 분할하여 각 배열의 원소를 제곱한 결과를 병합
array_to_split = np.array([[2, 4, 6],
                           [8, 10, 12],
                           [14, 16, 18]])
print("\n3. 주어진 배열:")
print(array_to_split)

# 행을 기준으로 3개의 배열로 분할
split_arrays = np.split(array_to_split, 3)
print("\n분할된 배열들:")
for i, arr in enumerate(split_arrays):
    print(f"Array {i+1}:")
    print(arr)

# 각 배열의 원소를 제곱한 결과
squared_arrays = [arr ** 2 for arr in split_arrays]
print("\n각 배열의 원소를 제곱한 결과:")
for i, arr in enumerate(squared_arrays):
    print(f"Squared Array {i+1}:")
    print(arr)

# 병합하여 원본 배열과 같은 차원으로 만들기
merged_array = np.vstack(squared_arrays)
print("\n제곱한 결과를 병합하여 원본 배열과 같은 차원으로 만든 결과:")
print(merged_array)