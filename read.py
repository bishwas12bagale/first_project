from es_con import estd_connection



def read_student():
    cursor = estd_connection()
    id = input("Enter student ID ")

    sql = f"""
    SELECT * FROM STUDENTS WHERE ID='{id}'
    """

    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    choice = input("Do you wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False


