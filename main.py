from scs import SCS

def main():
    scs = SCS()

    while True:
        try:
            print('Welcome to SCS system')
            selected_option = int(input("Options -> 1 to verify docking_bays, 2 to add a new docking_bay (or '0' to exit): "))
            if selected_option == 0:
                break 
            elif selected_option == 1:
                scs.verify_docking_bays()
            elif selected_option == 2:
                dock_id = int(input("Enter the ID of the new DockingBay: "))
                scs.add_docking_bay(dock_id)
        except ValueError:
            print("Please enter a valid integer number.")
main()
