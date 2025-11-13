MemberId = [""] * 1000
Name = [["", ""] for x in range(1000)] #a list of lists
MemberCount = 0
print("********* MemberShip Program ********* ")
choice = 0
while choice != 3: # Repeat menu until the user chooses to exit (choice == 3)

    print("1.) Input a new member")     # Display menu options
    print("2.) Output Member List")
    print("3.) Exit the program")
    choice = int(input("Enter your choice"))      # Input user's choice
    if choice == 1:
        if MemberCount < 1000:          # Check if the list has space for more members
            NewId = input("enter a new member id (6 alphanumeric char): ")
            while len(NewId) != 6 or NewId in MemberId:  # Validate that ID is exactly 6 characters and unique
                NewId = input("Please enter a (6 alphanumeric char) UNIQUE member id : ")
            MemberId[MemberCount] = NewId  #input names, member id and increase member count
            Name[MemberCount][0] = input("enter First name")
            Name[MemberCount][1] = input("enter last name")
            MemberCount = MemberCount + 1
        else:
            print("List is Full")
    elif choice == 2:
        for i in range(MemberCount): #loop to output all member names and id
            print("First Name: ", Name[i][0], "Last Name: ", Name[i][1], "Member Id: ", MemberId[i])

print("thanks for using the program")
