#!/usr/bin/python3
"""Abstract Animal class and concrete subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Blueprint for animals that can make a sound."""

    @abstractmethod
    def sound(self):
        """Return the sound this animal makes."""


class Dog(Animal):
    """Dog implementation of Animal."""

    def sound(self):
        """Return the dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat implementation of Animal."""

    def sound(self):
        """Return the cat sound."""
        return "Meow"
