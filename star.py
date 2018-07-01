#coding: UTF-8
import random

#メル計算関数
def cost(s):
	if s == 10:
		return 5470800
	elif s == 11:
		return 6919400
	elif s == 12:
		return 8588400
	elif s == 13:
		return 10490600
	elif s == 14:
		return 12638500
	elif s == 15:
		return 30087200
	elif s == 16:
		return 70875800
	else:
		print("ERROR")
		exit()

#成功失敗判定
def star_success(s,r):
	catch = 45 #スターキャッチなしなら0にする
	if s == 10:
		return 1
	elif s == 11:
		if r <= 350 + catch:
			return 1
		else:
			return -1
	elif s == 12:
		if r <= 300 + catch:
			return 1
		elif r >= 994:
			return -2
		else:
			return -1
	elif s == 13 or s == 14:
		if r <= 300 + catch:
			return 1
		elif r >= 987:
			return -2
		else:
			return -1
	elif s == 15:
		return 1
	elif s == 16:
		if r <= 300 + catch:
			return 1
		else:
			return -1
	else:
		print("ERROR")
		exit()

#メインメソッド
star = 10
sum  = 0
sum_now = 0
sc = 0
for i in range(100000):
	while 1:
		if star == 17:
			print(sum_now)
			sum += sum_now
			sum_now = 0
			star = 10
			sc = 0
			break
		x = random.randint(1,1000)
		sum_now += cost(star) 
		sc = star_success(star,x)
		if sc == 1:
			star += 1
		elif sc == -1:
			star -= 1
		elif sc == -2:
			star = 12
		else:
			print("ERROR")
			exit()
print("END")
print(sum/100000)
