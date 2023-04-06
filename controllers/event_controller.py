from app import app
from flask import render_template, request
from models.event_list import events, add_new_event
from models.events import Event

@app.route('/events')

def all_tasks():
    return render_template('index.html',event_list=events)

@app.route('/events',methods=['POST'])
def add_task():
    event_date = request.form ['date']
    event_name = request.form['name']
    event_no_of_guests = request.form['number_of_guests']
    event_room = request.form['room']
    event_description = request.form['description']
    new_id = len(events) +1
    new_event = Event(new_id,event_date, event_name, event_no_of_guests, event_room, event_description)
    add_new_event(new_event)

    return render_template('index.html',event_list=events)