# ==========================================
# 🩸 BLOOD BANK MANAGEMENT SYSTEM 🩸
# ==========================================

import os

# Valid Blood Groups Definition
VALID_BLOOD_GROUPS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# Initial Stock Configuration as per problem statement
# Note: Initial stock: A+ 10, B+ 5, O+ 8, AB+ 2; all other groups 0.
stock = {
    "A+": 10,
    "A-": 0,
    "B+": 5,
    "B-": 0,
    "AB+": 2,
    "AB-": 0,
    "O+": 8,
    "O-": 0
}

# Donors Data Structure
donors = []

# ------------------------------------------
# 📁 FILE HANDLING UTILITIES
# ------------------------------------------
def save_donor_to_file(name, blood_group, units):
    """Saves a donor record to donors.txt file"""
    with open("donors.txt", "a") as f:
        f.write(f"{name}, {blood_group}, {units}\n")

def load_initial_donors_for_tc4():
    """Initializes donors list for Test Case 4 as per requirements"""
    global donors
    donors = [
        {"name": "Meena Joshi", "blood_group": "O+", "units": 1},
        {"name": "Suresh Rao", "blood_group": "O+", "units": 2}
    ]
    with open("donors.txt", "w") as f:
        f.write("Meena Joshi, O+, 1\n")
        f.write("Suresh Rao, O+, 2\n")

# ------------------------------------------
# ⚙️ CORE SYSTEM FUNCTIONS
# ------------------------------------------
def add_donor():
    """Add a new donor and update stock & file"""
    print("\n--- Add Donor ---")
    name = input("Name: ").strip()
    blood_group = input("Blood group: ").strip().upper()
    
    # Validation for Blood Group
    if blood_group not in VALID_BLOOD_GROUPS:
        print(f"Invalid blood group. Valid groups: {', '.join(VALID_BLOOD_GROUPS)}")
        return

    try:
        units = int(input("Units: ").strip())
        if units <= 0:
            print("Units must be a positive integer.")
            return
    except ValueError:
        print("Invalid unit input. Please enter a number.")
        return

    # Update Stock & Donor List
    stock[blood_group] += units
    donors.append({"name": name, "blood_group": blood_group, "units": units})
    save_donor_to_file(name, blood_group, units)
    
    # Required Output Format
    print(f"Donor saved to donors.txt. Stock of {blood_group} is now {stock[blood_group]} units.")

def issue_blood():
    """Issue blood units if sufficient stock is available"""
    print("\n--- Issue Blood ---")
    blood_group = input("Blood group: ").strip().upper()
    
    # Validation for Blood Group
    if blood_group not in VALID_BLOOD_GROUPS:
        print(f"Invalid blood group. Valid groups: {', '.join(VALID_BLOOD_GROUPS)}")
        return

    try:
        units = int(input("Units: ").strip())
        if units <= 0:
            print("Units must be a positive integer.")
            return
    except ValueError:
        print("Invalid unit input. Please enter a number.")
        return

    # Check Available Stock
    available_stock = stock[blood_group]
    if units <= available_stock:
        stock[blood_group] -= units
        print(f"{units} unit(s) of {blood_group} issued. Stock of {blood_group} is now {stock[blood_group]} units.")
    else:
        print(f"Insufficient stock: only {available_stock} unit(s) of {blood_group} available.")

def view_stock():
    """Display current blood stock"""
    print("\n--- Current Stock ---")
    for group, count in stock.items():
        print(f"{group}: {count} units")

def search_donors():
    """Search and display donors by blood group"""
    print("\n--- Search Donors ---")
    blood_group = input("Blood group: ").strip().upper()
    
    matching_donors = [d for d in donors if d["blood_group"] == blood_group]
    
    if matching_donors:
        print(f"Donors with blood group {blood_group}:")
        for idx, d in enumerate(matching_donors, 1):
            print(f"{idx}. {d['name']} - {d['units']} unit(s)")
        print(f"Total donors found: {len(matching_donors)}")
    else:
        print(f"No donors found with blood group {blood_group}.")

# ------------------------------------------
# 🚀 MAIN APPLICATION MENU
# ------------------------------------------
def main():
    while True:
        print("\n==========================================")
        print("   BLOOD BANK MANAGEMENT SYSTEM MENU")
        print("==========================================")
        print("1. Add donor")
        print("2. Issue blood")
        print("3. View stock")
        print("4. Search donors")
        print("5. Setup Initial Data for TC4 (Optional)")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            add_donor()
        elif choice == '2':
            issue_blood()
        elif choice == '3':
            view_stock()
        elif choice == '4':
            search_donors()
        elif choice == '5':
            load_initial_donors_for_tc4()
            print("Initial donor data for Test Case 4 loaded successfully!")
        elif choice == '6':
            print("Exiting application. Thank you!")
            break
        else:
            print("Invalid choice! Please select between 1 and 6.")

if __name__ == "__main__":
    main()
