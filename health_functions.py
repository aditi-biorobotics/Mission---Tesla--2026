# Line 1:
print("automated lab report system")
def generate_report(name,bp,sugar):
    print("patient name: " + name)
    print("Blood pressure: " + str(bp))
    print("sugar level: " + str(sugar))
    if bp > 140 or sugar > 200:
        print("Status: Critical doctor needed!")
    else:
        print("status: stable.")
    print("\n")
generate_report("Aditi", 120, 90)
generate_report("Rahul", 150, 210)
generate_report("Anu", 130,100)