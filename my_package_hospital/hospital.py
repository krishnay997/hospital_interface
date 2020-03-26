from patient import Patient
from employee import Employee

class Hospital():
    def __init__(self):
        self.name="Bakery Hospital"
        self.location="TTDI"
        self.employees=[Employee("krishna", "password", "superadmin"),Employee("hannibal", "iluvpeople", "doctor"),Employee("karen", "ih8hannibal", "nurse")]
        self.patient_list=[Patient("John","Broken heart")]
        self.new_emp_list=self.employees.copy()
        self.new_pat_list=self.patient_list.copy()

    def list_employees(self):
        print("")
        print("-------------------------------------")
        print(f"Total employees: {len(self.new_emp_list)}")
        print("Employee list:")
        print("")
        for e in self.new_emp_list:
            print(f"Name: {e.username} | Title: {e.job}")
        print("-------------------------------------")
        print("")

    def list_patients(self):
        print("")
        print("-------------------------------------")
        print(f"Total patients: {len(self.new_pat_list)}")
        print("Patient list:")
        print("")
        for p in self.new_pat_list:
            print(f"Name: {p.name}")
            print(f"Condition: {p.info}")
            print("")
        print("-------------------------------------")


    def add_employee(self):
        username = input("Please give employee a username: ")
        password = input("Please give employee a password: ")
        job = input("Please give employee a job: ")
        self.new_emp_list.append(Employee(username, password, job))
        print("")
        print(f"{username} has been added to the employee list as a {job}")
        print("")

    def remove_employee(self):
        user_inp = input("Enter employee username: ")
        pass_inp= input("Enter employee password: ")
        job_inp = input("Enter employee job: ")
        for e in self.new_emp_list:
            if user_inp==e.username and pass_inp==e.password and job_inp==e.job:
                self.new_emp_list.remove(e)
        print("")
        print(f"{e.username} has been removed from the employee list.")
        print("")

    def add_patient(self):
        name=input("Enter patient name:\n")
        info=input("Enter patient condition:\n")
        self.new_pat_list.append(Patient(name,info))
        print(f"{name} has been added to the patient list.")
        print("")

    def remove_patient(self):
        name_inp=input("Enter patient name:\n")
        info_inp=input("Enter patient condition:\n")
        for p in self.new_pat_list:
            if name_inp==p.name and info_inp==p.info:
                self.new_pat_list.remove(p)
        print(f"{p.name} has been removed from the patient list.")
        print("")

    def start(self):
        print("")
        print(f"Welcome to {self.name}!")
        print("------------------------")
        while True:
            user_inp = input("Enter Username:\n")
            pass_inp = input("Enter Password:\n")
            user_found = False
            for e in self.new_emp_list:
                if e.username == user_inp and e.password == pass_inp:
                    user_found = True
                    self.after_login(e)
                    break
            if not user_found:
                print("User not found!")

    def after_login(self, user):
        print("")
        print(f"Welcome {user.username} || Title: {user.job}")
        while True:
            if user.job == "superadmin":
                print("")
                print("1. List Employees")
                print("2. Add Employees")
                print("3. Remove Employees")
                print("4. List Patients")
                print("5. Add Patients")
                print("6. Remove Patients")
                print("7. Log out")
                print("")
                user_select = input("Choose an option:\n")
                print("")
                if user_select == "1":
                    self.list_employees()
                elif user_select == "2":
                    self.add_employee()
                elif user_select == "3":
                    self.remove_employee()
                elif user_select == "4":
                    self.list_patients()
                elif user_select == "5":
                    self.add_patient()
                elif user_select == "6":
                    self.remove_patient()
                elif user_select == "7":
                    break
                else:
                    print("Please select available options.")
            elif user.job == "doctor":
                print("1. List Patients")
                print("2. Add Patients")
                print("3. Remove Patients")
                print("4. Log out")
            
                user_select = input("Choose an option:\n")
                print("")
                if user_select == "1":
                    self.list_patients()
                elif user_select == "2":
                    self.add_patient()
                elif user_select == "3":
                    self.remove_patient()
                elif user_select == "4":
                    break
                else:
                    print("Please select available options.")
            elif user.job == "nurse":
                print("1. List Patients")
                print("2. Log out")
            
                user_select = input("Choose an option:\n")
                print("")
                if user_select == "1":
                    self.list_patients()
                elif user_select == "2":
                    break
                else:
                    print("Please select available options.")