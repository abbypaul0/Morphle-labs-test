from flask import Flask
from datetime import datetime
import os
import subprocess
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to the Flask App! Go to <a href='/system-info'>/system-info</a> for system info.</h1>"

@app.route('/system-info')  # Change the route to /system-info
def system_info():
    # Name
    name = "Abhishek Paul"
    
    # Username (System User)
    username = os.getlogin()
    
    # Server Time (IST)
    tz = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # TOP output
    top_output = subprocess.getoutput('top -b -n 1')
    
    # Create response HTML
    response = f"""
    <h1>Name: {name}</h1>
    <p>User: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <h2>TOP output:</h2>
    <pre>{top_output.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
