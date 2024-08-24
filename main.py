from flask import Flask, redirect, session, render_template, request, abort
from zenora import APIClient
from dotenv import load_dotenv
import os
from servers import Servers
from check_user import check

load_dotenv()

TOKEN = os.getenv("DCTOKEN")
SECRET = os.getenv("DCSECRET")
CLIENT_ID = os.getenv("CLIENT_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")
OAUTH_URL = f"https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify+email"

client = APIClient(TOKEN, client_secret=SECRET, validate_token=False)

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()

password = os.getenv("RCON_PASSWORD")

@app.route("/")
def index():
    if "token" in session:
        bearer_client = APIClient(session.get("token"), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template("index.html", user=current_user.username)
    return redirect("/login")

#登入
@app.route("/login")
def login():
    if OAUTH_URL is None:
        return redirect("/")
    return redirect(OAUTH_URL)

@app.route("/oauth/callback")
def callback():
    if "code" in request.args:
        code = request.args["code"]
        access_token = client.oauth.get_access_token(code, REDIRECT_URI).access_token
        bearer_client = APIClient(access_token, bearer=True)
        current_user = bearer_client.users.get_current_user()
        session["token"] = access_token
        session.permanent = True
        
    return redirect("/")

#Rcon
@app.route("/rcon/<server>")
def rcon(server:str):
    if "token" in session:
        bearer_client = APIClient(session.get("token"), bearer=True)
        current_user = bearer_client.users.get_current_user()
        if not check(current_user.username):
            abort(403)
        if server in Servers:
            return render_template("rcon.html", user=current_user.username, server=server)
        else:
            abort(404)
    return redirect("/login")

@app.route("/send/<server>/<command>")
def send_command(server:str, command:str):
    if "token" in session:
        bearer_client = APIClient(session.get("token"), bearer=True)
        current_user = bearer_client.users.get_current_user()
        if check(current_user.username):
            if server not in Servers:
                return "Server not found"
            return Servers[server].send(command)
        else:
            abort(403)
    else:
        abort(403)

#錯誤處理
@app.errorhandler(403)
def error403():
    return "403 Error"

@app.errorhandler(404)
def error404():
    return "404 Error"

#登出
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

app.run(host="127.0.0.1", port=80, debug=True)