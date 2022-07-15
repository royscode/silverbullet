from omdbapi.movie_search import GetMovie
movie = GetMovie(api_key='56e4fde2')

def get_movie_deets_from_api(movieName):
	res = movie.get_movie(title=movieName.title(), plot='full')
	return res