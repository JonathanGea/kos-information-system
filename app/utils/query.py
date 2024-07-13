from app import app
import psycopg2
from app.utils.credentials import *


def get_database_connection():
    conn = psycopg2.connect(
        host=HOST,
        database=DATABSE,
        user=USER_POSTGRES_DB,
        password=PASSWORD_POSTGRES_DB
    )
    return conn

def execute_query(query, parameters=None):
    conn = get_database_connection()
    cur = conn.cursor()
    success = True
    try:
        if parameters:
            cur.execute(query, parameters)
        else:
            cur.execute(query)
        conn.commit()
    except Exception as e:
        print(f"Error executing query: {e}")
        conn.rollback()
        success = False
    finally:
        cur.close()
        conn.close()

    return success

def execute_queryWithReturn(query, parameters=None):
    conn = get_database_connection()
    cur = conn.cursor()
    data = ""
    try:
        if parameters:
            cur.execute(query, parameters)
        else:
            cur.execute(query)
        data = cur.fetchone()[0] 
        print("data :", data)
        conn.commit()
    except Exception as e:
        print(f"Error executing query: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
    return data

def fetches_query(query, parametereters=None):
    conn = get_database_connection()
    cur = conn.cursor()

    try:
        if parametereters:
            cur.execute(query, parametereters)
        else:
            cur.execute(query)

        data = cur.fetchall()
    except Exception as e:
        print(f"Error executing query: {e}")
        data = None
    finally:
        cur.close()
        conn.close()

    return data


def fetch_query(query, parametereters=None):
    conn = get_database_connection()
    cur = conn.cursor()

    try:
        if parametereters:
            cur.execute(query, parametereters)
        else:
            cur.execute(query)

        data = cur.fetchone()
    except Exception as e:
        print(f"Error executing query: {e}")
        data = None
    finally:
        cur.close()
        conn.close()

    return data