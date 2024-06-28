# from database import get_db_connection
from app.models.rooom import Room

class RoomDAO:
    def __init__(self):
        pass
        # self.conn = get_db_connection()

    def list_rooms(self):
        result = [
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True)
            ]
        if result :
            return result
        return None

    def add_room(self, name ):
        
        return True
