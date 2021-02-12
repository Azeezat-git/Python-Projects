black_list = ["JOHN", "JAMES", "KAREN", "PAUL"]

num_of_student = int(input("Enter the number of graduating student here: "))

white_list = ""

for student in range(num_of_student):
    name = input("Enter a name: ").upper()
    #while name == "":
    if name == "":
        print("Enter a non-empty name please!")
    if name not in black_list:
        #white_list.append(name)
        white_list = white_list + name + " "
    

print(white_list)


    

