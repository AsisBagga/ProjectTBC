from django.db import models
# Create your models here.

class RegisterComedian(models.Model):
    firstname = models.CharField(max_length = 20, blank = False)
    lastname = models.CharField(max_length = 20, blank = False)
    about = models.TextField(max_length = 200, blank = False)
    email = models.CharField(max_length = 200, blank = False)
    phoneno = models.CharField(max_length = 13, blank = False)
    profile_pic = models.ImageField(upload_to='profile_pic', blank = False)
    videos = models.URLField(blank = True, null = True)
    fb_link = models.URLField(blank = True)
    insta_link = models.URLField(blank = True)
    twitter_link = models.URLField(blank = True)
    youtube_link = models.URLField(blank = True)
    approved = models.BooleanField(blank = False, default = False)

    def get_all_objects(self):
        #queryset = self._meta.model.objects.all()
        #or
        queryset = self.__class__.objects.all()
        return queryset
