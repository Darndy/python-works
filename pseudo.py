def read_content():
    f_name = input("Please enter the file name you want to read: ")
    print(f"File name is {f_name}")
    with open(f_name, "r") as f1:
        print(f1.read())

def write_content():
    f_name = input("please name your file \n")
    f_text = input("enter the content of your file below \n")
    with open(f_name, "w") as f1:
        f1.write(f"{f_text}")


while True:
    choice = input("Action (read or write) enter 'done' to quit: ").lower()
    if choice == "read" or choice == "r":
        read_content()
    elif choice == "write" or choice == "w":
        write_content()
    elif choice == 'done':
        break
    
    else:
        print("Invalid Choice")
