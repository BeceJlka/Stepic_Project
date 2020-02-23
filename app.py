from flask import Flask, render_template
from data import *
import random
app = Flask(__name__)
random_tour = []
search_tours = []
for key, value in tours.items():
    search_tours.append(value)
for i in range(6):
    a = random.randint(1, 16)
    random_tour.append(a)

@app.route('/')
def main():
    return render_template('index.html', about_tour=tours, logo=description, random_tours = random_tour,
                           lst_departures=list_departures, info_tour=search_tours, about_departures=departures)


@app.route('/departure/<departure>')
def render_departure(departure):
    return render_template('departure.html', logo=description, title=subtitle,
                           info_deature=search_tours, about_departures=departures,
                           about_tour=tours, info_tour=search_tours, d=departure)


@app.route('/tour/<id>')
def tour(id):
    return render_template('tour.html', about_tour=tours[int(id)], about_departures=departures,
                           info_tour=search_tours)


app.run()
