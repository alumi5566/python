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

import cx_Oracle
tns = 'admin/!Al033626699@adb.us-sanjose-1.oraclecloud.com:1522/g1d275a9f70cf8a_cydb01_high.adb.oraclecloud.com'
db1 = cx_Oracle.connect(tns)