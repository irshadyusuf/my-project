from django.shortcuts import render

# Create your views here.


def doctorHome(request):
    return render(request, 'doctor_templates/home.html')


def doctorLogin(request):
    return render(request, 'doctor_templates/login.html')