from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('show_name', 'genre', 'language', 'duration',
                  'age_limit', 'date_time', 'comedians')

    
