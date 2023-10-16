from model import *
from flask import request,render_template

@app.route('/',methods=['GET','POST'])
def user_login():
    message=''
    if request.method=='POST':
        formdata = request.form
        username = formdata.get('username')
        password = formdata.get('password')
        if username and password:
            record = UserInfo.query.filter(UserInfo.username==username,UserInfo.password==password).first()

            if record:
                return render_template('home.html',message='Welcome {}'.format(username))
            else:
                message = "Invalid"

        else:
            message = 'username and password can not blank'

    return render_template('login.html',message=message)


