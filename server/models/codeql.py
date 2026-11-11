import sqlite3

def get_user(user_input):
    conn = sqlite3.connect("db.sqlite")
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return conn.execute(query)
