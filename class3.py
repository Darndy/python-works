import os

class User:
    def __init__(self, username, email, fullname, id, file="users.txt"):
        self.username = username
        self.email = email
        self.fullname = fullname
        self.id = id
        self.file = file
    
    def __str__(self):
        return f"{self.username}, {self.email}, {self.fullname}, {self.id}, {self.file}"
    
    def save(self):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.file), exist_ok=True)
        
        try:
            with open(self.file, "w") as myfile:
                myfile.write(f"user: {self.username} email: {self.email} fullname: {self.fullname} identity: {self.id}\n")
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
    
    def changeuser(self, newuser):
        self.username = newuser
        self.save()

# Example usage
newuser = User("folashade", "folashade@gmail.com", "folakefolabi", 1)
print(newuser)  

# Assuming you want to test the save functionality
#newuser.save()  # Uncomment this line if you want to see how the save method works
