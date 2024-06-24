class DockingBay:
    def __init__(self, id):
        self.id = id
        self.occupied = False

    def __repr__(self):
        return f"DockingBay {self.id}"

