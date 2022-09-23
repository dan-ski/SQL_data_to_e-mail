import pyodbc

def connection(driver='SQL Server', server_name='lap-ds\sql2014', database_name=):
    conn = pyodbc.connect(f'Driver={driver};'
                          f'Server={server_name};'
                          f'Database={}')