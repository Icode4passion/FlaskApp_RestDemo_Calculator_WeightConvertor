from flask import Flask , jsonify , make_response , abort, render_template , request

app = Flask(__name__)

movies = [
{
	'id' : 1,
	'title': 'Batman',
	'Author': 'Bob Kane',
	'Director' : 'Christopher'
},
{
	'id' : 2,
	'title': 'Superman',
	'Author': 'Jerry Siegel',
	'Director' : 'Richard Donner'
	
}]

@app.route('/movie/api/v1.0/movies',methods=['GET'])
def get_tasks():
	return jsonify({'movies':movies})


@app.route('/movie/api/v1.0/movies/<int:movie_id>',methods=['GET'])
def get_tasks_id(movie_id):
	movie = [movie for movie in movies if movie['id'] == movie_id]
	if len(movie) == 0 :
		abort(400)
	return jsonify({'movie': movie[0]})

@app.errorhandler(400)
def errorhandler(error):
	return make_response(jsonify({'error':'Not Found'}),404)
	#return render_template('home.html')

@app.route('/movie/api/v1.0/movies',methods=['POST'])
def create_tasks():
	if not request.json or not 'title' in request.json:
		abort(400)
	movie ={
			'id' : movies[-1]['id'] +1,
			'title' : request.json['title'],
			'Author' : request.json.get('Author', ''),
			'Director' : request.json.get('Director', ''),

	}
	movies.append(movie)
	return jsonify({'task':task}),201

	

if __name__ == '__main__':
	app.run(debug = True)
