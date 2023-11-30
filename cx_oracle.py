import getpass

# import oracledb
#
# un = 'admin'
# cs = 'adb.us-sanjose-1.oraclecloud.com:1522/g1d275a9f70cf8a_cydb01_high.adb.oraclecloud.com'
# pw = '!Al033626699'
#
# with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
#     with connection.cursor() as cursor:
#         sql = """select sysdate from dual"""
#         for r in cursor.execute(sql):
#             print(r)

# import cx_Oracle
# tns = 'admin/!Al033626699@adb.us-sanjose-1.oraclecloud.com:1522/g1d275a9f70cf8a_cydb01_high.adb.oraclecloud.com'
# db1 = cx_Oracle.connect(tns)

import cx_Oracle

dsn_tns = cx_Oracle.makedsn('adb.us-sanjose-1.oraclecloud.com', 1522, service_name='g1d275a9f70cf8a_cydb01_high.adb.oraclecloud.com') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user='admin', password='!Al033626699', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute('select * from database.table') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
#conn.close()


# cx_Oracle.init_oracle_client()
# version = cx_Oracle.clientversion()
# print(f"Oracle Client version: {version[0]}.{version[1]}.{version[2]}")


# import oracledb
#
# connection = oracledb.connect(user='admin', password='!Al033626699', dsn='localhost/oraclepdb1')
#
# with connection.cursor() as cursor:
#     for row in cursor.execute('select city from locations'):
#         print(row)