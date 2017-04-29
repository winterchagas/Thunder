import sqlite3
from flask_restful import Resource, reqparse
import uuid


class Company():
    TABLE_NAME = 'companies'

    def __init__(self, _id, name, email, phone, address, city, state):
        self.id = _id
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state


    @classmethod
    def find_by_company_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        if row:
            company = cls(*row)
        else:
            company = None

        connection.close()
        return company


    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            company = cls(*row)
        else:
            company = None

        connection.close()
        return company


class CompanyRegister(Resource):
    TABLE_NAME = 'companies'

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('email', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('phone', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('address', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('city', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('state', type=str, required=True, help="This field cannot be left blank!")

    def post(self):
        data = CompanyRegister.parser.parse_args()

        if Company.find_by_company_name(data['name']):
            return {"message": "Company with this name already exists."}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (?, ?, ?, ?, ?, ?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (uuid.uuid4().hex, data['name'], data['email'], data['phone'], data['address'], data['city'], data['state']))
        connection.commit()
        connection.close()

        return {"message": "Company created successfully."}, 201