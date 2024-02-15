import sqlite3

from commons.app_constants import DB_NAME



def create_table(create_table_query: str) -> str:
    try:
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()

        cursor.execute(create_table_query)
        cursor.close()
        return f'INFO: Tabela je uspjesno kreirana!'

    except sqlite3.Error as sql_error:
        print(f'ERROR: Dogodila se SQLite greska {sql_error}')

    except Exception as ex:
        print(f'ERROR: Dogodila se greska {ex}')

    finally:
        if sqlite_connection:
            sqlite_connection.close()


def create_employee(employee: tuple):
    insert_into_table_query = '''
        INSERT INTO employees (last_name, first_name, email, address, phone, website, company)
        VALUES  (?, ?, ?, ?, ?, ?, ?);
    '''
    try:
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()

        cursor.execute(insert_into_table_query, employee)
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