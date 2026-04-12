#!/usr/bin/python3
"""Iterator wrapper that counts consumed items."""


class CountedIterator:
    """Wrap an iterable and count successful next calls."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return iterator instance."""
        return self

    def __next__(self):
        """Return next item and increment consumed count."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return number of iterated items."""
        return self.count
