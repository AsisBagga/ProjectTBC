from django.db import models

# Create your models here.

class Book(models.Model):
    firstname = models.CharField(max_length = 20, blank = False)
    lastname = models.CharField(max_length = 20, blank = False)
    companyname = models.CharField(max_length = 30, blank = False)
    email = models.EmailField(max_length = 20, blank = False)
    phoneno = models.CharField(max_length = 12, blank = False)
    venue = models.CharField(max_length = 30, blank = False)
    typeofevent = models.CharField(max_length = 20, blank = False)
    datetimestartofevent = models.DateTimeField(blank = False)
    datetimeendofevent = models.DateTimeField(blank = False)
    preflanguage = models.CharField(max_length = 10, blank = True, null = True)
    audiencecount = models.CharField(max_length = 10, blank = True, null = True)
    budget = models.CharField(max_length = 10, blank = True, null = True)
    otherinfo = models.CharField(max_length = 200, blank = True, null = True)
    comedians = models.CharField(max_length = 100, blank = True, null = True)

class Produce(models.Model):
    firstname = models.CharField(max_length = 20, blank = False)
    lastname = models.CharField(max_length = 20, blank = False)
    companyname = models.CharField(max_length = 30, blank = False)
    email = models.EmailField(max_length = 20, blank = False)
    phoneno = models.CharField(max_length = 12, blank = False)
    venue = models.CharField(max_length = 30, blank = False)
    typeofevent = models.CharField(max_length = 100, blank = False) #requirements of the event
    datetimestartofevent = models.DateTimeField(blank = False)
    datetimeendofevent = models.DateTimeField(blank = False)
    preflanguage = models.CharField(max_length = 10, blank = True, null = True)
    audiencecount = models.CharField(max_length = 10, blank = True, null = True)
    budget = models.CharField(max_length = 10, blank = True, null = True)
    otherinfo = models.CharField(max_length = 200, blank = True, null = True)
    comedians = models.CharField(max_length = 100, blank = True, null = True)
