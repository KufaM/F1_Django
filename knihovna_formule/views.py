from django.shortcuts import render
from .models import Driver, Team, Track, GrandPrix

def index(request):
    return render(request, 'html/index.html')

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'html/drivers.html', {'drivers': drivers})

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'html/teams.html', {'teams': teams})

def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'html/tracks.html', {'tracks': tracks})

def grand_prix_list(request):
    races = GrandPrix.objects.all()
    return render(request, 'html/grandprix.html', {'races': races})

def driver_list_grouped(request):
    teams = Team.objects.prefetch_related('driver_set').all()
    data = []
    for team in teams:
        drivers = list(team.driver_set.all())
        if drivers:
            data.append({'team': team, 'drivers': drivers})
    return render(request, 'html/driver_list_grouped.html', {'data': data})
