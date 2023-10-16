from model import *
from flask import request,render_template

@app.route('/user/register',methods=['GET','POST'])
def user_register():
    message=''
    if request.method=='POST':
        formdata = request.form
        firstname = formdata.get('fname')
        lastname = formdata.get('lname')
        email = formdata.get('email')
        gender = formdata.get('gender')
        username = formdata.get('username')
        password = formdata.get('password')

        user = UserInfo(firstname = firstname,lastname= lastname,email = email,gender = gender,
                        username = username,password = password)
        db.session.add(user)
        db.session.commit()
        message="user Successfully Added"
    return render_template('user_registration.html',message=message)