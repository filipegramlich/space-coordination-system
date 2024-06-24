from backend.scs import SCS

# 1 - SCS will receive a request
# 2 - SCS will verify if the queue is empty
# if queue == empty, can add the data to one of the docking bays.
# else add to end of the queue

def main(): 
    
    scs = SCS()
    scs.open_docks()
    
    if scs.verify_if_queue_is_empty():
        scs.verify_which_docking_bays_are_not_occupied()
        
    
if __name__ == "__main__":
    main()
