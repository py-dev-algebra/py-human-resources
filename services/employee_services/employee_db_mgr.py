import sqlite3

from commons.app_constants import DB_NAME
from services.employee_services.employee_mapper import employee_from_web
from services.employee_services.employee_webapi_mgr import get_employee


def create_employee_from_web(id: int = 1):

    employee = get_employee(id)
    employee_tuple = employee_from_web(employee)

    insert_into_table_query = '''
        INSERT INTO employees (last_name, first_name, email, address, phone, website, company)
        VALUES  (?, ?, ?, ?, ?, ?, ?);
    '''
    try:
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()

        cursor.execute(insert_into_table_query, employee_tuple)
        sqlite_connection.commit()
        
        cursor.close()
        return f'INFO: Podaci su uspjesno pohranjeni u bazu!'

    except sqlite3.Error as sql_error:
        print(f'ERROR: Dogodila se SQLite greska {sql_error}')

    except Exception as ex:
        print(f'ERROR: Dogodila se greska {ex}')

    finally:
        if sqlite_connection:
            sqlite_connection.close()
