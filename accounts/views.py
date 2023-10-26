from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash
from . models import *

# Create your views here.

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Username or password is incorrect')
      return redirect('login')
  return render(request, 'login.html')


def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    if password1 == password2:
      if User.objects.filter(username = username).exists():
        messages.info(request, 'Username already exists')
      elif User.objects.filter(email = email).exists():
        messages.info(request, 'Email already exists')
      else:
        user = User.objects.create_user(username = username, first_name= first_name, last_name= last_name, email=email,password=password1)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')
    else:
      messages.info(request, 'Passwords do NOT match')
    return redirect('register')
  else:
    return render(request, "register.html")


def logout(request):
  auth.logout(request)
  return redirect('/')


def account(request):
  u = request.user
  if request.method == 'POST':
      username = request.POST['username']
      first_name = request.POST['fn']
      last_name = request.POST['ln']
      email = request.POST['email']
      old = request.POST['old']
      new = request.POST['new']
      user = User.objects.get(pk = u.pk)        

      if User.objects.filter(username=username).exclude(pk=u.pk).exists():
          messages.error(request,'Username already exists')

      elif User.objects.filter(email=email).exclude(pk=u.pk).exists():
              messages.error(request,'Email already exists')

      elif user.check_password(old):
          user.username = username
          user.first_name = first_name
          user.last_name = last_name
          user.email = email
          user.set_password(new)
          user.save()
          #update session
          update_session_auth_hash(request, user)

          messages.success(request,'Profile updated')
      else:
          messages.error(request,'Wrong Old Password')

      return redirect('profile')

  else:
      user = request.user
      return render(request,"profile.html")


def booking(request):
  user = request.user
  book = Bookings.object.filter(user = user.pk)
  return render(request, "bookings.html", {'book':book})


def movieIndex(request):
  user = request.user
  m = Shows.objects.filter.values('movie','movie__movie_name','movie__movie_poster').distinct()
  print(m)
  return render(request,"dashboard.html", {'list':m})


def new_show(request):
  user = request.user

  if request.method == 'POST':
      m = request.POST['m']
      t = request.POST['t']
      d = request.POST['d']
      p = request.POST['p']

      show = Shows(movie_id = m, date = d, time = t, price = p)
      show.save()
      messages.success(request,'Show Added')
      return redirect('add_shows')

  else:    
      m = Movie.objects.all()
      sh = Shows.objects.filter(cinema=user.cinema)
      data = {
          'mov':m,
          's':sh
      }
      return render(request,"add_shows.html", data)