from flask import render_template,Blueprint,request
signupPage=Blueprint("SignUp",__name__)

@signupPage.route('/signup', methods=['GET'])
def signup():
    if request.method == 'GET':
        try:
            return render_template("SignUP.html")
        except:
            return 500
