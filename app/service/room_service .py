# import hashlib
from app.dao.room_dao import RoomDAO

# class AdminService:
#     def __init__(self):
#         self.admin_dao = AdminDAO()

#     def login(self, username, password):
#         admin = self.admin_dao.get_admin_by_username(username)
#         if admin and admin.password == hashlib.sha256(password.encode()).hexdigest():
#             return True
#         return False

#     def is_password_same(self, username, old_password):
#         admin = self.admin_dao.get_admin_by_username(username)
#         if admin and admin.password == hashlib.sha256(old_password.encode()).hexdigest():
#             return True
#         return False

#     def change_password(self, username, new_password):
#         new_password_hashed = hashlib.sha256(new_password.encode()).hexdigest()
#         self.admin_dao.update_password(username, new_password_hashed)


class RoomService:
    def __init__(self):
        self.room_dao = RoomDAO()

    def list_rooms(self):
        return self.room_dao.list_rooms()
    
    
    