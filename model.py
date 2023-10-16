from config import db,app

class UserInfo(db.Model):
    user_id  = db.Column('user_id',db.Integer,primary_key=True)
    firstname= db.Column('first_name',db.String(40))
    lastname = db.Column('last_name', db.String(40))
    email = db.Column('email', db.String(40))
    gender = db.Column('gender', db.String(40))
    username = db.Column('username', db.String(40))
    password = db.Column('password', db.String(255))

class Product(db.Model):
    prodid = db.Column('prod_id',db.Integer,primary_key=True)
    prodname = db.Column('prod_name',db.String(40))
    prodven = db.Column('prod_vendor', db.String(40))
    prodcat = db.Column('prod_category', db.String(40))
    proddesc = db.Column('prod_desc', db.String(40))
    prodqty = db.Column('prod_qty', db.Integer())
    prodbarcode = db.Column('prod_barcode', db.String(255))
    prodprice = db.Column('prod_price', db.Float())

with app.app_context():
    db.create_all() # create table