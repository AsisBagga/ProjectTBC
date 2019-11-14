from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Produce
from .forms import BookForm, ProduceForm
from django.views.generic import CreateView
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def base(request):
    return render(request, 'base.html')

def book(request):
    if request.method == "POST":
        b_details = []
        form = BookForm(request.POST)
        if form.is_valid():
            b = form.save()
            #b_details = b.__dict__

            new_request = str(Book.objects.filter(id=b.id).values())

            email_from = settings.EMAIL_HOST_USER
            email_to = b.email
            email_admin = settings.EMAIL_ADMIN

            # turn the dict into a set of strings
            #content = {"%s: %s" % (key, value) for (key, value) in b_details.items()}
            # turn those strings into 1 block of text separated by newlines
            #content = "\n".join(content)

            message1 = ('Thank you for your interest!', 'We will review the details and get back to you', email_from, [email_to])
            message2 = ('New booking request', new_request , email_from, [email_admin])
            send_mass_mail((message1, message2), fail_silently=False)

            return render(request, 'enquiry/thankyou.html', {'b': b})
    else:
        form = BookForm()

    return render(request, 'enquiry/enquiry_book.html', {'form': form})

def produce(request):
    if request.method == "POST":
        p_details = []
        form = ProduceForm(request.POST)
        if form.is_valid():
            p = form.save()
            #p_details = p.__dict__
            #print(p.id)
            new_request = str(Produce.objects.filter(id=p.id).values())

            email_from = settings.EMAIL_HOST_USER
            email_to = p.email
            email_admin = settings.EMAIL_ADMIN

            # turn the dict into a set of strings
            #content = {"%s: %s" % (key, value) for (key, value) in p_details.items()}
            # turn those strings into 1 block of text separated by newlines
            #content = "\n".join(content)

            message1 = ('Thank you for your interest!', 'We will review the details and get back to you', email_from, [email_to])
            message2 = ('New booking request', new_request , email_from, [email_admin])
            send_mass_mail((message1, message2), fail_silently=False)

            return render(request, 'enquiry/thankyou.html')
    else:
        form = ProduceForm()

    return render(request, 'enquiry/enquiry_produce.html', {'form': form})

def thankyou(request):
    return render(request, 'enquiry/thankyou.html')

#class BookCreateView(CreateView):
#    model = Book
#    fields = "__all__"
