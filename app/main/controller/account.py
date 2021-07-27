from flask import request, render_template, session, url_for, make_response, g
from flask_restplus import Resource
from werkzeug.utils import redirect
from flask_socketio import emit
from app.restplus import api
from app.main.services import account_service as acc_service
from app.main.models.user import User
from app import init_db
import time

ac = api.namespace('account', description='Operations related to account')


@ac.route('/signup')
class SignUp(Resource):

    def get(self):
        error = None
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('signup.html', error=error), 200, headers)

    def post(self):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        bio = request.form['bio']

        acc_service.add_new_user(username, password, email, bio)
        acc_service.add_in_redis(username)
        return redirect(url_for('account_home'))


@ac.route('/login')
class loginn(Resource):

    def get(self):
        error = None
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html', error=error), 200, headers)

    def post(self):
        username = request.form['username']
        password = request.form['password']

        error = acc_service.authenticate_user(username, password)
        if error == None:
            acc_service.add_in_redis(username)
            return redirect(url_for('account_home'))

        else:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('login.html', error=error), 200, headers)



@ac.route('/logout')
class logoutt(Resource):
    def get(self):
        acc_service.remove_from_redis(session['session_id'])
        return redirect(url_for('account_loginn'))


@ac.route('/')
class home(Resource):
    def get(self):
        if not session:
            return redirect(url_for('account_loginn'))
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html', username=session['username']), 200, headers)

@ac.route('/view')
class view(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('details.html'), 200, headers)

    def post(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('details.html'), 200, headers)


@ac.route('/details')
class Details(Resource):
    def get(self):
        if not session:
            return redirect(url_for('account_loginn'))
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('details.html'))

