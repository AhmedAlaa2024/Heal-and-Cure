from flask import render_template,Blueprint,request
from werkzeug.utils import redirect
signupPage=Blueprint("SignUp",__name__)

@signupPage.route('/signup', methods=['GET'])
def signup():
    if request.method == 'GET':
        return render_template("SignUp.html")
    else:
        return redirect('/error')
