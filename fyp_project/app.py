from flask import Flask,render_template,url_for,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from the_news import  news_list
from pakistan_today import news_list_1
# import sports

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///databases/user_databases/cnir.db'
app.secret_key="cnirsecretkeyforsesstion"
db=SQLAlchemy(app)
class search_history(db.Model):
    search_id=db.Column(db.Integer,primary_key=True)
    search_keywords=db.Column(db.String(200),nullable=False)
    search_datetime=db.Column(db.DateTime,default=datetime.now)
    user_id=db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return '<search_row %r>' % self.search_id
class user_account(db.Model):
    user_id=db.Column(db.Integer,primary_key=True)
    user_firstname=db.Column(db.String(200),nullable=False)
    user_lastname=db.Column(db.String(200),nullable=False)
    user_email=db.Column(db.String(200),nullable=False,unique=True)
    user_password=db.Column(db.String(200),nullable=False)
    def __repr__(self):
        return '<user_row %r>' % self.user_id
class user_interest(db.Model):
    interest_id=db.Column(db.Integer,primary_key=True)
    interest_name=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return '<interest_row %r>' % self.interest_id

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        search_keyword=request.form['searchbar']
        try:
            return redirect('/')
        except:
            return 'There was an issue searching your News.'
    elif "id" in session:
        return redirect(url_for("user_index"))
    else:
        return render_template('index.html')
        # return render_template('index.html',latest_news_thenews=news_list,latest_news_pakistantoday=news_list_1,accounts=account)
@app.route('/user-index',methods=['POST','GET'])
def user_index():
    if request.method=='POST' and "id" in session:
        get_keywords=request.form['searchbar']
        get_id=session["id"]
        add_search=search_history(search_keywords=get_keywords,user_id=get_id)
        try:
            db.session.add(add_search)
            db.session.commit()
            return redirect('/user-index')
        except:
            return 'There was an issue searching your News.'
    elif "user" in session:
        account=session["user"]
        # return render_template('user_index.html',accounts=account)
        return render_template('user_index.html',latest_news_thenews=news_list,latest_news_pakistantoday=news_list_1,accounts=account)
    else:
        return redirect(url_for("signin"))
@app.route('/dashboard')
def dashboard():
    if "id" in session:
        get_id=session["id"]
        keywords=search_history.query.filter_by(user_id=get_id).all()
        return render_template('dashboard.html',keywords=keywords)
    else:
        return redirect(url_for("signin"))
@app.route('/newsfeed')
def newsfeed():
    if "id" in session:
        return render_template('newsfeed.html')
        # return render_template('newsfeed.html',sports_news=sports.finallist)
    else:
        return redirect(url_for("signin"))
@app.route('/signin',methods=['POST','GET'])
def signin():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        account=user_account.query.filter_by(user_email=email,user_password=password).first()
        if account:
            session["user"]=account.user_firstname
            session["id"]=account.user_id
            return redirect('/user-index')
    else:
        return render_template('signin.html')
@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        password=request.form['password']
        add_user=user_account(user_firstname=first_name,user_lastname=last_name,user_email=email,user_password=password)
        try:
            db.session.add(add_user)
            db.session.commit()
            return redirect('/signin')
        except:
            return 'Account already exists.'
    else:
        return render_template('signup.html')
@app.route('/signout')
def signout():
    if "user" in session and "id" in session:
        session.pop("user",None)
        session.pop("id",None)
        return redirect(url_for("index"))
@app.route('/change-name',methods=['POST','GET'])
def change_name():
    if request.method == 'POST':
        get_id=session["id"]
        get_fname=request.form['first_name']
        get_lname=request.form['last_name']
        user=user_account.query.filter_by(user_id=get_id).first()
        user.user_firstname=get_fname
        user.user_lastname=get_lname
        try:
            db.session.commit()
            session["user"]=user.user_firstname
            return redirect('/change-name')
        except:
            return "There was an issue updating data"
    if "id" in session:
        return render_template('change_name.html')
    else:
        return redirect(url_for("signin"))
@app.route('/change-password',methods=['POST','GET'])
def change_password():
    if request.method == 'POST':
        get_id=session["id"]
        get_password=request.form['old_password']
        get_new_password=request.form['new_password']
        get_confirm_password=request.form['confirm_new_password']
        user=user_account.query.filter_by(user_id=get_id).first()
        if user.user_password==get_password:
            user.user_password=get_confirm_password
            try:
                db.session.commit()
                return redirect('/change-password')
            except:
                return "There was an issue updating password"
        else:
            return "Your current password is incorrect"
    if "id" in session:
        return render_template('change_password.html')
    else:
        return redirect(url_for("signin"))
@app.route('/delete-account')
def delete_account():
    if "user" in session and "id" in session:
        get_id=session["id"]
        delete_user=user_account.query.filter_by(user_id=get_id).first()
        delete_user_history=search_history.query.filter_by(user_id=get_id).all()
        try:
            db.session.delete(delete_user)
            for users in delete_user_history:
                db.session.delete(users)
            db.session.commit()
            session.pop("user",None)
            session.pop("id",None)
            return redirect(url_for("signin"))
        except:
            return "There was an issue deleting history"
    else:
        return redirect(url_for("signin"))
@app.route('/clear')
def clear():
    if "user" in session and "id" in session:
        get_id=session["id"]
        delete_user_history=search_history.query.filter_by(user_id=get_id).all()
        try:
            for users in delete_user_history:
                db.session.delete(users)
            db.session.commit()
            return redirect('/dashboard')
        except:
            return "There was an issue deleting history"
    else:
        return redirect(url_for("signin"))
if __name__ == "__main__":
    app.run(debug=True)