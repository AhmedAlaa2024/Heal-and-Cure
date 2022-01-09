from flask import render_template,Blueprint,request
signupPage=Blueprint("SignUp",__name__)

@signupPage.route('/signup', methods=['GET'])
def signup():
    if request.method == 'GET':
        return render_template("SignUp.html")
        # try:
        #   return render_template("SignUP.html")
        # except:
        #    return 500
