from flask import Flask ,render_template , request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('speed.html')

@app.route("/",methods=["POST"])
def speed_calc():
	distance = request.form['distance']
	seconds = request.form['seconds']
	speed = int(distance) * int(seconds)
	sp =  str (speed)
	return render_template('speed_result.html', sp=sp)

@app.route("/cal_weight")
def weight_cal():
	return render_template('weight_cal.html')










if __name__ == '__main__':
	app.run(debug=True)



