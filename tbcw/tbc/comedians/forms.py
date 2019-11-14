from django import forms
from .models import RegisterComedian


class YoutubeLinksWidget(forms.MultiWidget):
    def __init__(self, attrs = None):
        self.widgets = [
            forms.TextInput(),
            forms.TextInput(),
            forms.TextInput()
        ]
        super().__init__(self.widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(';')
        return ['', '', '']

class YoutubeLinksField(forms.MultiValueField):
    widget = YoutubeLinksWidget()

    def __init__(self, *args, **kwargs):
        self.url_fields = [
            forms.URLField(required = False),
            forms.URLField(required = False),
            forms.URLField(required = False)
        ]
        super().__init__(self.url_fields, *args, **kwargs, required = False)


    def compress(self, value):
        return ';'.join(value)



class RegisterComedianForm(forms.ModelForm):
    class Meta:
        model = RegisterComedian
        fields = ('firstname', 'lastname', 'about', 'email', 'phoneno',
                  'profile_pic', 'videos', 'fb_link', 'insta_link',
                  'twitter_link', 'youtube_link')
    videos = YoutubeLinksField()
