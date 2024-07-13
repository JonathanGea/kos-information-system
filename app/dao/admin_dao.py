from app.utils.query import execute_query_with_return, execute_query, fetch_query
from app.models.admin import Admin

class AdminDAO:
    def __init__(self):
        pass
        
    def get_admins(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM admin")
            result = cursor.fetchone()
            
            # print ("query : ", query)
            # print ("params : ", params)
            # print ("result : ", result)
            
            if result:
                return Admin(username=result[0], password=result[1])
            return None
        

    def get_admin_by_username(self, username):
        try:
            query = '''
                    SELECT username, password_hash FROM admin WHERE username = %(username)s
                '''
            params = {
                    'username': username,
                }    
            result = fetch_query(query,params)
            
            print ("query : ", query)
            print ("params : ", params)
            print ("result : ", result)
            
            if result:
                return Admin(username=result[0], password=result[1])
            return None
        except Exception as e:
            print ("[ERROR] in get_admin_by_username :: {e}")
            return False


    def update_password(self, username, new_password):
        try:
            query = '''
                    UPDATE public."admin"
                    SET password_hash = %(new_password)s
                    WHERE username = %(username)s
                '''
            params = {
                    'new_password': new_password,
                    'username': username,
                }    
            result = execute_query_with_return(query,params)

            print ("query : ", query)
            print ("params : ", params)
            print ("result : ", result)
            
            if result:
                return True
            return None
        except Exception as e:
            print ("[ERROR] in update_password :: {e}")
            return False
