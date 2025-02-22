from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
   
    name = "Utkarsh Singh"  
    

    username = os.getenv('USER', 'codespace')  
    
    # Get IST Time
    utc_now = datetime.now(pytz.utc)
    ist = utc_now.astimezone(pytz.timezone('Asia/Kolkata'))
    server_time = ist.strftime('%Y-%m-%d %H:%M:%S %Z')
    
  
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True, timeout=5)
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"
    
    return f"""
    <html>
    <head><title>System Info</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
