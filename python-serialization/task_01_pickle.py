#!/usr/bin/python3
"""Pickle serialization for a custom class."""
import pickle


class CustomObject:
    """Represent a custom serializable object."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to a file."""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a file."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except (FileNotFoundError, EOFError, pickle.PickleError):
            return None
        except AttributeError:
            return None
        return None
