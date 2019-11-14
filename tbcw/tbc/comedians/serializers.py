from rest_framework import serializers
from comedians.models import RegisterComedian

class ComedianSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterComedian
        fields = ('firstname', 'lastname', 'about', 'email', 'phoneno',
                  'profile_pic', 'videos', 'fb_link', 'insta_link',
                  'twitter_link', 'youtube_link')
