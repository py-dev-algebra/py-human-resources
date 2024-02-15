from services.employee_services.employee_db_mgr import create_employee_from_web

from services.db_services.db_mgr import create_table
from commons.sql_queries import CREATE_TABLE_EMPLOYEES_QUERY


def init_db():
    message = create_table(CREATE_TABLE_EMPLOYEES_QUERY)
    print(message)


def start_app():
    create_employee_from_web(5)
    # update_employee()


if __name__ == '__main__':
    init_db()
    start_app()
