import oauth as oauth ,google,token
from flask import Flask, render_template, jsonify, request, url_for,session
from authlib.integrations.flask_client import OAuth
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.secret_key = '1hkrEaXJb57ayNgCQaMJwifU'

oauth = OAuth(app)
google = oauth.register(
    name = 'google',
    client_id= "418138573664-4bpktf1fjnuojm37cqe6bfapk7lb6ss3.apps.googleusercontent.com",
    token_uri= "https://oauth2.googleapis.com/token",
    access_token_params=None,
    authorize_url= "https://accounts.google.com/o/oauth2/auth",
    oauth_params = None,
    project_id ="conecta-nu",
    auth_provider_x509_cert_url ="https://www.googleapis.com/oauth2/v1/certs",
    client_secret="1hkrEaXJb57ayNgCQaMJwifU",
    redirect_uris=["http://localhost:5000/login", "http://localhost:5000/authorize"],
    client_kwargs={'scope': 'openid profile email'},

)



@app.route('/')
def hello():
    email= (session).get('email', None)
    return f'hello {email}'



@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_url = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_url)


@app.route('/authorize', methods =["GET"])
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_ifo = resp.json()
    session['email'] = user_ifo['email']
    return redirect('/')


if __name__ == "__main__":
    app.run()