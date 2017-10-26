# -*- coding: utf-8 -*
import table

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
	gua_order = table.order[down][up]
	oldDown = down
	oldUp = up
	if change < 3:
		down = change_gua(down, change)
	else:
		up = change_gua(up, change % 3)
	gua_after_change = table.gua[down][up]
	gua_after_change_order = table.order[down][up]
	
	oldDown = 8 if oldDown == 0 else oldDown
	oldUp = 8 if oldUp == 0 else oldUp
	down = 8 if down == 0 else down
	up = 8 if up == 0 else up
	return str(oldDown).ljust(4, ' ') + str(oldUp).ljust(4, ' ') + str(down).ljust(4, ' ') + str(up).ljust(4, ' ') + str(gua_order).ljust(4, ' ') + str(gua_after_change_order).ljust(4, ' ') + (gua + "  " if len(gua) == 3 else gua) + "  " + gua_after_change

if __name__ == '__main__':
	file = open('number.txt')
	newFile = open('gua.txt', 'w')
	newFile.truncate()
	try:
		contentList = file.readlines()
		for line in contentList:
			line = line.replace('\r', '').replace('\n', '')
			contents = line.split(',')
			print contents
			if not contents:
				break
			number = contents[0]
			date = contents[1]
			result = cal(date, number)
			newFile.write(line + ',' + result)
			newFile.write('\n')
			print result
	finally:
		file.close()
		newFile.close()
