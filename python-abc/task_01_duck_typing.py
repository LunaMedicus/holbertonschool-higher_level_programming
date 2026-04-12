#!/usr/bin/python3
"""Shapes example using abstract classes and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract shape interface."""

    @abstractmethod
    def area(self):
        """Return area of the shape."""

    @abstractmethod
    def perimeter(self):
        """Return perimeter of the shape."""


class Circle(Shape):
    """Circle implementation of Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle implementation of Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter for any shape-like object."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
