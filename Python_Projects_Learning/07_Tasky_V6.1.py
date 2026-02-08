# Started in 2/5/2026 at 5:49 AM
# Finish in 2/8/2026 at 10:00 AM
# Version-6
# A Python console-based task management application that allows users to add, view, modify,
# and delete tasks with details like type, priority, notes, time, serial, and status.

# Version-6.1
# Added functionality to save and load tasks from a JSON file for data persistence


#################################################  Libraries  ###############################################
import json
import os

#################################################  Global_Conidtions_Var  ###############################################

First = True

#################################################  Data_Structures  ###############################################

Storage = {
    
}

#################################################  Functions  ###############################################

def sep():
    print("=" * 70)
    input("Press Enter To Continue...")



def add_task():
    task_name = input("Type Your Task Name: ")
    task_type = input("Enter Your Task Type (Study, Project, Hobbie, Else): ")
    task_priority = input("Enter Your Task Priority (Not Important, Medium Importance, Important, Very Important): ")
    task_notes = input("Enter Your Notes: ")
    task_day = input("Enter Your Task Time (Year or Month or Day or Just Time): ")
    task_status = input("Enter Your Task Status (True = Completed | False = Not Completed Yet): ")
    if task_status not in ["True", "False", "1", "0"]:
        print("Error! Task Status Must be (True, False, 1 or 0)")
        return
    serial_num = input("Enter Your Serial Number! (To Delete, Search And Modify Tasks): ")

    Storage[task_name] = {
        "type" : task_type,
        "priority" : task_priority,
        "notes" : task_notes,
        "time" : task_day,
        "serial" : serial_num,
        "status" : task_status
    }

    print(f"Task [{task_name}] Added Succssefully!")
    sep()



def show_tasks():
    Test = True
    for Key1, Val1 in Storage.items():
        Test = False
        print(f"Task ({Key1})")
        for key2, Val2 in Val1.items():
            print(f"    [{key2}] =>   {Val2}")
    if(Test):
        print("There Is No Tasks!")
    sep()



def show_comp_tasks():
    for Key1, Val1 in Storage.items():
        if Storage[Key1]["status"] in ["True", "1"]:
            print(f"Task ({Key1})")
            for Key2, Val2 in Val1.items():
                print(f"    [{Key2}] =>   {Val2}")
                
    sep()




def modify_del():
    
    serial_num_test = input("Enter Your Task_Serial_Number Please! (If You Forget it return and show all tasks): ")
    test = True
    task_name = None
    for Key1, Val1 in Storage.items():
        for Key2, Val2 in Val1.items():
            if Storage[Key1][Key2] == serial_num_test and Key2 == "serial":
                task_name = Key1
                if test:
                    print(f"This is Your Task [{Key1}]:")
                    test = False
                for Key3, Val3 in Val1.items():
                    print(f"    [{Key3}] =>   {Val3}")
                print("=" * 70)
            
    if test:
            print("Not Defined Task!")
            sep()
    while not test:
        choose = input("{Modify : 0} | {Del : 1} | {Exit : 9} : ")
        if choose == "0":
            print("********** Modifying-List **********")
            print("=>       Modify Task_Name?     (1)")
            print("=>       Modify Task_Type?     (2)")
            print("=>       Modify Task_Priority? (3)")
            print("=>       Modify Task_Notes?    (4)")
            print("=>       Modify Task_Day?      (5)")
            print("=>       Modify Task_Serial?   (6)")
            print("=>       Modify Task_Status?    (7)")
            print("=>             Exit            (9)")
            chos = input("Enter Your Number!: ")

            if chos == "1":
                print("=" * 70)
                new_task_name = input("Enter Your New Task Name: ")
                task_data = Storage.pop(task_name)
                Storage[new_task_name] = task_data
                print(f"Task Successfully Changed From [{task_name}] To [{new_task_name}]")
                task_name = new_task_name
                sep()

            elif chos == "2":
                new_task_type = input("Enter Your New Task Type: ")
                for Key1, Val1 in Storage.items():
                    for Key2, Val2 in Val1.items():
                        if Storage[Key1][Key2] == serial_num_test and Key2 == "serial":
                            print(f"Task Successfully Changed From [{Storage[Key1]['type']}] To [{new_task_type}]")
                            Storage[Key1]["type"] = new_task_type
                            sep()
                            
            elif chos == "3":
                new_task_priority = input("Enter Your New Task Priority: ")
                for Key1, Val1 in Storage.items():
                    for Key2, Val2 in Val1.items():
                        if Storage[Key1][Key2] == serial_num_test and Key2 == "serial":
                            print(f"Task Successfully Changed From [{Storage[Key1]['priority']}] To [{new_task_priority}]")
                            Storage[Key1]["priority"] = new_task_priority
                            sep()

            elif chos == "4":
                new_task_notes = input("Enter Your New Task Notes: ")
                for Key1, Val1 in Storage.items():
                    for Key2, Val2 in Val1.items():
                        if Storage[Key1][Key2] == serial_num_test and Key2 == "serial":
                            print(f"Task Successfully Changed From [{Storage[Key1]['notes']}] To [{new_task_notes}]")
                            Storage[Key1]["notes"] = new_task_notes
                            sep()

            elif chos == "5":
                new_task_time = input("Enter Your New Task Time: ")
                for Key1, Val1 in Storage.items():
                    for Key2, Val2 in Val1.items():
                        if Storage[Key1][Key2] == serial_num_test and Key2 == "serial":
                            print(f"Task Successfully Changed From [{Storage[Key1]['time']}] To [{new_task_time}]")
                            Storage[Key1]["time"] = new_task_time
                            sep()

            elif chos == "6":
                new_task_serial = input("Enter Your New Task Serial: ")
                for Key1, Val1 in Storage.items():
                    for Key2, Val2 in Val1.items():
                        if Storage[Key1][Key2] == serial_num_test and Key2 == "serial":
                            print(f"Task Successfully Changed From [{Storage[Key1]['serial']}] To [{new_task_serial}]")
                            Storage[Key1]["serial"] = new_task_serial
                            sep()

            elif chos == "7":
                new_task_status = input("Enter Your New Task Status: ")
                for Key1, Val1 in Storage.items():
                    for Key2, Val2 in Val1.items():
                        if Storage[Key1][Key2] == serial_num_test and Key2 == "serial":
                            print(f"Task Successfully Changed From [{Storage[Key1]['status']}] To [{new_task_status}]")
                            Storage[Key1]["status"] = new_task_status
                            sep()

            elif chos == "9":
                sep()
                break


            
        elif choose == "1":
            print(f"Task [{task_name}] Deleted Successfully!")
            Storage.pop(task_name)
            sep()
            break

        elif choose == "9":
            sep()
            break



def save_load_file():
    global Storage
    choice = input("You Want Save File or Load? (Type Save or Load): ")

    folder_path = r"C:\Tasky"
    file_path = os.path.join(folder_path, "Tasky.json")
    if choice.lower() == "save":
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(file_path, "w") as file_obj:
            json.dump(Storage, file_obj, indent = 4)
        print(f"File Save in [{file_path}] Succesfully")
        sep()

    if choice.lower() == "load":
        if not os.path.exists(folder_path):
            print(f"No Folder Defined To Load in [{folder_path}]")
            sep()
            return
        if not os.path.exists(file_path):
            print(f"No File Defined To Load in [{file_path}]")
            sep()
            return
        with open(file_path, "r") as file:
            Storage = json.load(file)
        print(f"File [{file_path}] Loaded Successfully!")
        sep()


#################################################  Main_Func  ###############################################

while True:
    if First:
        print("Hello To Management Your Time")
        First = False
    print("=" * 70)
    print("Add a task                (1)")
    print("Show All Tasks            (2)")
    print("Show All Completed Tasks  (3)")
    print("Modify or Del Task        (4)")
    print("Save Or Load File         (5)")
    print("Exit                      (9)")



    Choice = input("Enter Your Number!: ")
    if Choice == "1":
        print("=" * 70)
        add_task()

    elif Choice == "2":
        print("=" * 70)
        show_tasks()


    elif Choice == "3":
        print("=" * 70)
        show_comp_tasks()

    elif Choice == "4":
        print("=" * 70)
        modify_del()

    elif Choice == "5":
        print("=" * 70)
        save_load_file()

    elif Choice == "9":
        print("=" * 70)
        break