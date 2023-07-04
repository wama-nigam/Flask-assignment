from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/studentform"
db = SQLAlchemy(app)

class Details(db.Model):

    roll_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone_num = db.Column(db.String,nullable=False)
    email = db.Column(db.String, nullable=False)
    college = db.Column(db.String, nullable=False)
    branch = db.Column(db.String, nullable=False)
    cgpa = db.Column(db.String, nullable=False)



@app.route("/",methods = ['GET' ,'POST'])
def home():
    if (request.method == 'POST'):
        roll_no = request.form.get('rollno')
        name = request.form.get('name')
        phone_num = request.form.get('phoneno')
        email = request.form.get('email')
        college = request.form.get('college')
        branch = request.form.get('branch')
        cgpa = request.form.get('cgpa')
        entry = Details(roll_no=roll_no,name=name, phone_num=phone_num,email=email, college=college, branch=branch,cgpa=cgpa)

        db.session.add(entry)
        db.session.commit()
    return render_template("index.html")


@app.route("/about", methods = ['GET'])
def about():
    post_route = Details.query.all()
    return render_template("about.html",post=post_route)
app.run(debug=True)