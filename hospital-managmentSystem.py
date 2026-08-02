# ==========================================================
#                 MASS HOSPITAL MANAGEMENT SYSTEM
# ==========================================================
# Hospital Name : MASS Hospital
# Developed Using:
# Classes & Objects
# Inheritance
# Encapsulation
# Association
# Aggregation
# Composition
# Polymorphism
# ==========================================================

# import os


# ==========================================================
# PERSON CLASS (Parent Class)
# ==========================================================

class Person:

    def __init__(self, pid, name, age, gender, contact):
        self._id = pid
        self._name = name
        self._age = age
        self._gender = gender
        self._contact = contact

    def display(self):
        print("--------------------------------")
        print("ID       :", self._id)
        print("Name     :", self._name)
        print("Age      :", self._age)
        print("Gender   :", self._gender)
        print("Contact  :", self._contact)


# ==========================================================
# PATIENT CLASS
# (Inheritance + Encapsulation)
# ==========================================================

class Patient(Person):

    def __init__(self, pid, name, age, gender, contact,
                 disease, blood_group):

        super().__init__(pid, name, age, gender, contact)

        self.__disease = disease
        self.__blood_group = blood_group
        self.__history = []

        self.doctor = None
        self.ward = None
        self.status = "Not Admitted"

    # Encapsulation
    def set_disease(self, disease):
        self.__disease = disease

    def get_disease(self):
        return self.__disease

    def set_blood_group(self, group):
        self.__blood_group = group

    def get_blood_group(self):
        return self.__blood_group

    def add_history(self, text):
        self.__history.append(text)

    def get_history(self):
        return self.__history

    # Polymorphism
    def display(self):

        print("\n========== PATIENT ==========")

        super().display()

        print("Disease      :", self.__disease)
        print("Blood Group  :", self.__blood_group)
        print("Status       :", self.status)

        if self.doctor is None:
            print("Doctor       : Not Assigned")
        else:
            print("Doctor       :", self.doctor._name)

        if self.ward is None:
            print("Ward         : Not Assigned")
        else:
            print("Ward         :", self.ward.name)


# ==========================================================
# DOCTOR CLASS
# (Inheritance + Encapsulation)
# ==========================================================

class Doctor(Person):

    def __init__(self,
                 did,
                 name,
                 age,
                 gender,
                 contact,
                 specialization,
                 experience,
                 salary):

        super().__init__(did,
                         name,
                         age,
                         gender,
                         contact)

        self.specialization = specialization
        self.experience = experience

        self.__salary = salary

        self.patients = []

    # Encapsulation

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def assign_patient(self, patient):

        self.patients.append(patient)
        patient.doctor = self

    # Polymorphism
    def display(self):

        print("\n========== DOCTOR ==========")

        super().display()

        print("Specialization :", self.specialization)
        print("Experience     :", self.experience)
        print("Salary         :", self.__salary)
        print("Patients       :", len(self.patients))


# ==========================================================
# STAFF CLASS
# (Inheritance)
# ==========================================================

class Staff(Person):

    def __init__(self,
                 sid,
                 name,
                 age,
                 gender,
                 contact,
                 position,
                 department,
                 salary):

        super().__init__(sid,
                         name,
                         age,
                         gender,
                         contact)

        self.position = position
        self.department = department
        self.salary = salary

    # Polymorphism
    def display(self):

        print("\n========== STAFF ==========")

        super().display()

        print("Position    :", self.position)
        print("Department  :", self.department)
        print("Salary      :", self.salary)

# ==========================================================
# APPOINTMENT CLASS
# (Association)
# ==========================================================

class Appointment:

    def __init__(self,
                 appointment_id,
                 patient,
                 doctor,
                 date,
                 time):

        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = "Booked"

    def cancel(self):
        self.status = "Cancelled"

    def reschedule(self, new_date, new_time):
        self.date = new_date
        self.time = new_time

    def display(self):

        print("\n========== APPOINTMENT ==========")

        print("Appointment ID :", self.appointment_id)
        print("Patient        :", self.patient._name)
        print("Doctor         :", self.doctor._name)
        print("Date           :", self.date)
        print("Time           :", self.time)
        print("Status         :", self.status)


# ==========================================================
# WARD CLASS
# (Aggregation)
# ==========================================================

class Ward:

    def __init__(self,
                 ward_id,
                 name,
                 capacity):

        self.ward_id = ward_id
        self.name = name
        self.capacity = capacity
        self.patients = []

    def add_patient(self, patient):

        if len(self.patients) < self.capacity:

            self.patients.append(patient)

            patient.ward = self
            patient.status = "Admitted"

            print("Patient admitted successfully.")

        else:

            print("Ward is Full.")

    def remove_patient(self, patient):

        if patient in self.patients:

            self.patients.remove(patient)

            patient.ward = None
            patient.status = "Discharged"

            print("Patient discharged successfully.")

        else:

            print("Patient not found.")

    def available_beds(self):

        return self.capacity - len(self.patients)

    def display(self):

        print("\n========== WARD ==========")

        print("Ward ID        :", self.ward_id)
        print("Ward Name      :", self.name)
        print("Capacity       :", self.capacity)
        print("Occupied Beds  :", len(self.patients))
        print("Available Beds :", self.available_beds())


# ==========================================================
# MEDICINE CLASS
# (Encapsulation)
# ==========================================================

class Medicine:

    def __init__(self,
                 medicine_id,
                 name,
                 company,
                 price,
                 stock,
                 expiry_date):

        self.medicine_id = medicine_id
        self.name = name
        self.company = company
        self.price = price

        self.__stock = stock

        self.expiry_date = expiry_date

    # Encapsulation

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        self.__stock = stock

    def issue(self, quantity):

        if quantity <= self.__stock:

            self.__stock -= quantity

            return True

        return False

    def display(self):

        print("\n========== MEDICINE ==========")

        print("Medicine ID :", self.medicine_id)
        print("Name        :", self.name)
        print("Company     :", self.company)
        print("Price       :", self.price)
        print("Stock       :", self.__stock)
        print("Expiry Date :", self.expiry_date)


# ==========================================================
# PHARMACY CLASS
# (Composition)
# ==========================================================

class Pharmacy:

    def __init__(self):

        self.medicines = []

    def add_medicine(self, medicine):

        self.medicines.append(medicine)

        print("Medicine Added Successfully.")

    def search_medicine(self, medicine_id):

        for medicine in self.medicines:

            if medicine.medicine_id == medicine_id:
                return medicine

        return None

    def delete_medicine(self, medicine_id):

        medicine = self.search_medicine(medicine_id)

        if medicine:

            self.medicines.remove(medicine)

            print("Medicine Deleted Successfully.")

        else:

            print("Medicine Not Found.")

    def update_stock(self,
                     medicine_id,
                     stock):

        medicine = self.search_medicine(medicine_id)

        if medicine:

            medicine.set_stock(stock)

            print("Stock Updated Successfully.")

        else:

            print("Medicine Not Found.")

    def issue_medicine(self,
                       medicine_id,
                       quantity):

        medicine = self.search_medicine(medicine_id)

        if medicine:

            if medicine.issue(quantity):

                total = quantity * medicine.price

                print("Medicine Issued Successfully.")
                print("Quantity :", quantity)
                print("Total Bill :", total)

            else:

                print("Insufficient Stock.")

        else:

            print("Medicine Not Found.")

    def display_all(self):

        if len(self.medicines) == 0:

            print("\nNo Medicines Available.")

        else:

            for medicine in self.medicines:

                medicine.display()

# ==========================================================
# LAB REPORT CLASS
# ==========================================================

class LabReport:

    def __init__(self,
                 report_id,
                 patient,
                 test_name,
                 result,
                 charges):

        self.report_id = report_id
        self.patient = patient
        self.test_name = test_name
        self.result = result
        self.charges = charges

    def display(self):

        print("\n========== LAB REPORT ==========")

        print("Report ID :", self.report_id)
        print("Patient   :", self.patient._name)
        print("Test Name :", self.test_name)
        print("Result    :", self.result)
        print("Charges   :", self.charges)


# ==========================================================
# LABORATORY CLASS
# (Composition)
# ==========================================================

class Laboratory:

    def __init__(self):

        self.reports = []

    def add_report(self, report):

        self.reports.append(report)

        print("Lab Report Added Successfully.")

    def search_report(self, report_id):

        for report in self.reports:

            if report.report_id == report_id:
                return report

        return None

    def display_reports(self):

        if len(self.reports) == 0:

            print("\nNo Lab Reports Available.")

        else:

            for report in self.reports:

                report.display()


# ==========================================================
# BILL CLASS
# (Composition)
# ==========================================================

class Bill:

    def __init__(self,
                 bill_id,
                 patient,
                 doctor_fee,
                 lab_fee,
                 medicine_fee,
                 ward_fee):

        self.bill_id = bill_id
        self.patient = patient

        self.doctor_fee = doctor_fee
        self.lab_fee = lab_fee
        self.medicine_fee = medicine_fee
        self.ward_fee = ward_fee

        self.total_bill = 0

        self.calculate_total()

    def calculate_total(self):

        self.total_bill = (
            self.doctor_fee +
            self.lab_fee +
            self.medicine_fee +
            self.ward_fee
        )

    def display(self):

        print("\n========== BILL ==========")

        print("Bill ID        :", self.bill_id)
        print("Patient        :", self.patient._name)
        print("Doctor Fee     :", self.doctor_fee)
        print("Lab Charges    :", self.lab_fee)
        print("Medicine Bill  :", self.medicine_fee)
        print("Ward Charges   :", self.ward_fee)
        print("----------------------------")
        print("Total Bill     :", self.total_bill)


# ==========================================================
# HOSPITAL CLASS
# ==========================================================

class Hospital:

    def __init__(self):

        self.name = "MASS Hospital"

        self.patients = []

        self.doctors = []

        self.staff = []

        self.appointments = []

        self.wards = []

        self.bills = []

        self.pharmacy = Pharmacy()

        self.laboratory = Laboratory()


# ==========================================================
# PATIENT SEARCH
# ==========================================================

    def search_patient(self, patient_id):

        for patient in self.patients:

            if patient._id == patient_id:
                return patient

        return None


# ==========================================================
# DOCTOR SEARCH
# ==========================================================

    def search_doctor(self, doctor_id):

        for doctor in self.doctors:

            if doctor._id == doctor_id:
                return doctor

        return None


# ==========================================================
# STAFF SEARCH
# ==========================================================

    def search_staff(self, staff_id):

        for staff in self.staff:

            if staff._id == staff_id:
                return staff

        return None


# ==========================================================
# APPOINTMENT SEARCH
# ==========================================================

    def search_appointment(self, appointment_id):

        for appointment in self.appointments:

            if appointment.appointment_id == appointment_id:
                return appointment

        return None


# ==========================================================
# WARD SEARCH
# ==========================================================

    def search_ward(self, ward_id):

        for ward in self.wards:

            if ward.ward_id == ward_id:
                return ward

        return None


# ==========================================================
# BILL SEARCH
# ==========================================================

    def search_bill(self, bill_id):

        for bill in self.bills:

            if bill.bill_id == bill_id:
                return bill

        return None

# ==========================================================
# ADD PATIENT
# ==========================================================

    def add_patient(self):

        print("\n========== ADD PATIENT ==========")

        pid = input("Enter Patient ID : ")

        if self.search_patient(pid):

            print("Patient ID Already Exists.")
            return

        name = input("Enter Name : ")

        age = input("Enter Age : ")

        gender = input("Enter Gender : ")

        contact = input("Enter Contact : ")

        disease = input("Enter Disease : ")

        blood_group = input("Enter Blood Group : ")

        patient = Patient(
            pid,
            name,
            age,
            gender,
            contact,
            disease,
            blood_group
        )

        self.patients.append(patient)

        print("\nPatient Added Successfully.")


# ==========================================================
# VIEW ALL PATIENTS
# ==========================================================

    def view_patients(self):

        print("\n========== PATIENT LIST ==========")

        if len(self.patients) == 0:

            print("No Patients Found.")
            return

        for patient in self.patients:

            patient.display()

            print("--------------------------------")


# ==========================================================
# SEARCH PATIENT
# ==========================================================

    def search_patient_menu(self):

        print("\n========== SEARCH PATIENT ==========")

        pid = input("Enter Patient ID : ")

        patient = self.search_patient(pid)

        if patient:

            patient.display()

        else:

            print("Patient Not Found.")

# ==========================================================
# UPDATE PATIENT
# ==========================================================

    def update_patient(self):

        print("\n========== UPDATE PATIENT ==========")

        pid = input("Enter Patient ID : ")

        patient = self.search_patient(pid)

        if patient is None:

            print("Patient Not Found.")
            return

        patient._name = input("Enter New Name : ")
        patient._age = input("Enter New Age : ")
        patient._gender = input("Enter New Gender : ")
        patient._contact = input("Enter New Contact : ")

        disease = input("Enter New Disease : ")
        blood_group = input("Enter New Blood Group : ")

        patient.set_disease(disease)
        patient.set_blood_group(blood_group)

        print("Patient Updated Successfully.")


# ==========================================================
# DELETE PATIENT
# ==========================================================

    def delete_patient(self):

        print("\n========== DELETE PATIENT ==========")

        pid = input("Enter Patient ID : ")

        patient = self.search_patient(pid)

        if patient is None:

            print("Patient Not Found.")
            return

        self.patients.remove(patient)

        print("Patient Deleted Successfully.")


# ==========================================================
# ADMIT PATIENT
# ==========================================================

    def admit_patient(self):

        print("\n========== ADMIT PATIENT ==========")

        pid = input("Enter Patient ID : ")

        patient = self.search_patient(pid)

        if patient is None:

            print("Patient Not Found.")
            return

        ward_id = input("Enter Ward ID : ")

        ward = self.search_ward(ward_id)

        if ward is None:

            print("Ward Not Found.")
            return

        ward.add_patient(patient)

        patient.add_history("Patient Admitted")


# ==========================================================
# DISCHARGE PATIENT
# ==========================================================

    def discharge_patient(self):

        print("\n========== DISCHARGE PATIENT ==========")

        pid = input("Enter Patient ID : ")

        patient = self.search_patient(pid)

        if patient is None:

            print("Patient Not Found.")
            return

        if patient.ward is None:

            print("Patient is not admitted.")
            return

        patient.ward.remove_patient(patient)

        patient.add_history("Patient Discharged")


# ==========================================================
# PATIENT MANAGEMENT MENU
# ==========================================================

    def patient_menu(self):

        while True:

            print("\n===================================")
            print("      PATIENT MANAGEMENT")
            print("===================================")

            print("1. Add Patient")
            print("2. View Patients")
            print("3. Search Patient")
            print("4. Update Patient")
            print("5. Delete Patient")
            print("6. Admit Patient")
            print("7. Discharge Patient")
            print("8. Back")

            choice = input("Enter Choice : ")

            if choice == "1":

                self.add_patient()

            elif choice == "2":

                self.view_patients()

            elif choice == "3":

                self.search_patient_menu()

            elif choice == "4":

                self.update_patient()

            elif choice == "5":

                self.delete_patient()

            elif choice == "6":

                self.admit_patient()

            elif choice == "7":

                self.discharge_patient()

            elif choice == "8":

                break

            else:

                print("Invalid Choice.")


# ==========================================================
# ADD DOCTOR
# ==========================================================

    def add_doctor(self):

        print("\n========== ADD DOCTOR ==========")

        did = input("Enter Doctor ID : ")

        if self.search_doctor(did):

            print("Doctor ID Already Exists.")
            return

        name = input("Enter Name : ")

        age = input("Enter Age : ")

        gender = input("Enter Gender : ")

        contact = input("Enter Contact : ")

        specialization = input("Enter Specialization : ")

        experience = input("Enter Experience (Years) : ")

        salary = input("Enter Salary : ")

        doctor = Doctor(
            did,
            name,
            age,
            gender,
            contact,
            specialization,
            experience,
            salary
        )

        self.doctors.append(doctor)

        print("\nDoctor Added Successfully.")


# ==========================================================
# VIEW ALL DOCTORS
# ==========================================================

    def view_doctors(self):

        print("\n========== DOCTOR LIST ==========")

        if len(self.doctors) == 0:

            print("No Doctors Found.")
            return

        for doctor in self.doctors:

            doctor.display()

            print("--------------------------------")


# ==========================================================
# SEARCH DOCTOR
# ==========================================================

    def search_doctor_menu(self):

        print("\n========== SEARCH DOCTOR ==========")

        did = input("Enter Doctor ID : ")

        doctor = self.search_doctor(did)

        if doctor:

            doctor.display()

        else:

            print("Doctor Not Found.")

# ==========================================================
# UPDATE DOCTOR
# ==========================================================

    def update_doctor(self):

        print("\n========== UPDATE DOCTOR ==========")

        did = input("Enter Doctor ID : ")

        doctor = self.search_doctor(did)

        if doctor is None:

            print("Doctor Not Found.")
            return

        doctor._name = input("Enter New Name : ")
        doctor._age = input("Enter New Age : ")
        doctor._gender = input("Enter New Gender : ")
        doctor._contact = input("Enter New Contact : ")

        doctor.specialization = input("Enter New Specialization : ")
        doctor.experience = input("Enter New Experience : ")

        salary = input("Enter New Salary : ")
        doctor.set_salary(salary)

        print("Doctor Updated Successfully.")


# ==========================================================
# DELETE DOCTOR
# ==========================================================

    def delete_doctor(self):

        print("\n========== DELETE DOCTOR ==========")

        did = input("Enter Doctor ID : ")

        doctor = self.search_doctor(did)

        if doctor is None:

            print("Doctor Not Found.")
            return

        self.doctors.remove(doctor)

        print("Doctor Deleted Successfully.")


# ==========================================================
# ASSIGN PATIENT TO DOCTOR
# (Association)
# ==========================================================

    def assign_patient_to_doctor(self):

        print("\n========== ASSIGN PATIENT ==========")

        pid = input("Enter Patient ID : ")

        patient = self.search_patient(pid)

        if patient is None:

            print("Patient Not Found.")
            return

        did = input("Enter Doctor ID : ")

        doctor = self.search_doctor(did)

        if doctor is None:

            print("Doctor Not Found.")
            return

        doctor.assign_patient(patient)

        patient.add_history("Assigned to Doctor : " + doctor._name)

        print("Patient Assigned Successfully.")


# ==========================================================
# DOCTOR MANAGEMENT MENU
# ==========================================================

    def doctor_menu(self):

        while True:

            print("\n===================================")
            print("       DOCTOR MANAGEMENT")
            print("===================================")

            print("1. Add Doctor")
            print("2. View Doctors")
            print("3. Search Doctor")
            print("4. Update Doctor")
            print("5. Delete Doctor")
            print("6. Assign Patient")
            print("7. Back")

            choice = input("Enter Choice : ")

            if choice == "1":

                self.add_doctor()

            elif choice == "2":

                self.view_doctors()

            elif choice == "3":

                self.search_doctor_menu()

            elif choice == "4":

                self.update_doctor()

            elif choice == "5":

                self.delete_doctor()

            elif choice == "6":

                self.assign_patient_to_doctor()

            elif choice == "7":

                break

            else:

                print("Invalid Choice.")


# ==========================================================
# ADD STAFF
# ==========================================================

    def add_staff(self):

        print("\n========== ADD STAFF ==========")

        sid = input("Enter Staff ID : ")

        if self.search_staff(sid):

            print("Staff ID Already Exists.")
            return

        name = input("Enter Name : ")
        age = input("Enter Age : ")
        gender = input("Enter Gender : ")
        contact = input("Enter Contact : ")

        position = input("Enter Position : ")
        department = input("Enter Department : ")
        salary = input("Enter Salary : ")

        staff = Staff(
            sid,
            name,
            age,
            gender,
            contact,
            position,
            department,
            salary
        )

        self.staff.append(staff)

        print("Staff Added Successfully.")


# ==========================================================
# VIEW STAFF
# ==========================================================

    def view_staff(self):

        print("\n========== STAFF LIST ==========")

        if len(self.staff) == 0:

            print("No Staff Found.")
            return

        for staff in self.staff:

            staff.display()

            print("--------------------------------")


# ==========================================================
# SEARCH STAFF
# ==========================================================

    def search_staff_menu(self):

        print("\n========== SEARCH STAFF ==========")

        sid = input("Enter Staff ID : ")

        staff = self.search_staff(sid)

        if staff:

            staff.display()

        else:

            print("Staff Not Found.")


# ==========================================================
# UPDATE STAFF
# ==========================================================

    def update_staff(self):

        print("\n========== UPDATE STAFF ==========")

        sid = input("Enter Staff ID : ")

        staff = self.search_staff(sid)

        if staff is None:

            print("Staff Not Found.")
            return

        staff._name = input("Enter New Name : ")
        staff._age = input("Enter New Age : ")
        staff._gender = input("Enter New Gender : ")
        staff._contact = input("Enter New Contact : ")

        staff.position = input("Enter New Position : ")
        staff.department = input("Enter New Department : ")
        staff.salary = input("Enter New Salary : ")

        print("Staff Updated Successfully.")


# ==========================================================
# DELETE STAFF
# ==========================================================

    def delete_staff(self):

        print("\n========== DELETE STAFF ==========")

        sid = input("Enter Staff ID : ")

        staff = self.search_staff(sid)

        if staff is None:

            print("Staff Not Found.")
            return

        self.staff.remove(staff)

        print("Staff Deleted Successfully.")


# ==========================================================
# STAFF MANAGEMENT MENU
# ==========================================================

    def staff_menu(self):

        while True:

            print("\n===================================")
            print("        STAFF MANAGEMENT")
            print("===================================")

            print("1. Add Staff")
            print("2. View Staff")
            print("3. Search Staff")
            print("4. Update Staff")
            print("5. Delete Staff")
            print("6. Back")

            choice = input("Enter Choice : ")

            if choice == "1":

                self.add_staff()

            elif choice == "2":

                self.view_staff()

            elif choice == "3":

                self.search_staff_menu()

            elif choice == "4":

                self.update_staff()

            elif choice == "5":

                self.delete_staff()

            elif choice == "6":

                break

            else:

                print("Invalid Choice.")

# ==========================================================
# BOOK APPOINTMENT
# ==========================================================

    def book_appointment(self):

        print("\n========== BOOK APPOINTMENT ==========")

        appointment_id = input("Enter Appointment ID : ")

        if self.search_appointment(appointment_id):

            print("Appointment ID Already Exists.")
            return

        patient_id = input("Enter Patient ID : ")

        patient = self.search_patient(patient_id)

        if patient is None:

            print("Patient Not Found.")
            return

        doctor_id = input("Enter Doctor ID : ")

        doctor = self.search_doctor(doctor_id)

        if doctor is None:

            print("Doctor Not Found.")
            return

        date = input("Enter Appointment Date : ")
        time = input("Enter Appointment Time : ")

        appointment = Appointment(
            appointment_id,
            patient,
            doctor,
            date,
            time
        )

        self.appointments.append(appointment)

        print("Appointment Booked Successfully.")


# ==========================================================
# VIEW APPOINTMENTS
# ==========================================================

    def view_appointments(self):

        print("\n========== APPOINTMENT LIST ==========")

        if len(self.appointments) == 0:

            print("No Appointments Found.")
            return

        for appointment in self.appointments:

            appointment.display()

            print("--------------------------------")


# ==========================================================
# SEARCH APPOINTMENT
# ==========================================================

    def search_appointment_menu(self):

        print("\n========== SEARCH APPOINTMENT ==========")

        appointment_id = input("Enter Appointment ID : ")

        appointment = self.search_appointment(appointment_id)

        if appointment:

            appointment.display()

        else:

            print("Appointment Not Found.")


# ==========================================================
# CANCEL APPOINTMENT
# ==========================================================

    def cancel_appointment(self):

        print("\n========== CANCEL APPOINTMENT ==========")

        appointment_id = input("Enter Appointment ID : ")

        appointment = self.search_appointment(appointment_id)

        if appointment is None:

            print("Appointment Not Found.")
            return

        appointment.cancel()

        print("Appointment Cancelled Successfully.")


# ==========================================================
# RESCHEDULE APPOINTMENT
# ==========================================================

    def reschedule_appointment(self):

        print("\n========== RESCHEDULE APPOINTMENT ==========")

        appointment_id = input("Enter Appointment ID : ")

        appointment = self.search_appointment(appointment_id)

        if appointment is None:

            print("Appointment Not Found.")
            return

        new_date = input("Enter New Date : ")
        new_time = input("Enter New Time : ")

        appointment.reschedule(new_date, new_time)

        print("Appointment Rescheduled Successfully.")


# ==========================================================
# APPOINTMENT MANAGEMENT MENU
# ==========================================================

    def appointment_menu(self):

        while True:

            print("\n===================================")
            print("    APPOINTMENT MANAGEMENT")
            print("===================================")

            print("1. Book Appointment")
            print("2. View Appointments")
            print("3. Search Appointment")
            print("4. Cancel Appointment")
            print("5. Reschedule Appointment")
            print("6. Back")

            choice = input("Enter Choice : ")

            if choice == "1":

                self.book_appointment()

            elif choice == "2":

                self.view_appointments()

            elif choice == "3":

                self.search_appointment_menu()

            elif choice == "4":

                self.cancel_appointment()

            elif choice == "5":

                self.reschedule_appointment()

            elif choice == "6":

                break

            else:

                print("Invalid Choice.")

# ==========================================================
# ADD WARD
# ==========================================================

    def add_ward(self):

        print("\n========== ADD WARD ==========")

        ward_id = input("Enter Ward ID : ")

        if self.search_ward(ward_id):

            print("Ward ID Already Exists.")
            return

        name = input("Enter Ward Name : ")

        capacity = int(input("Enter Ward Capacity : "))

        ward = Ward(
            ward_id,
            name,
            capacity
        )

        self.wards.append(ward)

        print("Ward Added Successfully.")


# ==========================================================
# VIEW WARDS
# ==========================================================

    def view_wards(self):

        print("\n========== WARD LIST ==========")

        if len(self.wards) == 0:

            print("No Wards Found.")
            return

        for ward in self.wards:

            ward.display()

            print("Patients :", len(ward.patients))

            if len(ward.patients) != 0:

                print("\nPatient List")

                for patient in ward.patients:

                    print(patient._id, "-", patient._name)

            print("--------------------------------")


# ==========================================================
# SEARCH WARD
# ==========================================================

    def search_ward_menu(self):

        print("\n========== SEARCH WARD ==========")

        ward_id = input("Enter Ward ID : ")

        ward = self.search_ward(ward_id)

        if ward:

            ward.display()

            if len(ward.patients) != 0:

                print("\nPatients")

                for patient in ward.patients:

                    print(patient._id, "-", patient._name)

        else:

            print("Ward Not Found.")


# ==========================================================
# ASSIGN PATIENT TO WARD
# ==========================================================

    def assign_patient_to_ward(self):

        print("\n========== ASSIGN PATIENT TO WARD ==========")

        patient_id = input("Enter Patient ID : ")

        patient = self.search_patient(patient_id)

        if patient is None:

            print("Patient Not Found.")
            return

        ward_id = input("Enter Ward ID : ")

        ward = self.search_ward(ward_id)

        if ward is None:

            print("Ward Not Found.")
            return

        ward.add_patient(patient)

        patient.add_history("Assigned to Ward : " + ward.name)


# ==========================================================
# REMOVE PATIENT FROM WARD
# ==========================================================

    def remove_patient_from_ward(self):

        print("\n========== REMOVE PATIENT FROM WARD ==========")

        patient_id = input("Enter Patient ID : ")

        patient = self.search_patient(patient_id)

        if patient is None:

            print("Patient Not Found.")
            return

        if patient.ward is None:

            print("Patient is not assigned to any ward.")
            return

        patient.ward.remove_patient(patient)

        patient.add_history("Removed from Ward")


# ==========================================================
# WARD MANAGEMENT MENU
# ==========================================================

    def ward_menu(self):

        while True:

            print("\n===================================")
            print("         WARD MANAGEMENT")
            print("===================================")

            print("1. Add Ward")
            print("2. View Wards")
            print("3. Search Ward")
            print("4. Assign Patient to Ward")
            print("5. Remove Patient from Ward")
            print("6. Back")

            choice = input("Enter Choice : ")

            if choice == "1":

                self.add_ward()

            elif choice == "2":

                self.view_wards()

            elif choice == "3":

                self.search_ward_menu()

            elif choice == "4":

                self.assign_patient_to_ward()

            elif choice == "5":

                self.remove_patient_from_ward()

            elif choice == "6":

                break

            else:

                print("Invalid Choice.")

# ==========================================================
# ADD LAB REPORT
# ==========================================================

    def add_lab_report(self):

        print("\n========== ADD LAB REPORT ==========")

        report_id = input("Enter Report ID : ")

        if self.laboratory.search_report(report_id):

            print("Report ID Already Exists.")
            return

        patient_id = input("Enter Patient ID : ")

        patient = self.search_patient(patient_id)

        if patient is None:

            print("Patient Not Found.")
            return

        test_name = input("Enter Test Name : ")

        result = input("Enter Test Result : ")

        charges = float(input("Enter Test Charges : "))

        report = LabReport(
            report_id,
            patient,
            test_name,
            result,
            charges
        )

        self.laboratory.add_report(report)

        patient.add_history("Lab Test : " + test_name)

        print("Lab Report Added Successfully.")


# ==========================================================
# VIEW LAB REPORTS
# ==========================================================

    def view_lab_reports(self):

        print("\n========== LAB REPORT LIST ==========")

        self.laboratory.display_reports()


# ==========================================================
# SEARCH LAB REPORT
# ==========================================================

    def search_lab_report(self):

        print("\n========== SEARCH LAB REPORT ==========")

        report_id = input("Enter Report ID : ")

        report = self.laboratory.search_report(report_id)

        if report:

            report.display()

        else:

            print("Lab Report Not Found.")


# ==========================================================
# LABORATORY MENU
# ==========================================================

    def laboratory_menu(self):

        while True:

            print("\n===================================")
            print("      LABORATORY MANAGEMENT")
            print("===================================")

            print("1. Add Lab Report")
            print("2. View Lab Reports")
            print("3. Search Lab Report")
            print("4. Back")

            choice = input("Enter Choice : ")

            if choice == "1":

                self.add_lab_report()

            elif choice == "2":

                self.view_lab_reports()

            elif choice == "3":

                self.search_lab_report()

            elif choice == "4":

                break

            else:

                print("Invalid Choice.")

# ==========================================================

# ==========================================================
# ADD MEDICINE
# ==========================================================

    def add_medicine(self):

        print("\n========== ADD MEDICINE ==========")

        medicine_id = input("Enter Medicine ID : ")

        if self.pharmacy.search_medicine(medicine_id):

            print("Medicine ID Already Exists.")
            return

        name = input("Enter Medicine Name : ")

        company = input("Enter Company Name : ")

        price = float(input("Enter Price : "))

        stock = int(input("Enter Stock Quantity : "))

        expiry_date = input("Enter Expiry Date : ")

        medicine = Medicine(
            medicine_id,
            name,
            company,
            price,
            stock,
            expiry_date
        )

        self.pharmacy.add_medicine(medicine)


# ==========================================================
# VIEW MEDICINES
# ==========================================================

    def view_medicines(self):

        print("\n========== MEDICINE LIST ==========")

        self.pharmacy.display_all()


# ==========================================================
# SEARCH MEDICINE
# ==========================================================

    def search_medicine(self):

        print("\n========== SEARCH MEDICINE ==========")

        medicine_id = input("Enter Medicine ID : ")

        medicine = self.pharmacy.search_medicine(medicine_id)

        if medicine:

            medicine.display()

        else:

            print("Medicine Not Found.")


# ==========================================================
# UPDATE MEDICINE STOCK
# ==========================================================

    def update_medicine_stock(self):

        print("\n========== UPDATE MEDICINE STOCK ==========")

        medicine_id = input("Enter Medicine ID : ")

        medicine = self.pharmacy.search_medicine(medicine_id)

        if medicine is None:

            print("Medicine Not Found.")
            return

        stock = int(input("Enter New Stock : "))

        medicine.set_stock(stock)

        print("Medicine Stock Updated Successfully.")


# ==========================================================
# DELETE MEDICINE
# ==========================================================

    def delete_medicine(self):

        print("\n========== DELETE MEDICINE ==========")

        medicine_id = input("Enter Medicine ID : ")

        medicine = self.pharmacy.search_medicine(medicine_id)

        if medicine is None:

            print("Medicine Not Found.")
            return

        self.pharmacy.delete_medicine(medicine_id)


# ==========================================================
# ISSUE MEDICINE
# ==========================================================

    def issue_medicine(self):

        print("\n========== ISSUE MEDICINE ==========")

        medicine_id = input("Enter Medicine ID : ")

        quantity = int(input("Enter Quantity : "))

        self.pharmacy.issue_medicine(
            medicine_id,
            quantity
        )


# ==========================================================
# PHARMACY MANAGEMENT MENU
# ==========================================================

    def pharmacy_menu(self):

        while True:

            print("\n===================================")
            print("      PHARMACY MANAGEMENT")
            print("===================================")

            print("1. Add Medicine")
            print("2. View Medicines")
            print("3. Search Medicine")
            print("4. Update Medicine Stock")
            print("5. Delete Medicine")
            print("6. Issue Medicine")
            print("7. Back")

            choice = input("Enter Choice : ")

            if choice == "1":

                self.add_medicine()

            elif choice == "2":

                self.view_medicines()

            elif choice == "3":

                self.search_medicine()

            elif choice == "4":

                self.update_medicine_stock()

            elif choice == "5":

                self.delete_medicine()

            elif choice == "6":

                self.issue_medicine()

            elif choice == "7":

                break

            else:

                print("Invalid Choice.")

# ==========================================================
# GENERATE BILL
# ==========================================================

    def generate_bill(self):

        print("\n========== GENERATE BILL ==========")

        bill_id = input("Enter Bill ID : ")

        if self.search_bill(bill_id):

            print("Bill ID Already Exists.")
            return

        patient_id = input("Enter Patient ID : ")

        patient = self.search_patient(patient_id)

        if patient is None:

            print("Patient Not Found.")
            return

        doctor_fee = float(input("Enter Doctor Fee : "))
        lab_fee = float(input("Enter Lab Charges : "))
        medicine_fee = float(input("Enter Medicine Charges : "))
        ward_fee = float(input("Enter Ward Charges : "))

        bill = Bill(
            bill_id,
            patient,
            doctor_fee,
            lab_fee,
            medicine_fee,
            ward_fee
        )

        self.bills.append(bill)

        print("Bill Generated Successfully.")


# ==========================================================
# VIEW BILLS
# ==========================================================

    def view_bills(self):

        print("\n========== BILL LIST ==========")

        if len(self.bills) == 0:

            print("No Bills Found.")
            return

        for bill in self.bills:

            bill.display()

            print("--------------------------------")


# ==========================================================
# SEARCH BILL
# ==========================================================

    def search_bill_menu(self):

        print("\n========== SEARCH BILL ==========")

        bill_id = input("Enter Bill ID : ")

        bill = self.search_bill(bill_id)

        if bill:

            bill.display()

        else:

            print("Bill Not Found.")


# ==========================================================
# BILLING MENU
# ==========================================================

    def billing_menu(self):

        while True:

            print("\n===================================")
            print("         BILLING SYSTEM")
            print("===================================")

            print("1. Generate Bill")
            print("2. View Bills")
            print("3. Search Bill")
            print("4. Back")

            choice = input("Enter Choice : ")

            if choice == "1":

                self.generate_bill()

            elif choice == "2":

                self.view_bills()

            elif choice == "3":

                self.search_bill_menu()

            elif choice == "4":

                break

            else:

                print("Invalid Choice.")


# ==========================================================
# HOSPITAL REPORT
# ==========================================================

    def hospital_report(self):

        print("\n===================================")
        print("        MASS HOSPITAL REPORT")
        print("===================================")

        print("Hospital Name      :", self.name)

        print("Total Patients     :", len(self.patients))

        print("Total Doctors      :", len(self.doctors))

        print("Total Staff        :", len(self.staff))

        print("Total Appointments :", len(self.appointments))

        print("Total Wards        :", len(self.wards))

        print("Total Medicines    :", len(self.pharmacy.medicines))

        print("Total Lab Reports  :", len(self.laboratory.reports))

        print("Total Bills        :", len(self.bills))

        print("===================================")


# ==========================================================
# SAVE DATA
# ==========================================================

    def save_data(self):

        print("\nSave Data Feature Coming Soon.")

        # File Handling can be added here
        # according to your practiced file handling.


# ==========================================================
# LOAD DATA
# ==========================================================

    def load_data(self):

        print("\nLoad Data Feature Coming Soon.")

        # File Handling can be added here
        # according to your practiced file handling.

# ==========================================================
# MAIN MENU
# ==========================================================

def main_menu(hospital):

    while True:

        print("\n")
        print("==============================================")
        print("        MASS HOSPITAL MANAGEMENT SYSTEM")
        print("==============================================")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Staff Management")
        print("4. Appointment Management")
        print("5. Ward Management")
        print("6. Laboratory Management")
        print("7. Pharmacy Management")
        print("8. Billing System")
        print("9. Hospital Report")
        print("10. Save Data")
        print("11. Load Data")
        print("12. Exit")
        print("==============================================")

        choice = input("Enter Your Choice : ")

        if choice == "1":

            hospital.patient_menu()

        elif choice == "2":

            hospital.doctor_menu()

        elif choice == "3":

            hospital.staff_menu()

        elif choice == "4":

            hospital.appointment_menu()

        elif choice == "5":

            hospital.ward_menu()

        elif choice == "6":

            hospital.laboratory_menu()

        elif choice == "7":

            hospital.pharmacy_menu()

        elif choice == "8":

            hospital.billing_menu()

        elif choice == "9":

            hospital.hospital_report()

        elif choice == "10":

            hospital.save_data()

        elif choice == "11":

            hospital.load_data()

        elif choice == "12":

            print("\nSaving Data...")

            hospital.save_data()

            print("\nThank You For Using MASS Hospital")
            print("Program Closed Successfully.")

            break

        else:

            print("Invalid Choice.")


# ==========================================================
# MAIN FUNCTION
# ==========================================================

def main():

    hospital = Hospital()

    hospital.load_data()

    main_menu(hospital)


# ==========================================================
# PROGRAM START
# ==========================================================

if __name__ == "__main__":

    main()

# ==========================================================
# SAVE DATA
# ==========================================================

    def save_data(self):

        # ---------- Patients ----------
        with open("patients.txt", "w") as file:

            for patient in self.patients:

                data = (
                    patient._id + "," +
                    patient._name + "," +
                    str(patient._age) + "," +
                    patient._gender + "," +
                    patient._contact + "," +
                    patient.get_disease() + "," +
                    patient.get_blood_group() + "\n"
                )

                file.write(data)

        # ---------- Doctors ----------
        with open("doctors.txt", "w") as file:

            for doctor in self.doctors:

                data = (
                    doctor._id + "," +
                    doctor._name + "," +
                    str(doctor._age) + "," +
                    doctor._gender + "," +
                    doctor._contact + "," +
                    doctor.specialization + "," +
                    str(doctor.experience) + "," +
                    str(doctor.get_salary()) + "\n"
                )

                file.write(data)

        # ---------- Staff ----------
        with open("staff.txt", "w") as file:

            for staff in self.staff:

                data = (
                    staff._id + "," +
                    staff._name + "," +
                    str(staff._age) + "," +
                    staff._gender + "," +
                    staff._contact + "," +
                    staff.position + "," +
                    staff.department + "," +
                    str(staff.salary) + "\n"
                )

                file.write(data)

        # ---------- Medicines ----------
        with open("medicines.txt", "w") as file:

            for medicine in self.pharmacy.medicines:

                data = (
                    medicine.medicine_id + "," +
                    medicine.name + "," +
                    medicine.company + "," +
                    str(medicine.price) + "," +
                    str(medicine.get_stock()) + "," +
                    medicine.expiry_date + "\n"
                )

                file.write(data)

        print("\nData Saved Successfully.")


# ==========================================================
# LOAD DATA
# ==========================================================

    def load_data(self):

        # ---------- Patients ----------
        if os.path.exists("patients.txt"):

            with open("patients.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 7:

                        patient = Patient(
                            data[0],
                            data[1],
                            data[2],
                            data[3],
                            data[4],
                            data[5],
                            data[6]
                        )

                        self.patients.append(patient)

        # ---------- Doctors ----------
        if os.path.exists("doctors.txt"):

            with open("doctors.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 8:

                        doctor = Doctor(
                            data[0],
                            data[1],
                            data[2],
                            data[3],
                            data[4],
                            data[5],
                            data[6],
                            data[7]
                        )

                        self.doctors.append(doctor)

        # ---------- Staff ----------
        if os.path.exists("staff.txt"):

            with open("staff.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 8:

                        staff = Staff(
                            data[0],
                            data[1],
                            data[2],
                            data[3],
                            data[4],
                            data[5],
                            data[6],
                            data[7]
                        )

                        self.staff.append(staff)

        # ---------- Medicines ----------
        if os.path.exists("medicines.txt"):

            with open("medicines.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 6:

                        medicine = Medicine(
                            data[0],
                            data[1],
                            data[2],
                            float(data[3]),
                            int(data[4]),
                            data[5]
                        )

                        self.pharmacy.add_medicine(medicine)

        print("\nData Loaded Successfully.")

# ==========================================================
# SAVE APPOINTMENTS
# ==========================================================

        with open("appointments.txt", "w") as file:

            for appointment in self.appointments:

                file.write(
                    appointment.appointment_id + "," +
                    appointment.patient._id + "," +
                    appointment.doctor._id + "," +
                    appointment.date + "," +
                    appointment.time + "," +
                    appointment.status + "\n"
                )


# ==========================================================
# SAVE WARDS
# ==========================================================

        with open("wards.txt", "w") as file:

            for ward in self.wards:

                file.write(
                    ward.ward_id + "," +
                    ward.name + "," +
                    str(ward.capacity) + "\n"
                )


# ==========================================================
# SAVE LAB REPORTS
# ==========================================================

        with open("labreports.txt", "w") as file:

            for report in self.laboratory.reports:

                file.write(
                    report.report_id + "," +
                    report.patient._id + "," +
                    report.test_name + "," +
                    report.result + "," +
                    str(report.charges) + "\n"
                )


# ==========================================================
# SAVE BILLS
# ==========================================================

        with open("bills.txt", "w") as file:

            for bill in self.bills:

                file.write(
                    bill.bill_id + "," +
                    bill.patient._id + "," +
                    str(bill.doctor_fee) + "," +
                    str(bill.lab_fee) + "," +
                    str(bill.medicine_fee) + "," +
                    str(bill.ward_fee) + "\n"
                )


# ==========================================================
# LOAD APPOINTMENTS
# ==========================================================

        if os.path.exists("appointments.txt"):

            with open("appointments.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 6:

                        patient = self.search_patient(data[1])
                        doctor = self.search_doctor(data[2])

                        if patient and doctor:

                            appointment = Appointment(
                                data[0],
                                patient,
                                doctor,
                                data[3],
                                data[4]
                            )

                            appointment.status = data[5]

                            self.appointments.append(appointment)


# ==========================================================
# LOAD WARDS
# ==========================================================

        if os.path.exists("wards.txt"):

            with open("wards.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 3:

                        ward = Ward(
                            data[0],
                            data[1],
                            int(data[2])
                        )

                        self.wards.append(ward)


# ==========================================================
# LOAD LAB REPORTS
# ==========================================================

        if os.path.exists("labreports.txt"):

            with open("labreports.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 5:

                        patient = self.search_patient(data[1])

                        if patient:

                            report = LabReport(
                                data[0],
                                patient,
                                data[2],
                                data[3],
                                float(data[4])
                            )

                            self.laboratory.add_report(report)


# ==========================================================
# LOAD BILLS
# ==========================================================

        if os.path.exists("bills.txt"):

            with open("bills.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 6:

                        patient = self.search_patient(data[1])

                        if patient:

                            bill = Bill(
                                data[0],
                                patient,
                                float(data[2]),
                                float(data[3]),
                                float(data[4]),
                                float(data[5])
                            )

                            self.bills.append(bill)










