from django import forms
from .models import Book, Produce


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('firstname','lastname','companyname','email','phoneno',
                  'venue','typeofevent','datetimestartofevent','datetimeendofevent',
                  'preflanguage','audiencecount','budget','otherinfo','comedians')


class ProduceForm(forms.ModelForm):
    class Meta:
        model = Produce
        fields = ('firstname','lastname','companyname','email','phoneno',
                  'venue','typeofevent','datetimestartofevent','datetimeendofevent',
                  'preflanguage','audiencecount','budget','otherinfo','comedians')
