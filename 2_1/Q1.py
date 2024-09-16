n, k = map(int, input().split())
scores = []
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for _ in range(n):
    mid, fin, home = map(int, input().split())
    score = mid * 0.35 + fin * 0.45 + home * 0.2
    scores.append(score)

target = scores[k-1]
scores.sort(reverse=True)
rate = n//10
ratio_score = scores.index(target) // rate
print(scores[ratio_score])
