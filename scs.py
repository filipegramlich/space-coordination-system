from docking import DockingBay

class SCS:
    def __init__(self):
        self.docking_bays = {}
    
    def verify_docking_bays(self):
        print(self.docking_bays)
        
    def add_docking_bay(self, id):
        print(self.docking_bays)
        if id not in self.docking_bays:
            self.docking_bays[id] = DockingBay(id)
            print(f"New DockingBay was added: {id}.")
        else:
            print(f"DockingBay {id} already exists.")