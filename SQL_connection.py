import pyodbc

def connection(driver='SQL Server Native Client 11.0', server_name='lap-ds\sql2014',
               database_name='CDN_Prezentacja_KH',
               trusted_connection='yes'):

    conn = pyodbc.connect(f'Driver={driver};'
                          f'Server={server_name};'
                          f'Database={database_name};'
                          f'Trusted_Connection={trusted_connection};')

    cursor = conn.cursor()
    print('Inside connection function')
    return cursor

cursor = connection()

def execute_query(cursor, query):
    cursor.execute(query)

    return


print('test')
