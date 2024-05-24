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
            with open(self.file, "a+") as myfile: 
                myfile.write(f"user:{self.username} email:{self.email} fullname:{self.fullname} identity:{self.id}\n")
        except ValueError:
            print(f"An error occurred while writing to the file: ")

    def changeusername(self, newuser):
        self.username = newuser
        self.save()
    
class Person(User):
    def getinfo():
        print("enter your information here as indicated \n")
        username = input("enter your username here: \n")
        email = input("enter your email adress here: \n")
        fullname = input("enter your full name here: \n")
        id = input("enter your i.d number here: \n")
        file = input("please name the file to save your info to(should end with .txt \n): ")
        return User(username, email, fullname, id, file)

def main():
    newuser = Person()
    option = input("do you want to change your username? y or n").lower()
    if option == 'y':
        username = input("enter new username \n")
        newuser.changeusername(username)
    elif option == 'n':
        newuser.save()
        print(newuser)
    else:
        raise ValueError("invalid selection")

main()
