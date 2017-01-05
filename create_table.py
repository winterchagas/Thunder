import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS houses_completed (id INTEGER PRIMARY KEY, address text, city text, state text, zip int, county text, order_number text, work_code text, inspect_pay real, start_date text, due_date text, ordered_date text , assigned_date text, completed_date text, submitted_date text, follow_up_date text , submitted_by text, inspector_id int, owner text, lender text, vacant text, photo_required text, instructions text, notes text, latitude real, longitude real)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS houses_open (id INTEGER PRIMARY KEY, address text, city text, state text, zip int, county text, order_number text, work_code text, inspect_pay real, start_date text, due_date text, ordered_date text , assigned_date text, completed_date text, submitted_date text, follow_up_date text , submitted_by text, inspector_id int, owner text, lender text, vacant text, photo_required text, instructions text, notes text, latitude real, longitude real)"
cursor.execute(create_table)

connection.commit()

connection.close()