#write a simple python code that continues to request for price of things a customer bought and when user is done, 
#it will ask user to input done and the program will calulate the total price ofthe goods

price = 0
total = 0

while price != "done":
    price = input("Enter the price of the item: ").lower()
    try:
        price = float(price)
        total += price
    except:
        if price != 'done':
            print("invalid")
while True:
    discount = input("please enter preffered discount (from 1 - 100) ")
    try:
        discount = float(discount)
        assert discount <= 100.0 and discount >= 0
        break
    except:
        print("invalid discount")


p_discount = (discount/100) * total
new_price = total - p_discount
        #print("please enter a valid discount rate")
#p_discount = (discount / 100) * total
#new_price = total - p_discount

print(f"Total price is: {total}")
print(f"Total price after discount of {discount}% is: {new_price}")
#after total price has been calculated, ask yuser for percentage discount(range 1 to 100)
#cal how muchnuser will pay after the dicount
# print total price, discount, total price after discount.
