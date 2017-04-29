from flask import Flask
from flask_jwt import  JWT
from flask_restful import Api

from house import House, HouseList
from form import Form, FormList
from security import authenticate, identity
from user import UserRegister
from company import CompanyRegister

app = Flask(__name__)
app.secret_key = 'winter'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(House, '/house/<string:id>')
api.add_resource(HouseList, '/house_list')
api.add_resource(UserRegister, '/register_user')
api.add_resource(CompanyRegister, '/register_company')
api.add_resource(Form, '/form')
api.add_resource(FormList, '/form_list')

@app.route('/orders')
def hello_world():
    return 'List of the orders.'

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True