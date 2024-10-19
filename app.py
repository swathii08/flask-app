from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    system_username = os.getlogin()

    # Get server time in IST
    ist_timezone = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist_timezone).strftime('%Y-%m-%d %H:%M:%S')

    # Get top command output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    return f'''
    <h1>System Info</h1>
    <p>Name: Swathi</p>
    <p>Username: {system_username}</p>
    <p>Server Time (IST): {server_time}</p>
    <pre>{top_output}</pre>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
