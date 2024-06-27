import hashlib
from app.dao.admin_dao import AdminDAO

class AdminService:
    def __init__(self):
        self.admin_dao = AdminDAO()

    def login(self, username, password):
        admin = self.admin_dao.get_admin_by_username(username)
        print(admin)
        print(hashlib.sha256(password.encode()).hexdigest())
        if admin and admin.password == hashlib.sha256(password.encode()).hexdigest():
            print("True")
            return True
        return False

    def change_password(self, username, new_password):
        new_password_hashed = hashlib.sha256(new_password.encode()).hexdigest()
        self.admin_dao.update_password(username, new_password_hashed)
