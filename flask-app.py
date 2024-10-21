from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = input("Please enter a number")
	y = input("Please enter another number")
	added = x + y
	return ("The sum of the numbers you entered is " str(added))

if __name__ == "__main__":
	app.run()
