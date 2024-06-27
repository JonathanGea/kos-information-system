# from database import get_db_connection
from app.models.admin import Admin

class AdminDAO:
    def __init__(self):
        pass
        # self.conn = get_db_connection()

    def get_admin_by_username(self, username):
        # with self.conn.cursor() as cursor:
        #     cursor.execute("SELECT username, password FROM admin WHERE username = %s", (username,))
        #     result = cursor.fetchone()
        #     if result:
        #         return Admin(username=result[0], password=result[1])
        #     return None
        result = ('admin', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8')
        if result:
            return Admin(username=result[0], password=result[1])
        return None

    def update_password(self, username, new_password):
        with self.conn.cursor() as cursor:
            cursor.execute("UPDATE admin SET password = %s WHERE username = %s", (new_password, username))
            self.conn.commit()
