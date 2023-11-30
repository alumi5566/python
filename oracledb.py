import oracledb
import json
from django.core.exceptions import ImproperlyConfigured

with open('secrets.json') as secrets_file:
    secrets = json.load(secrets_file)


def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))


username = "admin"
password = get_secret("PYTHON_PASSWORD")
dsn = get_secret("PYTHON_CONNECTSTRING")

connection = oracledb.connection(user=username, password=password, dsn=dsn)

with connection.cursor() as cursor:
    try:

        sql = """select systimestamp from dual"""
        for r in cursor.execute(sql):
            print(r)

    except oracledb.Error as e:
        error, = e.args
        print(error.message)
        print(sql)
        if error.offset:
            print('^'.rjust(error.offset + 1, ' '))
