def estd_connection():
    import psycopg2
    conn = psycopg2.connect(
        database="student_details",
        user="postgres",
        password="postgres123",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    print("Connection established successfully !!")
    cursor = conn.cursor()
    return cursor


if __name__ == "__main__":
    estd_connection()
