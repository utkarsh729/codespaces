import os
import datetime
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/htop')
def htop():
   
    system_user = os.getenv('USER', 'codespace')


    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")

    try:
        htop_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout
    except Exception as e:
        htop_output = f"Error fetching top output: {str(e)}"

    return f"""
    <html>
    <head><title>System Info</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong>Utkarsh Singh</p>
        <p><strong>Username:</strong> {system_user}</p>
        <p><strong>Server Time (IST):</strong> {formatted_time}</p>
        <h2>Top Output:</h2>
        <pre>{htop_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
