class Room:
    def __init__(self, id, name, is_active):
        self.id = id
        self.name = name
        self.is_active = is_active
        
    def __str__(self):
        return f"Room(id={self.id}, name={self.name}, is_active={self.is_active})"