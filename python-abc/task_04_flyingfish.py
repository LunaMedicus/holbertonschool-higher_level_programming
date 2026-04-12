#!/usr/bin/python3
"""Multiple inheritance example with fish and bird classes."""


class Fish:
    """Fish behavior."""

    def swim(self):
        """Print fish swim behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird behavior."""

    def fly(self):
        """Print bird flight behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Flying fish with overridden parent behaviors."""

    def fly(self):
        """Print flying fish flight behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print flying fish swim behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
