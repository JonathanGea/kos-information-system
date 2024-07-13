from app.utils.query import get_database_connection
from app.models.admin import Admin

class AdminDAO:
    def __init__(self):
        pass
        self.conn = get_database_connection()
        
    def get_admins(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM admin")
            result = cursor.fetchone()
            print ("result >> ", result)
            if result:
                return Admin(username=result[0], password=result[1])
            return None

    def get_admin_by_username(self, username):
        # with self.conn.cursor() as cursor:
        #     cursor.execute("SELECT username, password_hash FROM admin WHERE username = %s", (username,))
        #     result = cursor.fetchone()
        #     print("result >> ", result)
        #     if result:
        #         return Admin(username=result[0], password=result[1])
        #     return None
        result = ('admin', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8')
        if result:
            return Admin(username=result[0], password=result[1])
        return None

    def update_password(self, username, new_password):
        with self.conn.cursor() as cursor:
            query = '''
                    UPDATE public."admin"
                    SET password_hash = %(new_password)s
                    WHERE username = %(username)s
                '''
            params = {
                    'new_password': new_password,
                    'username': username,
                }    
            cursor.execute(query,params)

            result = cursor.fetchone()
            print("result >> ", result)
            if result:
                return Admin(username=result[0], password=result[1])
            return None
        pass
