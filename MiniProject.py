
import os
import fileinput
from platform import release

#Car Release
def carV():
    car_description = input('Enter the Car Number Which you hired : ')
    car_AV = input("Enter Avai;able if you retrned the vehicle : ")

    with open('car.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('car.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if car_description in line:
            for b in file[i+1:i+2]:
                value = str(b)
                change = (car_AV)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('car.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print("Thank you for Hiring")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()


# Van Release 
def vanV():
    van_description = input('Enter the Van Number Which you hired : ')
    van_AV = input("Enter Available if you returned the vehicle : ")

    with open('van.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('van.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if van_description in line:
            for b in file[i+1:i+2]:
                value = str(b)
                change = (van_AV)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('van.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print("Thank you for Hiring")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()

#three wheel hiring
def three_WheelV():
    three_description = input('Enter the threewheel Number Which you Hird : ')
    three_AV = input("Enter Available if you returned the vehicle : ")

    with open('ThreeWheel.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('ThreeWheel.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if three_description in line:
            for b in file[i+1:i+2]:
                value = str(b)
                change = (three_AV)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('ThreeWheel.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print("Thank you for Hiring")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()

#Truck Release 
def truckV():
    truck_description = input('Enter the Truck Number Which you Hired : ')
    truck_AV = input("Enter Available if you returned the vehicle : ")

    with open('truck.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('truck.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if truck_description in line:
            for b in file[i+1:i+2]:
                value = str(b)
                change = (truck_AV)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('truck.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print("Thank you for Hiring")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()

#Lorry Release 
def lorryV():
    lorry_description = input('Enter the Lorry Number Which you Hired : ')
    lorry_AV = input("Enter Available if you returned the vehicle : ")

    with open('lorry.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('lorry.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if lorry_description in line:
            for b in file[i+1:i+2]:
                value = str(b)
                change = (lorry_AV)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('lorry.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print("Thank you for Hiring")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()

#release a vehicle
def release_Vehicle():
    print("""
        ======Which Vehicle You Want to Remove======

                    1. Car
                    2. Van
                    3. Three Wheeler
                    4. Truck
                    5. Lorry

        ======================================
    """)

    add = input("Select the vehicle type : ")

    try:
          add = int(add)
    except ValueError:
          print("This is Invalid")

    if add == 1 :
        carV()
    elif add == 2 :
        vanV()
    elif add == 3:
        three_WheelV()
    elif add == 4 :
        truckV()
    elif add == 5 :
        lorryV()
    else :
        print("Check the Numbers again")
        back = input("Do you Want to Continue ? (y/n) ")

        if back == 'y':
            admin()
        else:
            exit()
   


#Car Hire
def carH():
    carD()
    car_description = input('Enter the Car Number Which you need : ')
    car_AV = input("Enter UnAvailable if you are giving for a Hire if not enter Available : ")

    with open('car.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('car.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if car_description in line:
            for b in file[i+1:i+2]:
                value = str(b)
                change = (car_AV)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('car.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print("Thank you for Hiring")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        main()
    else:
        exit()


# Van Hiring
def vanH():
    vanD()
    InventoryFile = open('van.txt', 'r')
    van_description = InventoryFile.read()
    van_available = InventoryFile.read()
    van_info = InventoryFile.read()
    print('\n\n-----------------')
    print('Current Inventory')
    print('-----------------\n\n')
    while van_description != '':
        van_info = InventoryFile.readline()
        van_available = InventoryFile.readline()
        van_description = van_description.rstrip('\n')
        van_available = van_available.rstrip('\n')
        van_info = van_info.rstrip('\n')
        print( '\n',van_description)
        print( '\n',van_available)
        print( '\n',van_info)
        van_description = InventoryFile.readline()
    InventoryFile.close()
    van_description = input('Enter the Van Number Which you need : ')
    van_AV = input("Enter UnAvailable if you are giving for a Hire if not enter Available : ")

    with open('van.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('van.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if van_description in line:
            for b in file[i+1:i+2]:
                value = str(b)
                change = (van_AV)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('van.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print("Thank you for Hiring")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        main()
    else:
        exit()

#three wheel hiring
def three_WheelH():
    three_WheelD()
    three_description = input('Enter the threewheel Number Which you need : ')
    three_AV = input("Enter UnAvailable if you are giving for a Hire if not enter Available : ")

    with open('ThreeWheel.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('ThreeWheel.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if three_description in line:
            for b in file[i+1:i+2]:
                value = str(b)
                change = (three_AV)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('ThreeWheel.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print("Thank you for Hiring")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        main()
    else:
        exit()

#Truck Hiring
def truckH():
    truckD()
    truck_description = input('Enter the Truck Number Which you need : ')
    truck_AV = input("Enter UnAvailable if you are giving for a Hire if not enter Available : ")

    with open('truck.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('truck.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if truck_description in line:
            for b in file[i+1:i+2]:
                value = str(b)
                change = (truck_AV)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('truck.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print("Thank you for Hiring")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        main()
    else:
        exit()

#Lorry Hiring 
def lorryH():
    lorryD()
    lorry_description = input('Enter the Lorry Number Which you need : ')
    lorry_AV = input("Enter UnAvailable if you are giving for a Hire if not enter Available : ")

    with open('lorry.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('lorry.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if lorry_description in line:
            for b in file[i+1:i+2]:
                value = str(b)
                change = (lorry_AV)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('lorry.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print("Thank you for Hiring")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        main()
    else:
        exit()

#assign a vehicle
def assign_Vehicle():
    print("""
        ======Which Type of Vehicle You Want to Hire/Assign======

                            1. Car
                            2. Van
                            3. Three Wheeler
                            4. Truck
                            5. Lorry

        ===========================================================
    """)

    add = input("Select the vehicle type : ")

    try:
          add = int(add)
    except ValueError:
          print("This is Invalid")

    if add == 1 :
        carH()
    elif add == 2 :
        vanH()
    elif add == 3:
        three_WheelH()
    elif add == 4 :
        truckH()
    elif add == 5 :
        lorryH()
    else :
        print("Check the Numbers again")
        back = input("Do you Want to Continue ? (y/n) ")

        if back == 'y':
            main()
        else:
            exit()


#remove a vehicle 
def remove_Vehicle():
    print("""
        ======Which Vehicle You Want to Remove======

                    1. Car
                    2. Van
                    3. Three Wheeler
                    4. Truck
                    5. Lorry

        ======================================
    """)

    add = input("Select the vehicle type : ")

    try:
          add = int(add)
    except ValueError:
          print("This is Invalid")

    if add == 1 :
        carR()
    elif add == 2 :
        vanR()
    elif add == 3:
        three_WheelR()
    elif add == 4 :
        truckR()
    elif add == 5 :
        lorryR()
    else :
        print("Check the Numbers again")
        back = input("Do you Want to Continue ? (y/n) ")

        if back == 'y':
            admin()
        else:
            exit()

#CarRemove
def carR():
    print("\n\n==================")
    print("Removing Inventory")
    print("==================\n\n")
    carPlate = input("Enter the number plate number : ")

    file = fileinput.input('car.txt', inplace=True)

    for line in file:
         if carPlate in line:
             for i in range(2):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    carPlate
    print("You have removed the car successfully")

    back = input("Do you Want to Continue ? (y/n)")

    if back == 'y':
        admin()
    else:
        exit()


#VanRemove
def vanR():
    print("\n\n==================")
    print("Removing Inventory")
    print("==================\n\n")
    vanPlate = input("Enter the number plate number : ")

    file = fileinput.input('van.txt', inplace=True)

    for line in file:
         if vanPlate in line:
             for i in range(2):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    vanPlate
    print("You have removed the van successfully")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()


#ThreeWheelRemove
def three_WheelR():
    print("\n\n==================")
    print("Removing Inventory")
    print("==================\n\n")
    threePlate = input("Enter the number plate number : ")

    file = fileinput.input('ThreeWheel.txt', inplace=True)

    for line in file:
         if threePlate in line:
             for i in range(2):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    threePlate
    print("You have removed the three wheeler successfully")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()



#TruckRemove
def truckR():
    print("\n\n==================")
    print("Removing Inventory")
    print("==================\n\n")
    truckPlate = input("Enter the number plate number : ")

    file = fileinput.input('truck.txt', inplace=True)

    for line in file:
         if truckPlate in line:
             for i in range(2):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    truckPlate
    print("You have removed the truck successfully")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()


#lorryRemove

def lorryR():
    print("\n\n==================")
    print("Removing Inventory")
    print("==================\n\n")
    lorryPlate = input("Enter the number plate number : ")

    file = fileinput.input('lorry.txt', inplace=True)

    for line in file:
         if lorryPlate in line:
             for i in range(2):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    lorryPlate
    print("You have removed the lorry successfully")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()

#Display Car
def carD():
    InventoryFile = open('car.txt', 'r')
    car_description = InventoryFile.read()
    car_available = InventoryFile.read()
    car_info = InventoryFile.read()
    print('\n\n-----------------')
    print('Current Inventory')
    print('-----------------\n\n')
    while car_description != '':
        car_info = InventoryFile.readline()
        car_available = InventoryFile.readline()
        car_description = car_description.rstrip('\n')
        car_available = car_available.rstrip('\n')
        car_info = car_info.rstrip('\n')
        print( '\n',car_description)
        print( '\n',car_available)
        print( '\n',car_info)
        car_description = InventoryFile.readline()
    InventoryFile.close()


#Display Van
def vanD():
    InventoryFile = open('van.txt', 'r')
    van_description = InventoryFile.read()
    van_available = InventoryFile.read()
    van_info = InventoryFile.read()
    print('\n\n-----------------')
    print('Current Inventory')
    print('-----------------\n\n')
    while van_description != '':
        van_info = InventoryFile.readline()
        van_available = InventoryFile.readline()
        van_description = van_description.rstrip('\n')
        van_available = van_available.rstrip('\n')
        van_info = van_info.rstrip('\n')
        print( '\n',van_description)
        print( '\n',van_available)
        print( '\n',van_info)
        van_description = InventoryFile.readline()
    InventoryFile.close()


#Display Three Wheel
def three_WheelD():
    InventoryFile = open('ThreeWheel.txt', 'r')
    three_description = InventoryFile.read()
    three_available = InventoryFile.read()
    three_info = InventoryFile.read()
    print('\n\n-----------------')
    print('Current Inventory')
    print('-----------------\n\n')
    while three_description != '':
        three_info = InventoryFile.readline()
        three_available = InventoryFile.readline()
        three_description = three_description.rstrip('\n')
        three_available = three_available.rstrip('\n')
        three_info = three_info.rstrip('\n')
        print( '\n',three_description)
        print( '\n',three_available)
        print( '\n',three_info)
        three_description = InventoryFile.readline()
    InventoryFile.close()

#Display Trucks
def truckD():
    InventoryFile = open('truck.txt', 'r')
    truck_description = InventoryFile.read()
    truck_available = InventoryFile.read()
    truck_info = InventoryFile.read()
    print('\n\n-----------------')
    print('Current Inventory')
    print('-----------------\n\n')
    while truck_description != '':
        truck_info = InventoryFile.readline()
        truck_available = InventoryFile.readline()
        truck_description = truck_description.rstrip('\n')
        truck_available = truck_available.rstrip('\n')
        truck_info = truck_info.rstrip('\n')
        print( '\n',truck_description)
        print( '\n',truck_available)
        print( '\n',truck_info)
        truck_description = InventoryFile.readline()
    InventoryFile.close()

#Display Lorry
def lorryD():
    InventoryFile = open('lorry.txt', 'r')
    lorry_description = InventoryFile.read()
    lorry_available = InventoryFile.read()
    lorry_info = InventoryFile.read()
    print('\n\n-----------------')
    print('Current Inventory')
    print('-----------------\n\n')
    while lorry_description != '':
        lorry_info = InventoryFile.readline()
        lorry_available = InventoryFile.readline()
        lorry_description = lorry_description.rstrip('\n')
        lorry_available = lorry_available.rstrip('\n')
        lorry_info = lorry_info.rstrip('\n')
        print( '\n',lorry_description)
        print( '\n',lorry_available)
        print( '\n',lorry_info)
        lorry_description = InventoryFile.readline()
    InventoryFile.close()


#display all the vehicles in the inventory
def display_Vehicle():
    print("""
        ======Which Type of Vehicle Want to Display======

                    1. Car
                    2. Van
                    3. Three Wheeler
                    4. Truck
                    5. Lorry

        ======================================
    """)

    add = input("Select the vehicle type : ")

    try:
          add = int(add)
    except ValueError:
          print("This is Invalid")

    if add == 1 :
        carD()
    elif add == 2 :
        vanD()
    elif add == 3:
        three_WheelD()
    elif add == 4 :
        truckD()
    elif add == 5 :
        lorryD()
    else :
        print("Check the Numbers again")
        back = input("Do you Want to Continue ? (y/n) ")

        if back == 'y':
            main()
        else:
            exit()



#add a vehicle
def add_Vehicle():
    print("""
        ======Which Vehicle You Want to Add======

                    1. Car
                    2. Van
                    3. Three Wheeler
                    4. Truck
                    5. Lorry

        ======================================
    """)

    add = input("Select the vehicle type : ")

    try:
          add = int(add)
    except ValueError:
          print("This is Invalid")

    if add == 1 :
        carA()
    elif add == 2 :
        vanA()
    elif add == 3:
        three_WheelA()
    elif add == 4 :
        truckA()
    elif add == 5 :
        lorryA()
    else :
        print("Check the Numbers again")
        back = input("Do you Want to Continue ? (y/n) ")

        if back == 'y':
            admin()
        else:
            exit()


#CarAdd
def carA():
    InventoryFile = open('car.txt', 'a')
    print("\n\n===============")
    print("Adding New Cars")
    print("================\n\n")
    carPlate = input("Enter the number plate number of the car: ")
    carType = input("Enter the type of the car: ")
    passanger = input("How many passangers can travel: ")
    ac = input("A/C is Present or Non : ")
    InventoryFile.write('\n\nNumber Plate : '+ carPlate + ' \n ')
    InventoryFile.write("Available \n")
    InventoryFile.write('Car Type : '+ carType + ' , ')
    InventoryFile.write('Number of Passangers : '+ passanger + ' , ')
    InventoryFile.write('A/C Facility : '+ ac + '\n')
    InventoryFile.close()
    print("You have added the car successfully")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()


#VanAdd
def vanA():
    InventoryFile = open('van.txt', 'a')
    print("\n\n===============")
    print("Adding New Vans")
    print("================\n\n")
    vanPlate = input("Enter the number plate number of the Van: ")
    vanType = input("Enter the type of the Van: ")
    passanger = input("How many passangers can travel: ")
    ac = input("A/C is Present or Non : ")
    InventoryFile.write('\n\nNumber Plate : '+ vanPlate + ' \n ')
    InventoryFile.write("Available \n")
    InventoryFile.write('Van Type : '+ vanType + ' , ')
    InventoryFile.write('Number of Passangers : '+ passanger + ' , ')
    InventoryFile.write('A/C Facility : '+ ac + '\n')
    InventoryFile.close()
    print("You have added the Van successfully")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()
    
#ThreeWheelAdd

def three_WheelA():
    InventoryFile = open('ThreeWheel.txt', 'a')
    print("\n\n===============")
    print("Adding New Three Wheels")
    print("================\n\n")
    threePlate = input("Enter the number plate number of the Three Wheel: ")
    threeType = input("Enter the type of the Three Wheel: ")
    passanger = input("How many passangers can travel: ")
    InventoryFile.write('Number Plate : '+ threePlate + ' \n ')
    InventoryFile.write("Available \n")
    InventoryFile.write('\n\nThree Wheel Type : '+ threeType + ' , ')
    InventoryFile.write('Number of Passangers : '+ passanger + ' , ')
    InventoryFile.close()
    print("You have added the Three Wheeler successfully")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()

#TruckAdd

def truckA(): 
    InventoryFile = open('truck.txt', 'a')
    print("\n\n===============")
    print("Adding New Truck")
    print("================\n\n")
    truckPlate = input("Enter the number plate number of the Truck: ")
    truckType = input("Enter the type of the car: ")
    passanger = input("What is the size of the truck : ")
    InventoryFile.write('\n\nNumber Plate : '+ truckPlate + ' \n ')
    InventoryFile.write("Available \n")
    InventoryFile.write('Truck Type : '+ truckType + ' , ')
    InventoryFile.write('Size : '+ passanger + ' , ')
    InventoryFile.close()
    print("You have added the Truck successfully")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()

#lorryAdd
def lorryA():
    InventoryFile = open('lorry.txt', 'a')
    print("\n\n===============")
    print("Adding New Lorries")
    print("================\n\n")
    lorryPlate = input("Enter the number plate number of the lorry: ")
    lorryType = input("Enter the type of the lorry: ")
    passanger = input("What is the max load : ")
    InventoryFile.write('\n\nNumber Plate : '+ lorryPlate + ' \n ')
    InventoryFile.write("Available \n")
    InventoryFile.write('Lorry Type : '+ lorryType + ' , ')
    InventoryFile.write('Max Load : '+ passanger + ' , ')
    InventoryFile.close()
    print("You have added the lorry successfully")

    back = input("Do you Want to Continue ? (y/n) ")

    if back == 'y':
        admin()
    else:
        exit()

   
#Admin Fuction

def admin():
    print("""
          =============ADMIN MENUE==============

               1. Add New Vehicle
               2. Remove a Vehicle
               3. Assign a Job
               4. Release form assigned Job
               5. Display Available Vehicles
               6. Go Back
               9. Exit

           ======================================
          """)
    choose = input("Choose an option : ") 

    try:
          choose = int(choose)
    except ValueError:
          print("This is Invalid")
    
    if choose == 1 :
        add_Vehicle()
    elif choose == 2 :
        remove_Vehicle()
    elif choose == 3 :
        assign_Vehicle()
    elif choose == 4 :
        release_Vehicle()
    elif choose == 5 :
        display_Vehicle()
    elif choose == 6:
        main()
    elif choose == 9 :
        print("Thank you for using our Cab Service")
        exit()
    else :
        print("Check the Numbers again")
        back = input("Do you Want to Continue ? (y/n) ")

        if back == 'y':
            admin()
        else:
            exit()
         

#Customer Fuction
def customer():
    print("""
          =============CUSTOMER MENUE==============

                1. Hire A Vehicle
                2. Display Available Vehicles
                6. Go Back
                9. Exit

           ======================================
          """)
    choose = input("Choose an option : ")

    try:
          choose = int(choose)
    except ValueError:
          print("This is Invalid")

    if choose == 1 :
        assign_Vehicle()
    elif choose == 2 :
        display_Vehicle()
    elif choose == 6:
        main()
    elif choose == 9 :
        print("Thank you for using our Cab Service")
        exit()
    else :
        print("Check the Numbers again")
        back = input("Do you Want to Continue ? (y/n) ")

        if back == 'y':
            customer()
        else:
            exit()




#Main Function

def main():
    print("""
            =============**************************=============
                         WELCOME TO THE CAB SERVICE
            =============**************************=============

                             1. Admin
                             2. Customer
                             9. Exit

            ====================================================

          """)

    select = input("Select an option : ")

    try:
        select = int(select)
    except ValueError:
        print("This is Invaild")

    if select == 1 :
        admin()
    elif select == 2 :
        customer()
    elif select == 9 :
        print("\n Thank you for using our Cab Service \n")
        exit()

main()

