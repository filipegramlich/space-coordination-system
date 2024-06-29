from backend.scs import SCS

def main(): 
    
    scs = SCS()
    scs.open_docks()
    
    request_data_1 = {
        'name': 'spacecraft_1',
        'type': 'A'
    }
    
    request_data_2 = {
        'name': 'spacecraft_2',
        'type': 'B'
    }
    
    if scs.verify_if_queue_is_empty():
        scs.verify_which_docking_bays_are_not_occupied(request_data_1)
        
    
if __name__ == "__main__":
    main()
