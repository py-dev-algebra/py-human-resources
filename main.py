from services.employee_services.employee_db_mgr import create_table
from commons.sql_queries import CREATE_TABLE_EMPLOYEES_QUERY

message = create_table(CREATE_TABLE_EMPLOYEES_QUERY)
print(message)
