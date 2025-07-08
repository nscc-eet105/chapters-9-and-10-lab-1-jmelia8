#Joe Melia EET-107

def main():
    print("Name Processor\n")
    name = input("Enter your first and last name: ")
    fullname = name.split()
    if "," in name:
        fname = fullname[1]
        lname = fullname[0]
        fname = fname.lower()
        lname = lname.lower()
        fname = fullname[1].capitalize()
        lname = fullname[0].capitalize()
        print(lname, fname)
    else:
        fname = fullname[0]
        lname = fullname[1]
        fname = fname.lower()
        lname = lname.lower()
        fname = fullname[0].capitalize()
        lname = fullname[1].capitalize()
        print(lname,",", fname)
main()
    
    
