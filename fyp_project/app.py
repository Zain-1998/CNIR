from flask import Flask,render_template,url_for,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from latest_nation import latest_nation_list
from latest_dawn import latest_dawn_list
from latest_pakistan_today import latest_pakToday_list
from latest_daily_pakistan import latest_dailyPak_list
from latest_tribune import latest_tribune_list

from nation_sports import nation_sports_list
from nation_business import nation_business_list
from nation_entertainment import nation_entertainment_list
from nation_pakistan import nation_pakistan_list    
from dailyPak_sports import dailyPak_sports_list
from dailyPak_business import dailyPak_business_list
from dailyPak_entertainment import dailyPak_entertainment_list
from dailyPak_pakistan import dailyPak_pakistan_list
from dawn_sports import dawn_sports_list
from dawn_business import dawn_business_list
from dawn_entertainment import dawn_entertainment_list
from dawn_pakistan import dawn_pakistan_list
from pakToday_sports import pakToday_sports_list
from pakToday_business import pakToday_business_list
from pakToday_entertainment import pakToday_entertainment_list
from pakToday_pakistan import pakToday_pakistan_list
from tribune_sports import tribune_sports_list
from tribune_bussines import tribune_bussiness_list
from tribune_entertainment import tribune_entertainment_list
from tribune_pakistan import tribune_pakistan_list

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
        return render_template('user_index.html',accounts=account)
    else:
        return redirect(url_for("signin"))
@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    if request.method == 'POST' and "id" in session:
        u_id=session["id"]
        get_value=request.form.getlist('checkbox')
        if get_value:
            delete_interest=user_interest.query.filter_by(user_id=u_id).all()
            try:
                for interests in delete_interest:
                    db.session.delete(interests)
                    db.session.commit()
            except:
                return "There was an issue deleting interest"
            for i in get_value:
                add_interest=user_interest(interest_name=i,user_id=u_id)
                try:
                    db.session.add(add_interest)
                    db.session.commit()
                except:
                    return "problem saving"+get_value[i]
            return redirect('/dashboard')
        else:
            delete_interest=user_interest.query.filter_by(user_id=u_id).all()
            try:
                for interests in delete_interest:
                    db.session.delete(interests)
                    db.session.commit()
                return redirect('/dashboard')
            except:
                return "There was an issue deleting history"
    if "id" in session:
        get_id=session["id"]
        keywords=search_history.query.filter_by(user_id=get_id).all()
        get_interests=user_interest.query.filter_by(user_id=get_id).all()
        sports=False
        entertainment=False
        pakistan=False
        business=False
        for i in get_interests:
            if i.interest_name == "sports":
                sports=True
            if i.interest_name == "entertainment":
                entertainment=True
            if i.interest_name == "pakistan":
                pakistan=True
            if i.interest_name == "business":
                business=True
        return render_template('dashboard.html',
        keywords=keywords,sports=sports,entertainment=entertainment,
        business=business,pakistan=pakistan)
    else:
        return redirect(url_for("signin"))
@app.route('/newsfeed')
def newsfeed():
    if "id" in session:
        get_id=session["id"]
        get_interests=user_interest.query.filter_by(user_id=get_id).all()
        sports=False
        entertainment=False
        pakistan=False
        business=False
        for i in get_interests:
            if i.interest_name == "sports":
                sports=True
            if i.interest_name == "entertainment":
                entertainment=True
            if i.interest_name == "pakistan":   
                pakistan=True
            if i.interest_name == "business":
                business=True
        return render_template('newsfeed.html',
        sports=sports,entertainment=entertainment,business=business,pakistan=pakistan,
        get_nation_business_list=nation_business_list,
        get_nation_entertainment_list=nation_entertainment_list,
        get_nation_pakistan_list=nation_pakistan_list,get_nation_sports_list=nation_sports_list,
        get_pakToday_business_list=pakToday_business_list,
        get_pakToday_entertainment_list=pakToday_entertainment_list,
        get_pakToday_pakistan_list=pakToday_pakistan_list,
        get_pakToday_sports_list=pakToday_sports_list,
        get_dawn_business_list=dawn_business_list,
        get_dawn_entertainment_list=dawn_entertainment_list,
        get_dawn_pakistan_list=dawn_pakistan_list,get_dawn_sports_list=dawn_sports_list,
        get_dailyPak_business_list=dailyPak_business_list,
        get_dailyPak_entertainment_list=dailyPak_entertainment_list,
        get_dailyPak_pakistan_list=dailyPak_pakistan_list,
        get_dailyPak_sports_list=dailyPak_sports_list,
        get_tribune_bussiness_list=tribune_bussiness_list,
        get_tribune_entertainment_list=tribune_entertainment_list,
        get_tribune_pakistan_list=tribune_pakistan_list,
        get_tribune_sports_list=tribune_sports_list)
    else:
        return redirect(url_for("signin"))
@app.route('/latest-news')
def latest_news():
    return render_template('latest_news.html',
    get_latest_nation_list=latest_nation_list,get_latest_dailyPak_list=latest_dailyPak_list,
    get_latest_dawn_list=latest_dawn_list,get_latest_pakToday_list=latest_pakToday_list,
    get_latest_tribune_list=latest_tribune_list)
@app.route('/signin',methods=['POST','GET'])
def signin():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        account=user_account.query.filter_by(user_email=email,
        user_password=password).first()
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
        add_user=user_account(user_firstname=first_name,user_lastname=last_name,
        user_email=email,user_password=password)
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