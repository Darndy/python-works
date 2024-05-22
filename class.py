class User:
    def __init__(self, username, email, fullname, id, file="users.txt"):
        self.username = username
        self.email = email
        self.fullname = fullname
        self.id = id
        self.file = file
    
    def __str__(self):
        return f"{self.username}, {self.email}, {self.fullname}, {self.id}, {self.file}."
    
    def save(self):
        with open (self.file, "w+") as myfile:
            myfile.write(f"user: {self.username} email: {self.email} fullname: {self.fullname} identity: {self.id}")

    def changeuser(self, newuser):
        self.username = newuser
        self.save()

newuser = User("folashade", "folashade@gmail.com", "folakefolabi", 1 )
print(newuser)

