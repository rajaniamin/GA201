str1 = "Ault"
str2 = "Kelly"
length = len(str1)
mid_index = length // 2

str3 = str1[:mid_index] + str2 + str1[mid_index:]

print(str3)
