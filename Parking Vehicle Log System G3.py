from datetime import datetime
from zoneinfo import ZoneInfo  

LOCAL_TIMEZONE = ZoneInfo("Asia/Manila") 

parking_log = []

def log_vehicle_in():
    plate = input("Enter vehicle plate number: ").strip().upper()
    
    if not plate:
        print("Plate number cannot be empty.")
        return

    # Prevent double parking
    for r in parking_log:
        if r["plate"] == plate and r["time_out"] is None:
            print(f"Vehicle {plate} is already parked!")
            return

    time_in = datetime.now(LOCAL_TIMEZONE)
    record = {
        "plate": plate,
        "time_in": time_in,
        "time_out": None
    }
    parking_log.append(record)
    print(f"Vehicle {plate} logged in at {time_in.strftime('%Y-%m-%d %H:%M:%S')}")

def log_vehicle_out():
    plate = input("Enter vehicle plate number: ").strip().upper()
    
    if not plate:
        print("Plate number cannot be empty.")
        return

    for r in parking_log:
        if r["plate"] == plate and r["time_out"] is None:
            r["time_out"] = datetime.now(LOCAL_TIMEZONE)
            print(f"Vehicle {plate} logged out at {r['time_out'].strftime('%Y-%m-%d %H:%M:%S')}")
            return
    
    print(f"No active record found for vehicle: {plate}.")

def view_vehicle_list():
    current_vehicles = [r for r in parking_log if r["time_out"] is None]
    
    print("=== CURRENT VEHICLES IN PARKING ===")
    if not current_vehicles:
        print("No Current Vehicle Parked.")
        return
    
    for r in current_vehicles:
        print(f"{r['plate']} | Time In: {r['time_in'].strftime('%Y-%m-%d %H:%M:%S')}")
    print()

def generate_report():
    print("=== PARKING REPORT ===")
    if not parking_log:
        print("No car record found.")
        return

    for r in parking_log:
        time_in = r["time_in"].strftime('%Y-%m-%d %H:%M:%S')
        time_out = r["time_out"].strftime('%Y-%m-%d %H:%M:%S') if r["time_out"] else "Still Parked"
        print(f"{r['plate']} | In: {time_in} | Out: {time_out}")
    print()

def attendant_menu():
    while True:
        print("=== PARKING ATTENDANT MENU ===")
        print("1. Log Vehicle In")
        print("2. Log Vehicle Out")
        print("3. Back to Main Menu")
        c = input("Select your choice: ")
        
        if c == '1':
            log_vehicle_in()
        elif c == '2':
            log_vehicle_out()
        elif c == '3':
            break
        else:
            print("Invalid input.")

def supervisor_menu():
    while True:
        print("=== SECURITY SUPERVISOR MENU ===")
        print("1. View Current Vehicles")
        print("2. Generate Parking Report")
        print("3. Back to Main Menu")
        c = input("Enter your choice: ")
        
        if c == '1':
            view_vehicle_list()
        elif c == '2':
            generate_report()
        elif c == '3':
            break
        else:
            print("Invalid input.")

def main():
    while True:
        print("=== VEHICLE PARKING LOG SYSTEM ===")
        print("1. Parking Attendant")
        print("2. Security Supervisor")
        print("3. Exit")

        role = input("Select your role (1-3): ")

        if role == '1':
            attendant_menu()
        elif role == '2':
            supervisor_menu()
        elif role == '3':
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid option.")

# Run the system
main()
