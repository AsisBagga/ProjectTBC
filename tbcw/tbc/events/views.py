from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event
from django.db.models import Q
from comedians.models import RegisterComedian

# Create your views here.

def view_events(request):
    events = Event.objects.values() # Returns all events
    eventsobj = Event.objects.all() # Returns all event objects

    for i in eventsobj:
        comediansobj = i.comedians.all() #gives all the comedians
    print(comediansobj)
    for i in comediansobj:
        print(i.firstname + ' ' + i.lastname) #To get each comedians details

    print("\n")
    print("\n")
    print("\n")

    someevent = Event.objects.filter(Q(show_name__icontains="Show A")) # Returns a specific event based on our search
    print("Event Show A: ")
    print(someevent)
    for i in someevent:
        somecomedian = i.comedians.all() # Returns the comedian/s associated with that event
    print("Comedians for Show A : ")
    for i in somecomedian:
        print(i.firstname + ' ' + i.lastname + '\n')

    return render(request, 'events/view_events.html', {'events': events, 'eventsobj': eventsobj})
