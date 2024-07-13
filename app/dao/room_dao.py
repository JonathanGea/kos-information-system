# from database import get_db_connection
from app.models.room import Room

class RoomDAO:
    def __init__(self):
        pass
        # self.conn = get_db_connection()

    def list_rooms(self):
        result = [
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True),
                Room(1, "Room 1", True),
                Room(2, "Room 2", False),
                Room(3, "Room 3", True)
            ]
        if result :
            return result
        return None

    def get_room(self, id ):
        room = Room(id=id, name="name", is_active=True) 
        if room :
            return room
        return None
    
    def add_room(self, name ):
        room = Room(id="1222", name=name, is_active=True) 
        if room :
            return room
        return None
    
    def deactivate_room(self, id ):
        room = Room(id=id, name="room name", is_active=True) 
        if room :
            return room
        return None
    
    def edit_room(self, id, new_name ):
        room = Room(id=id, name=new_name, is_active=True) 
        if room :
            return room
        return None
