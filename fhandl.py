def r_content():
    f_name = input("Please enter your file name: ")
    print(f"File name is {f_name}")
    with open(f_name, "r") as f1:
        print(f1.read())
def w_content():
    f_name = input("please enter your file name " )
    w = input("please enter file content here ")
    with open(f_name, "w") as f1:
        f1.write(f"{w} ")



choice = input("please enter 'R' to read your file or 'W' to wrint content in your file \n" ).lower
r = choice
w = choice 
if choice == 'r':
    r_content()
elif choice == 'w':
    w_content()
else:
    print("please enter a valid option thanks... ")
















#f_name = input("please enter your file name " )
#w = input("please enter file content here ")

#with open(f_name, "w+") as f1:
#    f1.write(f"{w} \n")
  #  print(f1.read())