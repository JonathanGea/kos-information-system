from app.dao.room_dao import RoomDAO

class RoomService:
    def __init__(self):
        self.room_dao = RoomDAO()

    def list_rooms(self):
        return self.room_dao.list_rooms()
    
    def get_room(self):
        return self.room_dao.get_room()
    
    
    