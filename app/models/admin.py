class Admin:
    def __init__(self ,username, password, id = None):
        self.id = id
        self.username = username
        self.password = password
        
    def __str__(self):
        return f"Admin(username={self.username}, password={self.password})"
    
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
        }