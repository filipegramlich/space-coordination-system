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
    
    def verify_which_docking_bays_are_not_occupied(self):
        for dock in self.docking_bays:
            if dock.occupied == False:
                self.docks_not_occupied.append(dock)
            else:
                self.docks_occupied.append(dock)
        return self.docks_not_occupied
    
    def direct_spacecraft_to_free_dock(self, free_dock, spacecraft_data):
        free_dock.dock(spacecraft_data)
        self.docks_not_occupied.remove(free_dock)
        self.docks_occupied.append(free_dock)
        
        print(self.docks_not_occupied)
        print(self.docks_occupied)         
    
        
            
    
            
        
                
            
