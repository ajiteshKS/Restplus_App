import json
from io import BytesIO
import os
from werkzeug.datastructures import FileStorage


#Positive Test
def test_uploadfile_api(flask_app_client):
    stored_file = os.path.join("D:/Ud.zip")

    my_file = FileStorage(
        stream=open(stored_file, "rb"),
        filename="Ud.zip",  content_type="zip",
    )

    data = {
        'upld_file': my_file
    }

    response = flask_app_client.post('/upload-file',
                         content_type='multipart/form-data',
                         data=data, follow_redirects=True)

    assert response.get_json()['1']['rows'] == 6
    assert response.status_code == 200


#Negative Test
# Passing zip that do not contain any allowed extension files
def test_uploadfile_api_with_notAllowedExtensions(flask_app_client):
    stored_file = os.path.join("D:/jar_files.zip")

    my_file = FileStorage(
        stream=open(stored_file, "rb"),
        filename="jar_files.zip",  content_type="zip",
    )

    data = {
        'upld_file': my_file
    }

    response = flask_app_client.post('/upload-file',
                         content_type='multipart/form-data',
                         data=data, follow_redirects=True)

    assert response.status_code == 415
    assert response.get_json() == None



