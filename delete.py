from es_con import estd_connection


def delete_student():
    cursor = estd_connection()

    id = input("Enter student ID ")

    sql = f"""
    DELETE FROM STUDENTS WHERE ID='{id}'
    """

    cursor.execute(sql)
    print("Student Deleted Successfully")
    choice = input("Do you wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False

