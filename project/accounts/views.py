from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile, Clinic
from .forms import Login_Form
from django.contrib.auth import authenticate,login
# Create your views here.


def doctors_list(request):
    doctors = Profile.objects.all()
    context = {"doctors": doctors}
    return render(request, 'user/doctors_list.html', context)


def doctor_detail(request, slug):
    doctor = Profile.objects.get(slug=slug)
    img = Clinic.objects.filter(namedoc=doctor)
    context = {"doctor": doctor, "img": img}
    return render(request, 'user/doctor_detail.html', context)


def login_user(request):
    if request.method == "POST":
        login_form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("accounts:doctors_list")
    else:
        login_form = Login_Form()

    return render(request, "user/login.html",
                  {'login_form': login_form
    })
