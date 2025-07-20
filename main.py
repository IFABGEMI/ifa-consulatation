from flask import Flask, send_from_directory
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Formspree now handles form submissions directly

@app.route('/about.html')
def about():
    return send_from_directory('.', 'about.html')

@app.route('/merci.html')
def merci():
    return send_from_directory('.', 'merci.html')

@app.route('/logo.png')
def logo():
    return send_from_directory('.', 'logo.png')

@app.route('/new-logo.jpg')
def new_logo():
    return send_from_directory('.', 'new-logo.jpg')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
