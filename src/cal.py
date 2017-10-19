import table

#变卦
def change_gua(num, change):
	if change == 0:
		if num % 2 == 0:
			return num + 1
		else:
			return num - 1
	elif change == 1:
		if num % 4 < 2:
			return num + 2
		else:
			return num - 2
	elif change == 2:
		if num < 4:
			return num + 4
		else:
			return num - 4

def cal(date, number):
	year = int(date[0 : 4])
	month = int(date[4 : 6])
	day = int(date[6 : 8])
	number = int(number)
	down = (year + month + day) % 8
	up = (year + month + day + number) % 8
	change = (year + month + day + number) % 6
	gua = table.gua[down][up]
	if change < 3:
		down = change_gua(down, change)
	else:
		up = change_gua(up, change % 3)
	gua_after_change = table.gua[down][up]
	return (gua + "  " if len(gua) == 3 else gua) + "  " + gua_after_change

if __name__ == '__main__':
	file = open("number.txt")
	try:
		for line in file:
			contents = line.split(",")
			number = contents[0]
			date = contents[1]
			result = cal(date, number)
			print result
	finally:
		file.close()