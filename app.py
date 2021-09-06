import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app=Flask(__name__)
api=Api(app)

@app.route('/')
def hello():
    return "Welcome Your BOT, It has Successfully BORN OUT ! "

cred=credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred,{
    'databaseURL':'https://faculties-aa703-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref=db.reference('/')
ref.set({
    'fac':
    {
        'A':{
            'name':'A',
            'age':24,
            'mobile':123456789,
            'cabin':'G-118'
        },

        'B':{
            'name':'B',
            'age':20,
            'mobile':889955320,
            'cabin':'G-120'
        }
    }
})

#update
# upd=db.reference('fac')
# fac_upd=upd.child('B')
# fac_upd.update({
#     'age'
# })

#to get data
# data = db.reference("/fac/A/")
# fac_a=data.get()
# print(fac_a["age"])

con_put_args=reqparse.RequestParser()
con_put_args.add_argument("name",type=str,help="contact of the fac")
con_put_args.add_argument("age",type=int,help="contact of the fac")

# name=input('enter the fac name')
class contact(Resource):
    def get(self,name):
        data = db.reference("/fac/"+name+"/")
        fac_a=data.get()
        return fac_a

# data = db.reference("/fac/"+name+"/")
# fac_a=data.get()
# print(fac_a)

api.add_resource(contact, "/contact/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
