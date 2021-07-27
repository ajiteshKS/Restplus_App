from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base


def model_build(table_name):

    metadata = MetaData()

    # we can reflect it ourselves from a database, using options
    # such as 'only' to limit what tables we look at...
    metadata.reflect(db.engine, only=['table_name'])
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)

    table = Base.classes.table_name
    return table

#
# class CitySchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = City