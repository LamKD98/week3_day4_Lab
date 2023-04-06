from models.events import *
import datetime

event1 = Event(1,datetime.date(2023,4,6),"Comic Con", 500, 1, "Comic Convention")
event2 = Event(2,datetime.date(2023,12,5), "Winter Wonderland", 100, 2, "Christmas Market")
events = [event1,event2]

def add_new_event(event):
    events.append(event)

