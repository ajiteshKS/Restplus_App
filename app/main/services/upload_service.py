import csv
import os
import zipfile
from datetime import datetime

import xlrd
from werkzeug.utils import secure_filename
from app import app


def save_file(file):
    result = {}
    if file.filename == "":
        error = "Please select a file"
        result['error'] = error
        return result

    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        fname = filename.rsplit('.')
        if fname[-1] == 'zip':
            result = files_in_zip(file)
            return result

        dt = int(datetime.now().timestamp())
        filename = fname[0] + "_" + str(dt) + "." + fname[-1]

        file.save(os.path.join(app.config["FILE_UPLOADS"], filename))

        location = app.config['FILE_UPLOADS'] + '/' + filename

        result['name'] = filename
        result['rows'] = number_of_rows(location)

        return result
    else:
        error = "Unsupported Extension type"
        result['error'] = error
        return result


def allowed_file(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False


def number_of_rows(location):
    if location.endswith('csv'):
        file = open(location)
        reader = csv.reader(file)
        lines = len(list(reader))
        return (lines - 1)

    elif location.endswith(('xls', 'xlsx')):
        workbook = xlrd.open_workbook(location)
        sheet = workbook.sheet_by_index(0)
        return (sheet.nrows - 1)


def files_in_zip(file):
    result = {}
    rows = {}
    zip = zipfile.ZipFile(file)
    i=0
    for zip_info in zip.infolist():
        if zip_info.filename[-1] == '/':
            continue
        if not allowed_file(zip_info.filename):
            continue
        i = i+1
        dt = int(datetime.now().timestamp())
        zip_info.filename = os.path.basename(zip_info.filename)
        name = zip_info.filename.rsplit('.')
        zip_info.filename = name[0] + "_" + str(dt) + "." + name[-1]
        zip.extract(zip_info, app.config['FILE_UPLOADS'])
        location = app.config['FILE_UPLOADS'] + "/" + zip_info.filename
        rows['name'] = zip_info.filename
        rows['rows'] = number_of_rows(location)
        result[i] = rows
    if not bool(result):
        result['error'] = 'Unsupported Extension types in zip'
    return result
