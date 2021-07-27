from flask_restplus import reqparse
from werkzeug.datastructures import FileStorage

from app.restplus import api

# To upload a file
upload_parser = api.parser()
upload_parser.add_argument('upld_file', location='files',
                           type=FileStorage, required=True ,help='File to be Analysed')

