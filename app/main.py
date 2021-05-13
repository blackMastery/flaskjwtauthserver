from flask import Flask
from jose import jwt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/<email>')
def index(email):
  payload = {'iss': 'my_jitsi_app_id',
   'context':{
     'email': email
   }, 
  'sub': 'nexusu-jitsi.v75inc.dev',
  'aud':'jitsi',
  'moderator': True, 'room':'*'}
  token = jwt.encode(payload, 'my_jitsi_app_secret', algorithm='HS256')

  return token
