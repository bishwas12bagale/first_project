from es_con import estd_connection


def insert_student():
    cursor = estd_connection()

    id = input("Enter student ID ")
    name = input("Student name ")
    address=input("student address ")
    email = input("student email address ")
    age = int(input("Enter student's age "))


    sql = f"""
    INSERT INTO STUDENTS (ID, NAME, ADDRESS, EMAIL_ID, AGE) VALUES ('{id}','{name}','{address}','{email}',{age})
    """

    cursor.execute(sql)
    print("Student added successfully !!")
    choice = input("Do you wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
