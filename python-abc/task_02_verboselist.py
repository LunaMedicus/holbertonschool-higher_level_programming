#!/usr/bin/python3
"""Verbose list implementation with operation notifications."""


class VerboseList(list):
    """List subclass that prints messages on modifications."""

    def append(self, item):
        """Append an item and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list and print number of added items."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove an item and print a message."""
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """Pop an item and print a message."""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
