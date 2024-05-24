class User:
    def __init__(self, username, email, fullname, id, file="users.txt"):
        self.username = username
        self.email = email
        self.fullname = fullname
        self.id = id
        self.file = file

    def __str__(self):
        return f"{self.username}, {self.email}, {self.fullname}, {self.id},"

    def save(self):
        try:
            with open(self.file, "a") as myfile: 
                myfile.write(f"user:{self.username} email:{self.email} fullname:{self.fullname} identity:{self.id}\n")
        except IOError:  
            print(f"An error occurred while writing to the file: {self.file}")

    def changeusername(self, newuser):
        self.username = newuser
        self.save()

class Person(User):
    def __init__(self, username=None, email=None, fullname=None, id=None, file=None):
        super().__init__(username, email, fullname, id, file)


    def getinfo():
        print("Enter your information here as indicated\n")
        username = input("Enter your username here:\n")
        email = input("Enter your email address here:\n")
        fullname = input("Enter your full name here:\n")
        id = input("Enter your ID number here:\n")
        file = input("Please name the file to save your info to (should end with.txt):\n")
        return User(username, email, fullname, id, file)

def main():
    newuser = Person.getinfo()  
    option = input("Do you want to change your username? y or n \n").lower()
    if option == 'y':
        username = input("Enter new username\n")
        newuser.changeusername(username)
    elif option == 'n':
        newuser.save()
        print(newuser)
    else:
        raise ValueError("Invalid selection")

    main()
