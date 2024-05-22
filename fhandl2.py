def read_content():
    while True:
        try:
            f_name = input("Please enter the file name you want to read: ")
            with open(f_name, "r") as f1:
                print(f"File name is {f_name} and the content is ")
                print(f1.read())
        except ValueError:
            print("file name not present ")
            break

def write_content():
    f_name = input("please name your file \n")
    f_text = input("enter the content of your file below \n")
    with open(f_name, "w") as f1:
        f1.write(f"{f_text}")


while True:
    choice = input("Action (read or write): ").lower()
    if choice == "read" or choice == "r":
        read_content()
        break
    elif choice == "write" or choice == "w":
        write_content()
        break
    else:
        print("Invalid Choice")






