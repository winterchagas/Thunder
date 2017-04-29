from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
import sqlite3
from user import User


class FormList(Resource):
    TABLE_NAME = 'forms'

    parser = reqparse.RequestParser()

    parser.add_argument('id', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('completed_date', type=str, required=False, help="This field cannot be left blank!")
    parser.add_argument('violation_posted', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('postings_notices', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('occupancy_status', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('vacancy_posting_left', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('card_left', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('letter_delivered', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('submission_statement', type=str, required=False, help="This field cannot be left blank!")
    parser.add_argument('occupancy_verified_by', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('building_type', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('stories', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('construction_type', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('color', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('garage', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('additional_buildings', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('yard', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('roof', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('property_condition', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('property_damaged', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('property_value', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('for_sale', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('neighborhood_condition', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('how_many_sides', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('appear_vacant', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('safety_violations', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('presently_for_sale', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('typical_neighborhood', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('under_construction', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('roof_condition', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('windows_condition', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('finish_material', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('condition_finish_material', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('condition_foundation', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('condition_landscape', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('relation_to_properties', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('general_comments', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('external_factors', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('external_factors_comments', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('comments', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('six_damage', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('safety_issue', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('exterior_debris', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('lawn_maintenance', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('property_vacant', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('escalated_events', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('roof_damage', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('signs_vandalism', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('unsecured_openings', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('notice_posted', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('code_of_conduct', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('empty', type=str, required=True, help="This field cannot be left blank!")

    @jwt_required()
    def get(self):
        user_data = User.find_by_username(current_identity.username)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE user_id = '{id}'".format(table=self.TABLE_NAME, id=user_data.id)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'id': row[0], 'user_id': row[1], 'completed_date': row[2], 'violation_posted': row[3],
                          'postings_notices': row[4], 'occupancy_status': row[5], 'vacancy_posting_left': row[6],
                          'card_left': row[7], 'letter_delivered': row[8], 'submission_statement': row[9],
                          'occupancy_verified_by': row[10], 'building_type': row[11], 'stories': row[12],
                          'construction_type': row[13], 'color': row[14], 'garage': row[15],
                          'additional_buildings': row[16],
                          'yard': row[17], 'roof': row[18], 'property_condition': row[19], 'property_damaged': row[20],
                          'property_value': row[21], 'for_sale': row[22], 'neighborhood_condition': row[23],
                          'how_many_sides': row[24], 'appear_vacant': row[25], 'safety_violations': row[26],
                          'presently_for_sale': row[27], 'typical_neighborhood': row[28], 'under_construction': row[29],
                          'roof_condition': row[30], 'windows_condition': row[31], 'finish_material': row[32],
                          'condition_finish_material': row[33], 'condition_foundation': row[34],
                          'condition_landscape': row[35],
                          'relation_to_properties': row[36], 'general_comments': row[37],
                          'external_factors': row[38], 'external_factors_comments': row[39], 'comments': row[40],
                          'six_damage': row[41], 'safety_issue': row[42], 'exterior_debris': row[43],
                          'lawn_maintenance': row[44], 'property_vacant': row[45], 'escalated_events': row[46],
                          'roof_damage': row[47], 'signs_vandalism': row[48], 'unsecured_openings': row[49],
                          'notice_posted': row[50], 'code_of_conduct': row[51], 'empty': row[52]})
        connection.close()
        return {'items': items}


    @jwt_required()
    def put(self):
        data = FormList.parser.parse_args()
        updated_item = {'id': data['id'], 'violation_posted': data['violation_posted'],
                        'postings_notices': data['postings_notices'], 'occupancy_status': data['occupancy_status'],
                        'vacancy_posting_left': data['vacancy_posting_left'], 'card_left': data['card_left'],
                        'letter_delivered': data['letter_delivered'],
                        #'submission_statement': data['submission_statement'],
                        'occupancy_verified_by': data['occupancy_verified_by'], 'building_type': data['building_type'],
                        'stories': data['stories'], 'construction_type': data['construction_type'],
                        'color': data['color'], 'garage': data['garage'],
                        'additional_buildings': data['additional_buildings'], 'yard': data['yard'],
                        'roof': data['roof'], 'property_condition': data['property_condition'],
                        'property_damaged': data['property_damaged'], 'property_value': data['property_value'],
                        'for_sale': data['for_sale'], 'neighborhood_condition': data['neighborhood_condition'],
                        'how_many_sides': data['how_many_sides'], 'appear_vacant': data['appear_vacant'],
                        'safety_violations': data['safety_violations'], 'presently_for_sale': data['presently_for_sale'],
                        'typical_neighborhood': data['typical_neighborhood'], 'under_construction': data['under_construction'],
                        'roof_condition': data['roof_condition'], 'windows_condition': data['windows_condition'],
                        'finish_material': data['finish_material'], 'condition_finish_material': data['condition_finish_material'],
                        'condition_foundation': data['condition_foundation'], 'condition_landscape': data['condition_landscape'],
                        'relation_to_properties': data['relation_to_properties'], 'general_comments': data['general_comments'],
                        'external_factors': data['external_factors'], 'external_factors_comments': data['external_factors_comments'],
                        'comments': data['comments'], 'six_damage': data['six_damage'],
                        'safety_issue': data['safety_issue'], 'exterior_debris': data['exterior_debris'],
                        'lawn_maintenance': data['lawn_maintenance'], 'property_vacant': data['property_vacant'],
                        'escalated_events': data['escalated_events'], 'roof_damage': data['roof_damage'],
                        'signs_vandalism': data['signs_vandalism'], 'unsecured_openings': data['unsecured_openings'],
                        'notice_posted': data['notice_posted'], 'code_of_conduct': data['code_of_conduct'],
                        'empty': data['empty'] }
        try:
            Form.update(updated_item)
        except:
            return {"message": "An error occurred updating the form."}

        return {'message': '1 Form uploaded.'}


class Form(Resource):
    TABLE_NAME = 'forms'

    parser = reqparse.RequestParser()

    parser.add_argument('id', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('completed_date', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('violation_posted', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('postings_notices', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('occupancy_status', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('vacancy_posting_left', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('card_left', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('letter_delivered', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('submission_statement', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('occupancy_verified_by', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('building_type', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('stories', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('construction_type', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('color', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('garage', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('additional_buildings', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('yard', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('roof', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('property_condition', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('property_damaged', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('property_value', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('for_sale', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('neighborhood_condition', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('how_many_sides', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('appear_vacant', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('safety_violations', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('presently_for_sale', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('typical_neighborhood', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('under_construction', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('roof_condition', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('windows_condition', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('finish_material', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('condition_finish_material', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('condition_foundation', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('condition_landscape', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('relation_to_properties', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('general_comments', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('external_factors', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('external_factors_comments', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('comments', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('six_damage', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('safety_issue', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('exterior_debris', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('lawn_maintenance', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('property_vacant', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('escalated_events', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('roof_damage', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('signs_vandalism', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('unsecured_openings', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('notice_posted', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('code_of_conduct', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('empty', type=str, required=True, help="This field cannot be left blank!")

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE {table} SET violation_posted=?, postings_notices=?, occupancy_status =?, vacancy_posting_left =?, card_left =?, letter_delivered =?, occupancy_verified_by =?, building_type =?, stories =?, construction_type =?, color =?, garage =?, additional_buildings =?, yard =?, roof =?, property_condition =?, property_damaged =?, property_value =?, for_sale =?, neighborhood_condition =?, how_many_sides =?, appear_vacant =?, safety_violations =?, presently_for_sale =?, typical_neighborhood =?, under_construction =?, roof_condition =?, windows_condition =?, finish_material =?, condition_finish_material =?, condition_foundation =?, condition_landscape =?, relation_to_properties =?, general_comments =?, external_factors =?, external_factors_comments =?, comments =?, six_damage =?, safety_issue =?, exterior_debris =?, lawn_maintenance =?, property_vacant =?, escalated_events =?, roof_damage =?, signs_vandalism =?, unsecured_openings =?, notice_posted =?, code_of_conduct =?, empty =? WHERE id =?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['violation_posted'], item['postings_notices'], item['occupancy_status'],
                               item['vacancy_posting_left'], item['card_left'], item['letter_delivered'],
                               item['occupancy_verified_by'], item['building_type'], item['stories'],
                               item['construction_type'], item['color'], item['garage'], item['additional_buildings'],
                               item['yard'], item['roof'], item['property_condition'], item['property_damaged'],
                               item['property_value'], item['for_sale'], item['neighborhood_condition'],
                               item['how_many_sides'], item['appear_vacant'], item['safety_violations'],
                               item['presently_for_sale'], item['typical_neighborhood'], item['under_construction'],
                               item['roof_condition'], item['windows_condition'], item['finish_material'],
                               item['condition_finish_material'], item['condition_foundation'],
                               item['condition_landscape'], item['relation_to_properties'], item['general_comments'],
                               item['external_factors'], item['external_factors_comments'], item['comments'] ,
                               item['six_damage'], item['safety_issue'], item['exterior_debris'],
                               item['lawn_maintenance'], item['property_vacant'], item['escalated_events'],
                               item['roof_damage'], item['signs_vandalism'], item['unsecured_openings'],
                               item['notice_posted'], item['code_of_conduct'], item['empty'],
                               item['id']))
        connection.commit()
        connection.close()

    # @jwt_required()
    def get(self, id):
        item = self.find_by_id(id)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    def post(self):
        dic1 = {}
        Form.insert(dic1);

    # @jwt_required()
    def put(self, id):
        data = Form.parser.parse_args()
        item = self.find_by_id(id)
        # TAKE  USER AND COMPANY FROM HOUSE PASSED

        updated_item = {'company_id': comp_data.id, 'user_id': user_data.id, 'form_id': data['form_id'],
                        'address': data['address'], 'city': data['city'], 'state': data['state'],
                        'zip': data['zip'], 'county': data['county'], 'order_number': data['order_number'],
                        'work_code': data['work_code'], 'inspect_pay': data['inspect_pay'],
                        'start_date': data['start_date'], 'due_date': data['due_date'],
                        'ordered_date': data['ordered_date'], 'assigned_date': data['assigned_date'],
                        'completed_date': data['completed_date'], 'submitted_date': data['submitted_date'],
                        'follow_up_date': data['follow_up_date'], 'submitted_by': data['submitted_by'],
                        'owner': data['owner'], 'lender': data['lender'],
                        'vacant': data['vacant'], 'photo_required': data['photo_required'],
                        'instructions': data['instructions'], 'notes': data['notes'], 'latitude': data['latitude'],
                        'longitude': data['longitude'], 'status': data['status']}
        print('after updated item')
        if item is None:
            try:
                Form.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the form."}
        else:
            try:
                Form.update(updated_item)
            except:
                return {"message": "An error occurred updating the form."}
        return updated_item

    # @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': 'Item deleted'}

    # @classmethod
    # def find_by_id(cls, id):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #
    #     query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
    #     result = cursor.execute(query, (id,))
    #     row = result.fetchone()
    #     connection.close()
    #     if row:
    #         return {'house': {'id': row[0], 'address': row[1], 'city': row[2], 'state': row[3], 'zip': row[4],
    #                           'county': row[5], 'order_number': row[6], 'work_code': row[7], 'inspect_pay': row[8],
    #                           'start_date': row[9], 'due_date': row[10], 'ordered_date': row[11],
    #                           'assigned_date': row[12],
    #                           'completed_date': row[13], 'submitted_date': row[14], 'follow_up_date': row[15],
    #                           'submitted_by': row[16], 'inspector_id': row[17], 'owner': row[18], 'lender': row[19],
    #                           'vacant': row[20], 'photo_required': row[21], 'instructions': row[22], 'notes': row[23],
    #                           'latitude': row[24], 'longitude': row[25]}}

    # @classmethod
    # def insert(cls):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query = "INSERT INTO {table} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(
    #         table=cls.TABLE_NAME)
    #     cursor.execute(query, (
    #         data['house_id'], "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
    #         "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
    #         ""))
    #     connection.commit()
    #     connection.close()


    @classmethod
    def auto_insert(cls, data):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(
            table=cls.TABLE_NAME)
        cursor.execute(query, (
            data['house_id'], data['user_id'], "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "yes"))
        connection.commit()
        connection.close()



