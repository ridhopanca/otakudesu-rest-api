from flask import Flask
from root.model.main import Main
from root.model.anime import Anime

app = Flask(__name__)

@app.route("/")
def welcome():
	return "Welcome to unofficial otakudesu-rest-api"

@app.route("/home")
def get_home():
	controller = Main()
	result = controller.home()
	return result

@app.route("/complete")
def get_complete():
	controller = Main()
	result = controller.completed()
	return result

@app.route("/complete/page/<number>")
def get_complete_pagination(number):
	controller = Main()
	result = controller.completedWithPagination(number)
	return result

@app.route("/ongoing")
def get_ongoing():
	controller = Main()
	result = controller.ongoing()
	return result

@app.route("/ongoing/page/<number>")
def get_ongoing_pagination(number):
	controller = Main()
	result = controller.ongoingWithPagination(number)
	return result

@app.route("/genres")
def get_genres():
	controller = Main()
	result = controller.genres()
	return result

@app.route("/genre/<id>/page/<number>")
def get_anime_by_genre(id,number):
	controller = Main()
	result = controller.animeByGenre(id, number)
	return result

@app.route("/schedule")
def get_schedule():
	controller = Main()
	result = controller.schedule()
	return result
@app.route("/search/<query>")
def get_search(query):
	controller = Main()
	result = controller.search(query)
	return result

@app.route("/anime/<id>")
def get_anime(id):
	controller = Anime()
	result = controller.anime(id)
	return result

if __name__ == '__main__':
	app.run()
	