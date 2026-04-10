# -----------------------------
# HOSPITAL MANAGEMENT SYSTEM
# -----------------------------

patients = {}

# DEFAULT DOCTORS
doctors = {
    "D1": ["Dr Ravi", "Cardiologist"],
    "D2": ["Dr Priya", "Dermatologist"],
    "D3": ["Dr Arjun", "Orthopedic"],
    "D4": ["Dr Neha", "Pediatrician"],
    "D5": ["Dr Kiran", "Neurologist"]
}

appointments = {}
bills = {}

# ID counters
p_id = 1
d_id = 6  # start from 6 because 5 doctors already exist
a_id = 1
b_id = 1

# -----------------------------
# SAFE NUMBER INPUT
# -----------------------------
def get_number(msg):
    while True:
        val = input(msg)
        try:
            return float(val)
        except:
            print("Enter valid number!")

# -----------------------------
# PATIENT MANAGEMENT
# -----------------------------
def patient_management():
    global p_id
    while True:
        print("\n--- Patient Management ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Back")

        ch = input("Enter choice: ")

        if ch == '1':
            name = input("Name: ")
            age = input("Age: ")
            gender = input("Gender: ")
            disease = input("Disease: ")

            pid = "P" + str(p_id)
            p_id += 1

            patients[pid] = [name, age, gender, disease]
            print("Patient Added! ID:", pid)

        elif ch == '2':
            if len(patients) == 0:
                print("No patients found.")
            else:
                for pid in patients:
                    print(pid, patients[pid])

        elif ch == '3':
            break

        else:
            print("Invalid choice")

# -----------------------------
# DOCTOR MANAGEMENT
# -----------------------------
def doctor_management():
    global d_id
    while True:
        print("\n--- Doctor Management ---")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Back")

        ch = input("Enter choice: ")

        if ch == '1':
            name = input("Doctor Name: ")
            spec = input("Specialization: ")

            did = "D" + str(d_id)
            d_id += 1

            doctors[did] = [name, spec]
            print("Doctor Added! ID:", did)

        elif ch == '2':
            print("\n--- Doctors List ---")
            for did in doctors:
                print(did, ":", doctors[did][0], "-", doctors[did][1])

        elif ch == '3':
            break

        else:
            print("Invalid choice")

# -----------------------------
# APPOINTMENT SCHEDULING
# -----------------------------
def appointment_scheduling():
    global a_id

    print("\n--- Appointment Scheduling ---")

    if len(patients) == 0:
        print("No patients available!")
        return

    print("\nPatients:")
    for pid in patients:
        print(pid, "-", patients[pid][0])

    pid = input("Enter Patient ID: ")
    if pid not in patients:
        print("Invalid Patient ID!")
        return

    print("\nDoctors:")
    for did in doctors:
        print(did, "-", doctors[did][0], "(", doctors[did][1], ")")

    did = input("Enter Doctor ID: ")
    if did not in doctors:
        print("Invalid Doctor ID!")
        return

    date = input("Enter Date (DD-MM-YYYY): ")
    time = input("Enter Time (HH:MM): ")

    if date == "" or time == "":
        print("Invalid Date/Time!")
        return

    aid = "A" + str(a_id)
    a_id += 1

    appointments[aid] = [pid, did, date, time]

    print("\nAppointment SUCCESSFULLY BOOKED!")
    print("Appointment ID:", aid)

# -----------------------------
# BILLING SYSTEM
# -----------------------------
def billing_system():
    global b_id

    print("\n--- Billing ---")

    if len(patients) == 0:
        print("No patients available!")
        return

    for pid in patients:
        print(pid, "-", patients[pid][0])

    pid = input("Enter Patient ID: ")
    if pid not in patients:
        print("Invalid ID!")
        return

    c = get_number("Consultation: ")
    l = get_number("Lab: ")
    r = get_number("Room: ")

    d = input("Discount % (Enter for 0): ")
    if d == "":
        d = 0
    else:
        try:
            d = float(d)
        except:
            print("Invalid discount!")
            return

    total = c + l + r
    total = total - (total * d / 100)

    bid = "B" + str(b_id)
    b_id += 1

    bills[bid] = [pid, total]

    print("\n--- RECEIPT ---")
    print("Patient:", patients[pid][0])
    print("Total Amount:", total)
    print("Bill ID:", bid)

# -----------------------------
# REPORT SUMMARY
# -----------------------------
def report_summary():
    print("\n--- REPORT SUMMARY ---")

    print("Total Patients:", len(patients))
    print("Total Appointments:", len(appointments))

    total = 0
    for b in bills:
        total += bills[b][1]

    print("Total Revenue:", total)

# -----------------------------
# MAIN MENU
# -----------------------------
while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Patient Management")
    print("2. Appointment Scheduling")
    print("3. Doctor Management")
    print("4. Billing")
    print("5. Report")
    print("6. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        patient_management()
    elif ch == '2':
        appointment_scheduling()
    elif ch == '3':
        doctor_management()
    elif ch == '4':
        billing_system()
    elif ch == '5':
        report_summary()
    elif ch == '6':
        print("Exiting System...")
        break
    else:
        print("Invalid choice")
