from es_con import estd_connection



def update_student():
    cursor = estd_connection()

    id = input("Enter student ID ")
    to_change = input("Enter the data you want to change ")
    changed_value = input(f"Enter new {to_change} ")

    sql = f"""
    UPDATE STUDENTS SET {to_change}='{changed_value}' WHERE ID='{id}'
    """

    cursor.execute(sql)
    print("Student updated successfully !!")
    choice = input("Do you wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
