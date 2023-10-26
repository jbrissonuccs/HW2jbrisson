from django.shortcuts import render
from accounts.models import *
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
  movies = Movie.objects.all()
  context = {
    'mov': movies
  }
  return render(request,"index.html", context)


def movies(request, id):
  movies = Movie.objects.get(movie=id)
  show = Shows.objects.filter(movie=id)
  context = {
    'movies': movies,
    'show': show
  }
  return render(request, "movies.html", context)

def seat(request, id):
  show = Shows.objects.get(shows=id)
  seat = Bookings.objects.filter(shows=id)
  return render(request,"seat.html", {'show':show, 'seat':seat})    

def booked(request):
  if request.method == 'POST':
    user = request.user
    seat = ','.join(request.POST.getlist('check'))
    show = request.POST['show']
    book = Bookings(seat=seat, show_id=show, user=user)
    book.save()
    return render(request,"booked.html", {'book':book})    

def ticket(request, id):
  ticket = Bookings.objects.get(id=id)
  print(ticket.shows.price)
  return render(request,"ticket.html", {'ticket':ticket})