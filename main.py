from services.employee_services.employee_db_mgr import (create_employee_from_web,
                                                        update_employee)

from services.db_services.db_mgr import create_table
from commons.sql_queries import CREATE_TABLE_EMPLOYEES_QUERY


def init_db():
    message = create_table(CREATE_TABLE_EMPLOYEES_QUERY)
    print(message)


def start_app():
    create_employee_from_web(5)

    id = int(input('Upisite ID djelantika kojeg zelite editirati: '))
    first_name = input('Upisite novo ime djelantika: ')
    update_employee(id=id, new_value=first_name)


if __name__ == '__main__':
    init_db()
    start_app()
