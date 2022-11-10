import json
import uuid


class Item:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        print(self.id)

    def __repr__(self) -> str:
        return json.dumps(self.__dict__)
    
    def __eq__(self, __o: object) -> bool:
        return self.id == __o