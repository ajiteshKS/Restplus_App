from flask import request, render_template, jsonify, make_response
from flask_restplus import Resource

from app.main.parsers import upload_parser
from app.main.services import upload_service
from app.restplus import api

up = api.namespace('upload-file', description='Operations related upload ')


@up.route("")
class UploadFile(Resource):

    def get(self):
        '''Input csv/excel/zip files through html template'''
        error = None
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('upload_file.html', error=error), 200, headers)

    @api.expect(upload_parser)
    def post(self):
        '''Calculate number of rows in csv/excel/zip files'''
        if request.files:
            file = request.files["upld_file"]
            result = upload_service.save_file(file)

            if 'error' in result:
                headers = {'Content-Type': 'text/html'}
                return make_response(render_template('upload_file.html', error=result['error']), 415, headers)
            else:
                return result
