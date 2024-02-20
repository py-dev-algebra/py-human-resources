from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from services.employee_services.employee_db_mgr import (create_employee_from_web,
#                                                         update_employee)

# from services.db_services.db_mgr import create_table
# from commons.sql_queries import CREATE_TABLE_EMPLOYEES_QUERY
# from commons.sql_alchemy_base import Base
from models.addresses import Address
from models.companies import Company
from models.employees import Employee

from services.address_services.address_mgr import AddressManager


def init_db():
    # message = create_table(CREATE_TABLE_EMPLOYEES_QUERY)
    # print(message)
    engine = create_engine('sqlite:///database/tvrtka_sa.db')
    # Base.metadata.create_all(engine)
    Address.metadata.create_all(engine)
    Company.metadata.create_all(engine)
    Employee.metadata.create_all(engine)

    return engine


def start_app(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    address_manager = AddressManager(session)

    address = Address(street_number='Ilica 256', zip_code='10000', city='Zagreb')
    address_manager.create_address(address=address)
    # create_employee_from_web(5)

    # id = int(input('Upisite ID djelantika kojeg zelite editirati: '))
    # first_name = input('Upisite novo ime djelantika: ')
    # update_employee(id=id, new_value=first_name)
    pass


if __name__ == '__main__':
    db_engine = init_db()
    start_app(db_engine)
