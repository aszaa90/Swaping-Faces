from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hi everyone'
if __name__ == "__main__":
    app.run()