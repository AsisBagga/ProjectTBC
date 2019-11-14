from django.shortcuts import render
from comedians.models import RegisterComedian
# Create your views here.

def manage(request):
    return render(request, 'manage/manage.html')


def host_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'manage/ack.html', {'form': form})

    else:
        form = EventForm()

    return render(request, 'manage/host_event.html', {'form': form})


def comedian_profile(request):
    comedian_profiles = RegisterComedian.objects.filter(approved=False).values('firstname', 'id')
    print(comedian_profiles)
    return render(request, 'manage/comedian_profile.html', {'comedian_profiles': comedian_profiles})

def fetch_comedian(request, pk):
    print(pk)
    comedian = RegisterComedian.objects.filter(id=pk).values('firstname', 'lastname', 'id')
    return render(request, 'manage/fetch_comedian.html', {'comedian': comedian})

def approve_comedian(request, pk):
    RegisterComedian.objects.filter(id=pk).update(approved='True')
    comedian_profiles = RegisterComedian.objects.filter(approved=False).values('firstname', 'id')
    print(comedian_profiles)
    return render(request, 'manage/comedian_profile.html', {'comedian_profiles': comedian_profiles})

def reject_comedian(request, pk):
    RegisterComedian.objects.filter(id=pk).delete()
    comedian_profiles = RegisterComedian.objects.filter(approved=False).values('firstname', 'id')
    print(comedian_profiles)
    return render(request, 'manage/comedian_profile.html', {'comedian_profiles': comedian_profiles})
