from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base


# Init app
app = Flask(__name__)

# Init db
db = SQLAlchemy(app)
# employee = db.Table('employee', db.metadata, autoload=True, autoload_with=db.engine)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ajitesh1234@localhost/test'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from sqlalchemy.ext.automap import automap_base

def model_build(table_name):

    metadata = MetaData()

    # we can reflect it ourselves from a database, using options
    # such as 'only' to limit what tables we look at...
    metadata.reflect(db.engine, only=[table_name])
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)

    table = Base.classes.users
    return table



@app.route('/')
def hello():
    table = model_build('users')
    result = db.session.query(table).limit(2).offset(2).all()
    print(result)
    print("\n\n")

    return jsonify({"city":'hello'})


if __name__ == '__main__':
    app.run(debug=True)
