from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/db')
def db_info():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=os.environ.get('POSTGRES_DB', 'mydatabase'),
        user=os.environ.get('POSTGRES_USER', 'user'),
        password=os.environ.get('POSTGRES_PASSWORD', 'password'),
        host='db'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT version();')
    db_version = cursor.fetchone()
    cursor.close()
    conn.close()
    return f"PostgreSQL Version: {db_version[0]}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
