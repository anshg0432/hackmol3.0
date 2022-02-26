from django.shortcuts import render


def start(request):
    return render(request, 'clubs/start.html')


def home(request):
    return render(request, 'clubs/home.html')


def clubs(request):
    return render(request, 'clubs/my_clubs.html')


def explore(request):
    return render(request, 'clubs/explore.html')