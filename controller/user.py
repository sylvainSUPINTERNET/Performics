import json

import pymysql
from db.conf import host, password, user, dbname, port
from db.errorManager import dbQueryError
import time

dbInstance = pymysql.connect(host, user, password, dbname, port)


def findAll():
    dbc = dbInstance.cursor()
    try:
        sql = dbc.execute("""SELECT * FROM user""")
        users = dbc.fetchall()
        dbc.close()
        return users
    except Exception as e:
        dbc.close()
        return dbQueryError(e)


def findById(id=1):
    dbc = dbInstance.cursor()

    try:
        sql = dbc.execute("""SELECT * FROM user WHERE id = %s """, id)
        user = dbc.fetchall()
        dbc.close()
        return user
    except pymysql.Error as e:
        dbc.close()
        return dbQueryError(e)


def add(body):
    dbc = dbInstance.cursor()

    try:
        created_at = time.strftime('%Y-%m-%d')
        values = (body["username"], body["email"], body["statut"], body["annee"], created_at)
        sql = "INSERT INTO user (username, email, statut, annee, created_at) VALUES (%s, %s, %s, %s, %s)"
        dbc.execute(sql, values)
        dbInstance.commit()
        dbc.close()
        return [{'message': 'insert with success', 'error': False, 'code_status': 200}]
    except Exception as e:
        dbc.close()
        return dbQueryError(e)


def remove(id):
    dbc = dbInstance.cursor()

    try:
        sql = "DELETE FROM user WHERE id = '%d'" % (id)
        dbc.execute(sql)
        dbInstance.commit()
        dbInstance.close()
        return [{'message': 'deleted with success', 'error': False, 'code_status': 200}]
    except Exception as e:
        dbInstance.rollback()
        dbInstance.close()
        return dbQueryError(e)

# todo : https://www.tutorialspoint.com/python3/python_database_access.htm (delete create update)
