import pickle

# loading data from a .dat file using De-serialization
f = open("employees.dat", "rb")
employees = pickle.load(f)

for dept, emps in employees.items():
    print(dept, ",".join(emps))
