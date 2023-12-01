from insert import insert_student
from read import read_student
from update import update_student
from delete import delete_student
def student():
    selection = input("Enter your selection insert/read/update/delete ")
    selection = selection.lower()

    def exit_message():
        print("Thank you. See you again !!")
    if  selection == "insert":
        repeat = insert_student() 
        student() if repeat else exit_message()
    elif selection == "read":
        repeat = read_student()
        student() if repeat else exit_message()
    elif selection == "update":
        repeat = update_student()
        student() if repeat else exit_message()
    elif selection == "delete":
        repeat = delete_student()
        student() if repeat else exit_message()
    else:
        exit_message()


if __name__ == "__main__":
    student()
