str1 = "PyNaTive"

bag1=""
bag2=""

for char in str1:
    if char.islower():
        bag1+=char
    else:
        bag2+=char


print(bag1+bag2)