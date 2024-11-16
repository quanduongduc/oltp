import os
import pymysql

from config import OLTP_DB_HOST, OLTP_DB_PASS, OLTP_DB_USER

# Establish connection to the database
connection = pymysql.connect(
    host=OLTP_DB_HOST, user=OLTP_DB_USER, password=OLTP_DB_PASS
)

scripts_folder = "databases_scripts"
try:
    with connection.cursor() as cursor:
        for script_file in os.listdir(scripts_folder):
            if script_file.endswith(".sql"):
                script_path = os.path.join(scripts_folder, script_file)
                with open(script_path, "r") as file:
                    sql_commands = file.read()
                    for command in sql_commands.split(";"):
                        if command.strip():
                            cursor.execute(command)
        connection.commit()
finally:
    connection.close()
