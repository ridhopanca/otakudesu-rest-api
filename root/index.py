from flask import Flask
from root.model.main import Main
app = Flask(__name__)

@app.route("/home")
def get_home():
	controller = Main()
	route = controller.home()
	return route

@app.route("/complete")
def get_complete():
	controller = Main()
	route = controller.completed()
	return route

@app.route("/complete/page/<number>")
def get_complete_pagination(number):
	controller = Main()
	route = controller.completedWithPagination(number)
	return route

	