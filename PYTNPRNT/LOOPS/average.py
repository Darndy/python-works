#program that calculate the average height from a list of height
height = input("enter the set of number to sum seperated by space ")
#split the string using the split function

splt_height = height.split()
#print(splt_height)
#find the lenght of the string
count = 0
for i in splt_height:
    count = count + 1
#print(count)
#convert the string into an integer using for loop.
for i in range(count):
    splt_height[i] = int(splt_height[i])
#print(splt_height)
#find th sum total of all
sum_all = 0
for i in splt_height:
    sum_all = i + sum_all
#print(sum_all)
avg = sum_all/count
print(round(avg))
