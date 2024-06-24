class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("queue is empty")
