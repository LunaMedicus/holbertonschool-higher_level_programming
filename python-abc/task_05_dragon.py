#!/usr/bin/python3
"""Mixins example demonstrating composed behaviors."""


class SwimMixin:
    """Add swim behavior."""

    def swim(self):
        """Print swim behavior."""
        print("The creature swims!")


class FlyMixin:
    """Add fly behavior."""

    def fly(self):
        """Print fly behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon composed from swim and fly mixins."""

    def roar(self):
        """Print dragon roar behavior."""
        print("The dragon roars!")
