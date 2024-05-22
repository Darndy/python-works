# Store (Username Email FullName and Id)

class User:

    def _init_(self, username, email, fullname, id, file="users.txt"):
        
        self.username = username
        self.email = email
        self.fullname = fullname
        self.id = id
        self.file = file

    def _str_(self):

        #print(f"{self.username} {self.email} {self.fullname} {self.id} - Line 14")

        return f"{self.username} {self.email} {self.fullname} {self.id} {self.file}"

    def save(self):

        with open(self.file, 'a') as myfile:
            myfile.write(f"User: {self.username} email: {self.email} fullname:{self.fullname} id:{self.id}\n")

    def changeusername(self, newuser):
        self.username = newuser
        self.save()


newuser = User("Opeoluwa1", "opeoluwaadeyeri@gmail.com", "Opeoluwa", 2,)

print(newuser)
#newuser.changeusername("Jeremiah")

#print(newuser)