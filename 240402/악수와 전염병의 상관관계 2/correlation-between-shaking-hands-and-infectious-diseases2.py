# 클래스 선언
class Shake:
    def __init__(self, time, person1, person2):
        self.time, self.person1, self.person2 = time, person1, person2

# 변수 선언 및 입력
n, k, p, t = tuple(map(int, input().split()))	
shakes = []
for _ in range(t):
    time, person1, person2 = tuple(map(int, input().split()))
    shakes.append(Shake(time, person1, person2))

shake_num = [0] * (n + 1)
infected = [False] * (n + 1)

infected[p] = True

# Custom Comparator를 활용한 정렬
shakes.sort(key = lambda x: x.time)

# 각 악수 횟수를 세서,
# K번 초과로 악수를 했을 시 전염시키지 않습니다.
for shake in shakes:
	target1 = shake.person1
	target2 = shake.person2
	
	# 감염되어 있을 경우 악수 횟수를 증가시킵니다.
	if infected[target1]:
		shake_num[target1] += 1
	if infected[target2]:
		shake_num[target2] += 1
	
	# target1이 감염되어 있고 아직 K번 이하로 악수했다면 target2를 전염시킵니다.
	if shake_num[target1] <= k and infected[target1]:
		infected[target2] = True
	
	# target2가 감염되어 있고 아직 K번 이하로 악수했다면 target1을 전염시킵니다.
	if shake_num[target2] <= k and infected[target2]:
		infected[target1] = True
		
for i in range(1, n + 1):
	if infected[i]:
		print(1, end="")
	else:
		print(0, end="")