import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import current_identity, jwt_required
import uuid
from company import Company


class User():
    TABLE_NAME = 'users'

    def __init__(self, _id, company_id, username, password, permission, first_name, last_name):
        self.id = _id
        self.username = username
        self.password = password
        self.company_id = company_id
        self.permission = permission
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username = ?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('password', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('permission', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('company', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('first_name', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('last_name', type=str, required=True, help="This field cannot be left blank!")

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        comp_data = Company.find_by_company_name(data['company'])
        if comp_data:

            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "INSERT INTO {table} VALUES (?, ?, ?, ?, ?, ?, ?)".format(table=self.TABLE_NAME)
            cursor.execute(query, (uuid.uuid4().hex ,comp_data.id, data['username'], data['password'],
                                   data['permission'], data['first_name'], data['last_name']))

            connection.commit()
            connection.close()

            return {"message": "User created successfully."}, 201

        else:
            return {"message": "No company with this name."}, 400

    @jwt_required()
    def get(self):
        firstLastName = User.find_by_username(current_identity.username)
        items = {"username": "", "first_name": "", "last_name": "", "user_id": ""}
        items["username"] = current_identity.username
        items["first_name"] = firstLastName.first_name
        items["last_name"] = firstLastName.last_name
        items["user_id"] = firstLastName.id
        return items