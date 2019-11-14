from django.shortcuts import render, redirect
from .forms import RegisterComedianForm
from .models import RegisterComedian
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from .serializers import ComedianSerializer
import requests, json, base64
from django.core.files import File
# Create your views here.

def register_comedians(request):
    form = RegisterComedianForm(request.POST, request.FILES)
    imagec = RegisterComedianForm(request.FILES)
    print("Initial form captured")

    print("Register Commedians before if")
    if request.method == 'POST':
        print("It is inside POST")
        if form.is_valid():
            print(form.cleaned_data)
            print('\n')
            print(form.cleaned_data['profile_pic'])
            print("Creating session variable")
            
            process_image(request.FILES['profile_pic'], form)

            str_form = json.dumps(form.cleaned_data)

            request.session['comedian_form'] = str_form
            print("End of Register Comedian function")
            return render(request, 'comedians/preview_profile.html', {'form': form})
    else:
        print("Register Comedians ELSE")
        form = RegisterComedianForm()
        return render(request, 'comedians/register_comedians.html', {'form': form})

def process_image(profile_pic, form):
    print(type(form.cleaned_data['profile_pic']))
    image_read = profile_pic.read()
    form.cleaned_data['profile_pic'] = str(base64.encodestring(image_read))
    print(type(form.cleaned_data['profile_pic']))

def preview_profile(request):
    print("Inside preview profile")
    dict_form = request.session.get('comedian_form')
    form = json.loads(dict_form)
    fnp = "profile_pics/" + form['firstname']
    fn = form['firstname']

    print(type(form['profile_pic']))

    #profile_pict = eval(form['profile_pic'])
    image_write = base64.decodestring(eval(form['profile_pic']))
    form_profile = open("{% static fnp %}", 'wb')
    form_profile.write(image_write)


    print("Form from register comedians - profile picture ")
    print(type(form['profile_pic']))
    print(type(form))


    r = RegisterComedian.objects.create(**form)
    with open("{% static fnp %}", 'rb') as f:
        image = File(f)
        r.profile_pic.save(fn+".png", image , save = True)

    r_details = r.__dict__

    email_from = settings.EMAIL_HOST_USER
    email_to = r.email
    email_admin = settings.EMAIL_ADMIN

    content = {"%s: %s" % (key,value) for (key, value) in r_details.items()}
    content = "\n".join(content)
    print("\n")

    message1 = ('Thank you for your interest!', 'We will get back to you.', email_from, [email_to])
    message2 = ('New comedian registration', content , email_from, [email_admin])
    #send_mass_mail((message1, message2), fail_silently=False)
    print("Email sent!")
    return render(request, 'comedians/thankyou.html', {'form': form})


def view_comedians(request):
    all_comedians = RegisterComedian.objects.filter(approved=True).values()
    print(all_comedians)
    disp = RegisterComedian.objects.filter(id=34).values('profile_pic')
    # Need to write specific for loops depending on what kind of data we want to display
    # See comments.txt for more details - point 3

    return render(request, 'comedians/view_comedians.html',{'all_comedians': all_comedians, 'disp' : disp})
