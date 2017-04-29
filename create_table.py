import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, company_id TEXT, username text, password text, permission int, first_name text, last_name text, FOREIGN KEY(company_id) REFERENCES companies(id))"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS houses (id TEXT PRIMARY KEY, company_id TEXT, user_id TEXT, address text, city text, state text, zip int, county text, work_code text, inspect_pay real, start_date text, due_date text, ordered_date text , assigned_date text, completed_date text, submitted_date text, follow_up_date text , submitted_by text, owner text, lender text, vacant text, photo_required text, instructions text, notes text, latitude real, longitude real, status text, FOREIGN KEY(company_id) REFERENCES companies(id), FOREIGN KEY(user_id) REFERENCES users(id))"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS companies (id TEXT PRIMARY KEY, name text, email text, phone int, address text, city text, state text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS forms (id TEXT PRIMARY KEY, user_id TEXT, completed_date text, violation_posted text, postings_notices text, occupancy_status text, vacancy_posting_left text, card_left text, letter_delivered text, submission_statement text, occupancy_verified_by text, building_type text, stories text , construction_type text, color text, garage text , additional_buildings text, yard text, roof text, property_condition text, property_damaged text, property_value text, for_sale text, neighborhood_condition text, how_many_sides text, appear_vacant text, safety_violations text, presently_for_sale text, typical_neighborhood text, under_construction text, roof_condition text, windows_condition text, finish_material text, condition_finish_material text, condition_foundation text, condition_landscape text, relation_to_properties text, general_comments text, external_factors text, external_factors_comments text, comments text, six_damage text, safety_issue text, exterior_debris text, lawn_maintenance text, property_vacant text, escalated_events text, roof_damage text, signs_vandalism text, unsecured_openings text, notice_posted text, code_of_conduct text, empty text, FOREIGN KEY(user_id) REFERENCES users(id))"
cursor.execute(create_table)

connection.commit()

connection.close()