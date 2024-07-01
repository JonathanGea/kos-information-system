from app.dao.room_dao import RoomDAO

class RoomService:
    def __init__(self):
        self.room_dao = RoomDAO()

    def list_rooms(self):
        rooms = self.room_dao.list_rooms()
        return [room.to_dict() for room in rooms]
    
    def add_room(self, name):
        room = self.room_dao.add_room(name)
        if room :
            return room.to_dict()
        return None
    
    def deactivate_room(self, id):
        room = self.room_dao.deactivate_room(id)
        if room :
            return room.to_dict()
        return None
    
    def edit_room(self, id, new_name):
        room = self.room_dao.edit_room(id, new_name)
        if room :
            return room.to_dict()
        return None
    
    
    