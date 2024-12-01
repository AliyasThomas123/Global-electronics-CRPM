from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, entity_id):
        self.entity_id = entity_id

    @abstractmethod
    def to_dict(self):
        """Convert the object to a dictionary."""
        pass

    def __str__(self):
        return f"Entity(ID: {self.entity_id})"
