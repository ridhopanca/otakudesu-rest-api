from flask import Flask, Blueprint
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from root.model.main import Main
from root.model.anime import Anime

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
bp = Blueprint("API",__name__,url_prefix="/api")
#   main controller
@bp.route("/")
def welcome():
	return "Welcome to unofficial otakudesu-rest-api"

@bp.route("/home")
def get_home():
	controller = Main()
	result = controller.home()
	return result

@bp.route("/complete")
def get_complete():
	controller = Main()
	result = controller.completed()
	return result

@bp.route("/complete/page/<number>")
def get_complete_pagination(number):
	controller = Main()
	result = controller.completedWithPagination(number)
	return result

@bp.route("/ongoing")
def get_ongoing():
	controller = Main()
	result = controller.ongoing()
	return result

@bp.route("/ongoing/page/<number>")
def get_ongoing_pagination(number):
	controller = Main()
	result = controller.ongoingWithPagination(number)
	return result

@bp.route("/genres")
def get_genres():
	controller = Main()
	result = controller.genres()
	return result

@bp.route("/genre/<id>/page/<number>")
def get_anime_by_genre(id,number):
	controller = Main()
	result = controller.animeByGenre(id, number)
	return result

@bp.route("/schedule")
def get_schedule():
	controller = Main()
	result = controller.schedule()
	return result

@bp.route("/search/<query>")
def get_search(query):
	controller = Main()
	result = controller.search(query)
	return result

# end main controller

# anime detail controller
@bp.route("/anime/<id>")
def get_anime(id):
	controller = Anime()
	result = controller.anime(id)
	return result


@bp.route("/episode/<id>", defaults={"stream": None})
@bp.route("/episode/<id>/<stream>")
def get_episode(id, stream):
	controller = Anime()
	result = controller.episode(id, stream, bcrypt)
	return result

@bp.route("/batch/<id>")
def get_batch(id):
	controller = Anime()
	result = controller.batch(id)
	return result

@bp.route("/random")
def get_random():
	controller = Anime()
	result = controller.random()
	return result

# end anime detail controller
app.register_blueprint(bp)
if __name__ == "__main__":
	app.run()
	