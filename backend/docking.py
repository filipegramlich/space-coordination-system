class DockingBay:
    def __init__(self, id):
        self.id = id
        self.occupied = False
        self.spacecraft = None

    def __repr__(self):
        return f'Dock {self.id} - Occupied: {self.occupied} - Spacecraft: {self.spacecraft}'

    def dock(self, spacecraft_data):
        self.spacecraft = spacecraft_data
        self.occupied = True
