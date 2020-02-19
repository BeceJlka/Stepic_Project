from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/departure/<departure>')
def render_departure(departure):
    return render_template('departure.html')


@app.route('/tour/<id>')
def tour(id):
    return render_template('tour.html')


app.run()
