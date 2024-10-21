from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = input("Please enter a number")
	y = input("Please enter another number")
	return "The sum of the numbers you entered is " + str(x + y)

if __name__ == "__main__":
	app.run()
