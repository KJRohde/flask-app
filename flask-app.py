from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello World! Digital Ocean is awesome! It deployed this app automatically with my git push!"

if __name__ == "__main__":
	app.run()
