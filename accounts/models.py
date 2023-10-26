from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
  movie = models.AutoField(primary_key = True)
  title = models.CharField(max_length = 100)
  description = models.TextField()
  movie_poster=models.ImageField(upload_to='movies/poster', default="movies/poster/not.jpg")

  def __str__(self):
    return self.title


class Shows(models.Model):
  show = models.AutoField(primary_key = True)
  movie = models.ForeignKey('Movie', on_delete = models.CASCADE, related_name = 'movie_show')
  time = models.CharField(max_length = 100)
  date = models.CharField(max_length = 15, default = "")
  price = models.IntegerField()

  def __str__(self):
    return self.movie.title + " | " + self.time + " | " + self.date


class Bookings(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  show = models.ForeignKey(Shows, on_delete = models.CASCADE)
  seat = models.CharField(max_length = 100)

  @property
  def seat_list(self):
    return self.seat.split(',')
  def __str__(self):
    return self.user.username + " | " + self.show.movie.title + " | " + self.show.time + " | " + self.show.date + " | " + self.seat