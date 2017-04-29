from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
import sqlite3
import uuid
from form import Form
from company import Company
from user import User
import json

HOUSE_ID = 0

class House(Resource):
    TABLE_NAME = 'houses'

    parser = reqparse.RequestParser()
    # parser.add_argument('id', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('address', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('city', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('state', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('zip', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('county', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('work_code', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('inspect_pay', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('start_date', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('due_date', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('ordered_date', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('assigned_date', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('completed_date', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('submitted_date', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('follow_up_date', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('submitted_by', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('owner', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('lender', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('vacant', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('photo_required', type=bool, required=True, help="This field cannot be left blank!")
    parser.add_argument('instructions', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('notes', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('latitude', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('longitude', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('status', type=str, required=True, help="This field cannot be left blank!")


    # @jwt_required()
    def get(self, id):
        item = self.find_by_id(id)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_address(cls, address):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE address=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (address,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'id': row[0]}}

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'house': {'id': row[0], 'address': row[1], 'city': row[2], 'state': row[3], 'zip': row[4],
                              'county': row[5], 'order_number': row[6], 'work_code': row[7], 'inspect_pay': row[8],
                              'start_date': row[9], 'due_date': row[10], 'ordered_date': row[11],
                              'assigned_date': row[12], 'completed_date': row[13], 'submitted_date': row[14],
                              'follow_up_date': row[15], 'submitted_by': row[16], 'inspector_id': row[17],
                              'owner': row[18], 'lender': row[19], 'vacant': row[20], 'photo_required': row[21],
                              'instructions': row[22], 'notes': row[23], 'latitude': row[24], 'longitude': row[25]}}

    def post(self, id):
        pass

    # @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': 'Item deleted'}

    @classmethod
    def insert(cls, data):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(
            table=cls.TABLE_NAME)
        print(query)
        cursor.execute(query, (
            data['house_id'], data['company_id'], data['user_id'], data['address'], data['city'],
            data['state'], data['zip'], data['county'], data['work_code'], data['inspect_pay'],
            data['start_date'], data['due_date'], data['ordered_date'], data['assigned_date'],
            data['completed_date'], data['submitted_date'], data['follow_up_date'],
            data['submitted_by'], data['owner'], data['lender'], data['vacant'],
            data['photo_required'], data['instructions'], data['notes'],
            data['latitude'], data['longitude'], data['status']))
        connection.commit()
        connection.close()

    @jwt_required()
    def put(self, id):
        data = House.parser.parse_args()
        item = self.find_by_id(id)
        user_data = User.find_by_username(current_identity.username)
        comp_data = Company.find_by_id(user_data.company_id)
        house_id = uuid.uuid4().hex
        form_data = {'house_id': house_id, "user_id": user_data.id}
        updated_item = {'house_id': house_id, 'company_id': comp_data.id, 'user_id': user_data.id,
                        'address': data['address'], 'city': data['city'], 'state': data['state'],
                        'zip': data['zip'], 'county': data['county'],
                        'work_code': data['work_code'], 'inspect_pay': data['inspect_pay'],
                        'start_date': data['start_date'], 'due_date': data['due_date'],
                        'ordered_date': data['ordered_date'], 'assigned_date': data['assigned_date'],
                        'completed_date': data['completed_date'], 'submitted_date': data['submitted_date'],
                        'follow_up_date': data['follow_up_date'], 'submitted_by': data['submitted_by'],
                        'owner': data['owner'], 'lender': data['lender'],
                        'vacant': data['vacant'], 'photo_required': data['photo_required'],
                        'instructions': data['instructions'], 'notes': data['notes'], 'latitude': data['latitude'],
                        'longitude': data['longitude'], 'status': data['status']}

        if item is None:
            try:
                House.insert(updated_item)
                Form.auto_insert(form_data)
            except:
                return {"message": "An error occurred inserting the house."}
        else:
            try:
                House.update(updated_item)
            except:
                return {"message": "An error occurred updating the house."}
        return updated_item


    @classmethod
    def update(cls, item):
        print('INSIDE UPDATE')
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE {table} SET completed_date=?, submitted_date=?, submitted_by=?, status=?  WHERE id=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['completed_date'], item['submitted_date'],
                               item['submitted_by'], item['status'] ,item['id']))
        print('AFTER QUERY')
        connection.commit()
        connection.close()


class HouseList(Resource):
    TABLE_NAME = 'houses'

    parser1 = reqparse.RequestParser()
    #parser1.add_argument('houses', type=str, required=True, help="This field cannot be left blank!")
    parser1.add_argument('id', type=str, required=True, help="This field cannot be left blank!")
    parser1.add_argument('completed_date', type=str, required=False, help="This field cannot be left blank!")
    parser1.add_argument('submitted_date', type=str, required=False, help="This field cannot be left blank!")
    parser1.add_argument('submitted_by', type=str, required=False, help="This field cannot be left blank!")
    parser1.add_argument('status', type=str, required=False, help="This field cannot be left blank!")


    @jwt_required()
    def get(self):
        user_data = User.find_by_username(current_identity.username)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE user_id = '{id}'".format(table=self.TABLE_NAME,id=user_data.id)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'id': row[0], 'company_id': row[1], 'user_id': row[2],
                          'address': row[3], 'city': row[4], 'state': row[5], 'zip': row[6], 'county': row[7],
                          'work_code': row[8], 'inspect_pay': row[9], 'start_date': row[10],
                          'due_date': row[11], 'ordered_date': row[12], 'assigned_date': row[13],
                          'completed_date': row[14],
                          'submitted_date': row[15], 'follow_up_date': row[16], 'submitted_by': row[17],
                          'owner': row[18], 'lender': row[19], 'vacant': row[20],
                          'photo_required': row[21], 'instructions': row[22], 'notes': row[23], 'latitude': row[24],
                          'longitude': row[25], 'status': row[26]})
        connection.close()
        return {'items': items}


    @jwt_required()
    def put(self):
        data = HouseList.parser1.parse_args()
        updated_item = {'id': data['id'], 'completed_date': data['completed_date'],
                    'submitted_date': data['submitted_date'],
                    'submitted_by': data['submitted_by'], 'status': data['status']}

        try:
            House.update(updated_item)
        except:
            return {"message": "An error occurred updating the house."}

        return {'message': '1 House uploaded.'}


    # @jwt_required()
    # def put(self):
    #     data = HouseList.parser1.parse_args()
    #     print (data['houses'])
    #     # for house in data:
    #     #     print (house)
    #     # updated_item = {'id': data['id'], 'completed_date': data['completed_date'],
    #     #             'submitted_date': data['submitted_date'],
    #     #             'submitted_by': data['submitted_by'], 'status': data['status']}
    #     #
    #     # try:
    #     #     House.update(updated_item)
    #     # except:
    #     #     return {"message": "An error occurred updating the house."}
    #
    #     return {'message': '1 House uploaded.'}