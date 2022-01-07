from flask import render_template,Blueprint,request
signupPage=Blueprint("SignUp",__name__)

@signupPage.route('/signup/<int:error>', methods=['GET'])
def signup(error):
    if request.method == 'GET':
        try:
            return render_template("SignUP.html",Error=error)
        except:
            return 500
