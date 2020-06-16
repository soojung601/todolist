import sqlite3


conn = sqlite3.connect('/Users/soochungsohn/Documents/todolist/templates/todolist.db', isolation_level=None, check_same_thread=False)
cursor = conn.cursor()
def make_table(username):
    create_text = f"CREATE TABLE IF NOT EXISTS {username}(id INTEGER PRIMARY KEY,list text)"
    cursor.execute(create_text)

def make_list(username, text):
    added_text = f"INSERT INTO {username} ('list') VALUES('{text}')"
    cursor.execute(added_text)

def del_list(username, text):
    del_text = f"DELETE FROM {username} WHERE list = '{text}'"
    cursor.execute(del_text)

def get_list(username):
    cursor.execute(f"select list from {username}")
    todolist = cursor.fetchall()
    return todolist

def reset_list(username):
    cursor.execute(f"delete from {username}")



