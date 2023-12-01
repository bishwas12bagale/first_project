from es_con import estd_connection

cursor = estd_connection()

# cursor.execute("DROP TABLE STUDENT")
# def create_student():
sql = """
CREATE TABLE IF NOT EXISTS STUDENTS(
    ID CHAR(20),
    NAME CHAR(20),
    Address CHAR(30),
    EMAIL_ID CHAR(35),
    AGE INT
)
"""

cursor.execute(sql)
print("Table Created Successfully !!")


