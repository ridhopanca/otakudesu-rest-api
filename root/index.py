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

@app.route("/ongoing")
def get_ongoing():
	controller = Main()
	route = controller.ongoing()
	return route

@app.route("/ongoing/page/<number>")
def get_ongoing_pagination(number):
	controller = Main()
	route = controller.ongoingWithPagination(number)
	return route

@app.route("/genres")
def get_genres():
	controller = Main()
	route = controller.genres()
	return route

@app.route("/genre/<id>/page/<number>")
def get_anime_by_genre(id,number):
	controller = Main()
	route = controller.animeByGenre(id, number)
	return route

@app.route("/schedule")
def get_schedule():
	controller = Main()
	route = controller.schedule()
	return route

if __name__ == '__main__':
	app.run()
	