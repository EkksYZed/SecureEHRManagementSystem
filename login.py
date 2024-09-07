'''
CSCI 531 Final Project
Andrew Rodriguez
Aaron Lobo
'''

from flask import Flask, request, redirect, url_for, render_template, make_response, abort
import hashlib
from query import queryPatient,checkPatientAudit,addHealthRecord,deleteHealthRecord
from audit import addRecord


app = Flask(__name__)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = {
    "admin1": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
    "John Doe": "96d9632f363564cc3032521409cf22a852f2032eec099ed5967c0d000cec607a",
    "Bob Brown": "81b637d8fcd2c6da6359e6963113a1170de795e4b725b84d1e0b4cfd9ec58ce9",
    "Doctor": "72f4be89d6ebab1496e21e38bcd7c8ca0a68928af3081ad7dff87e772eb350c2",
    "Andrew Rodriguez": "d979885447a413abb6d606a5d0f45c3b7809e6fde2c83f0df3426f1fc9bfed97",
    "Aaron Lobo": "39fdbdb8ddf75a006ffec2a3ba95c3a04ce5517c608a786ef9a042af9843bd8c",
    "Carol Folt": "4c26d9074c27d89ede59270c0ac14b71e071b15239519f75474b2f3ba63481f5",
    "Clifford Neuman": "5359eec13763f1d5c49ee396739944e5bc4ca118ad681a0762f7da79e825edd6",
    "Omkar pot": "37028839aea3b5b27f75fafdcfda3915998d6535f598a16478b57f43f01d5c16",
    "Tanya Ryutov": "4ab17eebd8ab6696a0cc3ccd69e4aa2818911e5800b0ff335bf2fe6d2c11cd23",
    "Tommy Trojan": "044f4b3501cd8e8131d40c057893f4fdff66bf4032ecae159e0c892a28cf6c8e",
    "Zoe walberg": "9d017e2681b7f31725e1c0fbe2612e89079c22806b02cf7a894b500dd5a219c1"
}

admins = ["admin1"]
patients = ["John Doe","Bob Brown","Andrew Rodriguez","Aaron Lobo","Carol Folt","Clifford Neuman","Omkar pot","Tanya Ryutov","Tommy Trojan","Zoe walberg"]
doctors = ["Doctor"]

def is_authenticated(request):
    username = request.cookies.get('username')
    return username in users


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    hashed_input = hash_password(password)
    if username in users and users[username] == hashed_input:

        if username in admins:
            response = make_response(redirect(url_for('adminDashboard')))
            response.set_cookie('username', username, httponly=True, secure=True, samesite='Lax')
            return response
        elif username in patients:
            response = make_response(redirect(url_for('patientDashboard')))
            response.set_cookie('username', username, httponly=True, secure=True, samesite='Lax')
            return response
        elif username in doctors:
            response = make_response(redirect(url_for('doctorDashboard')))
            response.set_cookie('username', username, httponly=True, secure=True, samesite='Lax')
            return response
    return "Invalid credentials", 403


@app.route('/patientDashboard')
def patientDashboard():
    if not is_authenticated(request):
        return redirect(url_for('home'))
    return render_template('patientDashboard.html')

@app.route('/adminDashboard')
def adminDashboard():
    if not is_authenticated(request):
        return redirect(url_for('home'))
    return render_template('adminDashboard.html')

@app.route('/doctorDashboard')
def doctorDashboard():
    if not is_authenticated(request):
        return redirect(url_for('home'))
    return render_template('doctorDashboard.html')


@app.route('/adminQuery', methods=['POST'])
def adminQuery():
    if not is_authenticated(request):
        return redirect(url_for('home'))
    patient_name = request.form['patientName']
    user = request.cookies['username']


    patient_info = queryPatient(patient_name, user)
    patient_audit = checkPatientAudit(patient_name)

    return render_template('adminDashboard.html', patient_name=patient_name,patient_audit=patient_audit,patient_info=patient_info)

@app.route('/doctorQuery', methods=['POST'])
def doctorQuery():
    if not is_authenticated(request):
        return redirect(url_for('home'))
    patient_name = request.form['patientName']
    user = request.cookies['username']
    patient_info = queryPatient(patient_name, user)
    
    return render_template('doctorDashboard.html', patient_info=patient_info, patient_name=patient_name)


@app.route('/addComment', methods=['POST'])
def addComment():
    if not is_authenticated(request):
        return redirect(url_for('home'))
    comment = request.form['comment']
    patientName = request.form['patientName']
    user = request.cookies['username']
    commentStatus = addHealthRecord(patientName,user,comment)
    return render_template('doctorDashboard.html',comment_status=commentStatus)

@app.route('/deleteComment', methods=['POST'])
def deleteComment():
    if not is_authenticated(request):
        return redirect(url_for('home'))
    comment = request.form['comment']
    patientName = request.form['patientName']
    user = request.cookies['username']
    commentStatus = deleteHealthRecord(patientName,user,comment)
    return render_template('doctorDashboard.html',delete_status=commentStatus)





@app.route('/patientQuery', methods=['POST'])
def patientQuery():
    if not is_authenticated(request):
        return redirect(url_for('home'))
    user = request.cookies['username']
    patient_info = queryPatient(user, user)
    patient_audit = checkPatientAudit(user)

    return render_template('patientDashboard.html', patient_info=patient_info, patient_name=user, patient_audit=patient_audit)




@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('home')))
    response.delete_cookie('username')
    return response

if __name__ == '__main__':
   app.run(debug=True)
