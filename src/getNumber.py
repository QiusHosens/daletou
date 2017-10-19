# -*- coding: utf-8 -*

import bs4
import re
import requests
import lxml.html
import time
       
file = open('number.txt','w')#,encoding='utf-8'
file.truncate()
index = 0
#year = time.localtime().tm_year
total = 0
arr = []
for year in range(2007, 2018):
	index = 0
	while True:
		arr1 = [0 for i in range(35)]
		arr2 = [0 for i in range(12)]
		index += 1
		num = str(year % 100).zfill(2) + str(index).zfill(3)
		url = "http://kaijiang.500.com/shtml/dlt/" + num + ".shtml"
		beautiful = requests.get(url).content
		soup = bs4.BeautifulSoup(beautiful,"lxml")
		region = soup.find(class_ = "kj_tablelist02")
		numbers = ""
		print num
		if region == None:
			break
		#else:
		#	numbers = region.find_all("tr")[1].find_all("tr")[1].find_all("td")[1].text
		#	print numbers
		#if numbers == "|":#get number
		#	numbers = ""
		else:
			redEles = soup.find_all(class_ = "ball_red")
			eleIndex = 0
			for ele in redEles:
				if ele.text == "":
					break
				if eleIndex == 0:
					numbers += ele.text
				else:
					numbers += " " + ele.text
				eleIndex += 1
			numbers += "|"
			blueEles = soup.find_all(class_ = "ball_blue")
			eleIndex = 0
			for ele in blueEles:
				if ele.text == "":
					break
				if eleIndex == 0:
					numbers += ele.text
				else:
					numbers += " " + ele.text
				eleIndex += 1
		if numbers != "" and numbers != "|":
			print numbers
			
			time = soup.find_all(class_ = "span_right")[0].text.split(" ")[0]
			date = re.compile(r'[1-9]\d*\.\d*|0\.\d*[1-9]|[1-9]\d*').findall(time);
			date = date[0].zfill(4) + date[1].zfill(2) + date[2].zfill(2)
			#print date
			file.write(num + "," + date + "," + numbers)
			file.write('\n')
			#times before 35
			# if len(arr) <= 35:
				# arr.append(numbers)
			# else:
				# del arr[0]
				# arr.append(numbers)
			# for nums in arr:
				# numsArr = nums.split("|")
				# num1Arr = numsArr[0].split(" ")
				# for i in num1Arr:
					# arr1[int(i) - 1] += 1
				# num2Arr = numsArr[1].split(" ")
				# for i in num2Arr:
					# arr2[int(i) - 1] += 1
			# print arr1
			# print arr2
			# redStr = "red:"
			# pos = 1
			# for i in arr1:
				# if pos == 1:
					# redStr += str(pos).zfill(2) + ":" + str(i)
				# else:
					# redStr += " " + str(pos).zfill(2) + ":" + str(i)
				# pos += 1
			# pos = 1
			# blueStr = "blue:"
			# for i in arr2:
				# if pos == 1:
					# blueStr += str(pos).zfill(2) + ":" + str(i)
				# else:
					# blueStr += " " + str(pos).zfill(2) + ":" + str(i)
				# pos += 1
			# file.write(redStr)
			# file.write('\n')
			# file.write(blueStr)
			# file.write('\n')
			# total += 1
file.close()
