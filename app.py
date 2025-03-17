from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your full name
    username = os.getenv("USER") or os.getenv("USERNAME")  # Get system username
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)  # Convert to IST
    top_output = subprocess.getoutput("top -b -n 1")  # Run 'top' command

    return f"""
    <h1>System Information</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
