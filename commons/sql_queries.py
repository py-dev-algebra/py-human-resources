CREATE_TABLE_EMPLOYEES_QUERY = '''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            last_name TEXT NOT NULL,
            first_name TEXT,
            email TEXT NOT NULL UNIQUE,
            address TEXT,
            phone TEXT,
            website TEXT,
            company TEXT
        );
    '''
