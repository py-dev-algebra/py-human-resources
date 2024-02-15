

def employee_from_web(employee: dict) -> tuple:
    last_name = employee['name'].split(' ')[0]
    first_name = employee['name'].split(' ')[1]
    email = employee['email']
    address = f'{employee['address']['street']}, {employee['address']['zipcode']} {employee['address']['city']}'
    phone = employee['phone']
    website = employee['website']    
    company = employee['company']['name']
    
    return (last_name, first_name, email, address, phone, website, company)
