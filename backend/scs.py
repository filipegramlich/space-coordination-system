from backend.docking import DockingBay
from backend.queue import Queue

class SCS:
    def __init__(self):
        self.queue = Queue()
        self.docking_bays = []
        self.docks_occupied = []
        self.docks_not_occupied = []
    
    def open_docks(self):
        dock_1 = DockingBay(1)
        dock_2 = DockingBay(2)
        dock_3 = DockingBay(3)
        self.docking_bays = {
                dock_1, dock_2, dock_3
            }
        return self.docking_bays
    
    def verify_if_queue_is_empty(self):
        return self.queue.is_empty()
    
    def verify_docking_bays(self):
        for dock in self.docking_bays:
            if dock.occupied == False:
                self.docks_not_occupied.append(dock)
            else:
                self.docks_not_occupied.append(dock)
        print(f'Occupied DockingBays:{self.docks_occupied}')
        print(f'Not Occupied DockingBays:{self.docks_not_occupied}')
        
    def verify_which_docking_bays_are_not_occupied(self):
        for dock in self.docking_bays:
            if dock.occupied == False:
                self.docks_not_occupied.append(dock)
        print(f'Not Occupied DockingBays:{self.docks_not_occupied}')
            
