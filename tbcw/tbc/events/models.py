from django.db import models
from comedians.models import RegisterComedian
# Create your models here.

class Event(models.Model):
    show_name = models.CharField(max_length = 100, blank = False)
    genre = models.CharField(max_length = 100, blank = False)
    language = models.CharField(max_length = 10, blank = True)
    duration = models.CharField(max_length = 20, blank = False)
    age_limit = models.CharField(max_length = 10, blank = True)
    date_time = models.DateTimeField(blank = False)
    #comedians = models.ForeignKey('comedians.RegisterComedian', on_delete = models.CASCADE)
    comedians = models.ManyToManyField(RegisterComedian)
    #bms_link = ??? see comment 4
