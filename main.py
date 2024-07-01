from backend.scs import SCS

def main(): 
    
    scs = SCS()
    scs.open_docks()
    
    request_data_1 = {
        'name': 'spacecraft_1',
        'type': 'A'
    }
    
    if scs.verify_if_queue_is_empty():
        scs.verify_which_docking_bays_are_not_occupied()
        if len(scs.docks_not_occupied) > 0:
            first_free_docking_bay = scs.docks_not_occupied[0]
            scs.direct_spacecraft_to_free_dock(first_free_docking_bay, request_data_1)
        else:
            print('All docking_bays are occupied.')

if __name__ == "__main__":
    main()
