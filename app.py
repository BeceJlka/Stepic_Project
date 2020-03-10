from flask import Flask, render_template, request
import json
from data import teachers, goals, days
import random
import pprint
app = Flask(__name__)
with open('teachers.json', "w") as file_write:
    json.dump(teachers, file_write)
with open("teachers.json", "r") as f:
    teachers = json.load(f)

@app.route('/')
def main():
    random_teacher = []
    for i in range(6):
        a = random.randint(1, 11)
        random_teacher.append(a)
    pprint.pprint(teachers)
    return render_template('index.html',teacher = teachers, random = random_teacher)


@app.route('/goals/<goal>/')
def render_goals(goal):
    return render_template('goal.html')

@app.route('/all_profiles/')
def render_all_profile():
    return render_template('all_profile.html',teacher = teachers)


@app.route('/profiles/<int:id>/')
def render_profile(id):
    return render_template('profile.html', teacher=teachers, goals=goals, id=id, days = days)


@app.route('/request/')
def render_request():
    return render_template('request.html', teacher=teachers)


@app.route('/request_done/')
def render_request_done():
    return render_template('request_done.html')


@app.route('/booking/<int:id>/<day>/<time>/')
def rander_booking(id, day, time):
    return render_template('booking.html',teacher=teachers, id=id, day = day, time = time, days = days)


@app.route('/booking_done/', methods=['POST'])
def rander_booking_done():
    booking = dict.fromkeys(['cteacher', 'day', 'time', 'username', 'phone'])
    cteacher = request.form.get("clientTeacher")
    booking['cteacher'].append(cteacher)
    day = request.form.get("clientWeekday")
    booking['day'].append(day)
    time = request.form.get("clientTime")
    booking['time'].append(time)
    username = request.form.get("clientName")
    booking['username'].append(username)
    phone = request.form.get("clientPhone")
    booking['phone'].append(phone)
    with open('booking.json', "w") as f_write:
        json.dump(booking,f_write)
    print(booking)
    return render_template('booking_done.html', username=username, phone=phone, day=day, time=time, days=days, teacher=teachers, id=cteacher)


app.run()
