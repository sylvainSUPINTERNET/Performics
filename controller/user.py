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
        payload = []
        for user in users:
            content = {'id': user[0], 'username': user[1], 'email': user[2], 'statut': user[3], 'annee': user[4],
                       'created_at': user[5]}
            payload.append(content)
        return payload
    except Exception as e:
        return dbQueryError(e)


def findById(id=1):
    dbc = dbInstance.cursor()
    try:
        sql = dbc.execute("""SELECT * FROM user WHERE id = %s """, id)
        user = dbc.fetchall()
        content = {}
        for data in user:
            content = {'id': data[0], 'username': data[1], 'email': data[2], 'statut': data[3], 'annee': data[4],
                       'created_at': data[5]}
        return content
    except pymysql.Error as e:
        return dbQueryError(e)


def add(body):
    dbc = dbInstance.cursor()

    try:
        createdAt = time.strftime('%Y-%m-%d')
        values = (body["username"], body["email"], body["statut"], body["annee"], createdAt)
        sql = "INSERT INTO user (username, email, statut, annee, created_at) VALUES (%s, %s, %s, %s, %s)"
        dbc.execute(sql, values)
        dbInstance.commit()
        last_insert_id = dbc.lastrowid
        return {'id': last_insert_id, 'created_at': createdAt}
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
