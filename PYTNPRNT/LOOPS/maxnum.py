#program that print the maximum number from a set of nums
numbers = input("enter the set of numbers ")
number_splt = numbers.split()
#print(number_splt)
#find the lenght of the numbers
count = 0
for i in number_splt:
    count+=1
#print(count)
#convert to an integer
for i in range(count):
    number_splt[i] = int(number_splt[i])
#print(number_splt)
#finding out the max number
maxi_num = number_splt[0]
#for i in range(count):
   # maxi_num = number_splt[0]
#print(maxi_num)
for i in number_splt:
   if maxi_num[i] > maxi_num:
        maxi_num = maxi_num[i]
print(maxi_num)

