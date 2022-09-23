import pyodbc

def connection(driver='SQL Server', server_name='lap-ds\sql2014', database_name='CDN_Prezentacja_KH',
               trusted_connection='yes'):

    conn = pyodbc.connect(f'Driver={driver};'
                          f'Server={server_name};'
                          f'Database={database_name};'
                          f'Trusted_Connection={trusted_connection};')

    cursor = conn.cursor()
    print('Inside connection function')
    return cursor

print('test')
