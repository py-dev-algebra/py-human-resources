from services.employee_services.employee_webapi_mgr import get_employee
from services.employee_services.employee_db_mgr import create_employee
from services.db_services.db_mgr import create_table
from commons.sql_queries import CREATE_TABLE_EMPLOYEES_QUERY



def init_db():
    message = create_table(CREATE_TABLE_EMPLOYEES_QUERY)
    print(message)


def start_app():
    # Dohvati podatke s interneta
    employee = get_employee()

    # Prilagodi za upis u bazu
    last_name = employee['name'].split(' ')[0]
    first_name = employee['name'].split(' ')[1]
    email = employee['email']
    address = f'{employee['address']['street']}, {employee['address']['zipcode']} {employee['address']['city']}'
    phone = employee['phone']
    website = employee['website']    
    company = employee['company']['name']
    
    employee_tuple = (last_name, first_name, email, address, phone, website, company)
    print(employee_tuple)
    
    # upisi u bazu
    create_employee(employee_tuple)




if __name__ == '__main__':
    init_db()
    start_app()
