from flask import Flask , request , render_template
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/newentry')
def site():
	return render_template('site.html')

@app.route('/details', methods=["POST","GET"])
def details():
	if request.method == "POST":
		try :
			name = request.form['name']
			url = request.form['url']

			with sql.connect('database.db') as conn:
				cur = conn.cursor()

				cur.execute("INSERT INTO company (name,url) VALUES (?,?)",(name,url))

				conn.commit()

				msg = "Record Saved"

		except :
			conn.rollback()
			msg = "Error in Insertion"

		finally :
                        return render_template("result.html",msg = msg)
                        conn.close()

@app.route('/list')
def list():
	conn = sql.connect("database.db")
	conn.row_factory = sql.Row 

	cur = conn.cursor()
	cur.execute("SELECT * FROM company")

	rows = cur.fetchall()
	return render_tempalte('list.html',rows = rows)



if __name__ == '__main__':
	app.run(debug  =True)


				


