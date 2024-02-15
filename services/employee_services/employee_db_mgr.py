import sqlite3



def create_table(create_table_query: str) -> str:
    try:
        sqlite_connection = sqlite3.connect('tvrtka.db')
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
