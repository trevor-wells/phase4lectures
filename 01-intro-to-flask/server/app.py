#!/usr/bin/env python3

########## Step 1.  Navigate to `models.py` ##########

############### Step 2. Set Up Imports ###############

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from models import db, Production

############# Step 3. Initialize the App ##############

app = Flask(__name__)

    # Configure the database
    # ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'`
    # ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False` 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

 ################## Step 4. Migrate ###################

migrate = Migrate(app, db)
db.init_app(app)

# pipenv install
# pipenv shell
# cd server (module that you'll work in)
# export FLASK_APP=app.py
# export FLASK_RUN_PORT = 5555
# flask db init
# flask db revision --autogenerate -m 'create productions table'
# flask db upgrade

############# 5.  Navigate to `seed.rb` ##############

################## Step  6. Routes ###################
@app.before_request
def runs_before():
    current_user = {"user.id": 1, "username":"rose"}
    print(current_user)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/image')
def image():
    return '<img src="https://thumbs.dreamstime.com/b/happy-handsome-man-giving-thumbs-up-smiling-double-hand-gesture-wearing-brown-shirt-white-background-36564655.jpg" />'

##### 7. Run the server ####################
# with `flask run` and verify your route in the browser at `http://localhost:5000/`

# 8. ✅ Create a dynamic route
@app.route('/productions/<string:title>')
def production(title):
    production = Production.query.filter(Production.title == title).first()
    production_response = {
        "title": production.title,
        "genre": production.genre,
        "director": production.director,
        "description": production.description,
        "image": production.image,
        "budget": production.budget,
        "ongoing": production.ongoing
    }
    response = make_response(
        jsonify(production_response),
        200
    )
    return response


# 9.✅ Update the route to find a `production` by its `title` and send it to our browser
    
@app.route('/context')
def context():
    import ipdb
    ipdb.set_trace()


# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
