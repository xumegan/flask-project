from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
  data=request.form
  print(data)
  return render_template("login.html",boolean=True)

@auth.route('/logout')
def logout():
  return "<p>Logout</p>"

@auth.route('/signUp',methods=['GET', 'POST'])
def signUp():
  if request.method == 'POST':
    email = request.form.get('email')
    firstname = request.form.get('firstname')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    if len(email)<4:
      flash('email wrong',category='error')
    elif len (firstname)<2:
      flash('firstname wrong',category='error')
    elif password1 !=password2:
      flash('password wrong',category='error')
    elif len (password1)<7:
      flash('password wrong',category='error')
    else:
      flash('created',category='success')
  
  return render_template("signUp.html")

