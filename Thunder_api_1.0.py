from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from house import House, HouseList
from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'winter'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(House, '/house/<string:id>')
api.add_resource(HouseList, '/houselist')
api.add_resource(UserRegister, '/register')

#@app.route('/')
#def hello_world():
#    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True