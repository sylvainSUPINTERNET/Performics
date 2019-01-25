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
        return users
    except Exception as e:
        return dbQueryError(e)


def findById(id=1):
    dbc = dbInstance.cursor()

    try:
        sql = dbc.execute("""SELECT * FROM user WHERE id = %s """, id)
        user = dbc.fetchall()
        return user
    except pymysql.Error as e:
        return dbQueryError(e)


def add(body):
    dbc = dbInstance.cursor()

    try:
        created_at = time.strftime('%Y-%m-%d')
        values = (body["username"], body["email"], body["statut"], body["annee"], created_at)
        sql = "INSERT INTO user (username, email, statut, annee, created_at) VALUES (%s, %s, %s, %s, %s)"
        dbc.execute(sql, values)
        dbInstance.commit()
        return [{'message': 'insert with success', 'error': False, 'code_status': 200}]
    except Exception as e:
        return dbQueryError(e)


def remove(id):
    dbc = dbInstance.cursor()

    try:
        sql = "DELETE FROM user WHERE id = '%d'" % (id)
        dbc.execute(sql)
        dbInstance.commit()
        return [{'message': 'deleted with success', 'error': False, 'code_status': 200}]
    except Exception as e:
        dbInstance.rollback()
        return dbQueryError(e)


def modify(id, body):
    dbc = dbInstance.cursor()

    try:
        values = (body["username"], body["email"], body["statut"], body["annee"], id)
        sql = """UPDATE user SET username = %s, email = %s, statut = %s, annee= %s WHERE id = %s"""
        dbc.execute(sql, values)
        dbInstance.commit()
        return [{'message': 'updated with success', 'error': False, 'code_status': 200}]
    except Exception as e:
        dbInstance.rollback()
        return dbQueryError(e)
