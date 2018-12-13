from flask import Flask ,render_template,request,url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password/dbname'
db = SQLAlchemy(app)


class MovieData(db.Model):
	__tablename__ = 'data' 
	id = db.Column(db.Integer, primary_key = True)
	movie = db.Column(db.String(120),unique= True)
	director = db.Column(db.String(120),unique= True)
	year = db.Column(db.Integer)

	def __init__(self,id,movie,director,year):
		self.id = id
		self.movie = movie
		self.director = director
		self.year = year


@app.route('/')
def home():
	return render_template('movies.html')

@app.route('/success', methods=['POST'])
def movies():
	if request.method == 'POST':
		id = request.form['id']
		movie = request.form['movie']
		director = request.form['director']
		year = request.form['year']
		#print (id, movie, director, year)
		data = MovieData(id,movie,director,year)
		db.session.add(data)
		db.session.commit()
		return render_template('success.html')


if __name__ == '__main__':
	app.run(debug = True)
