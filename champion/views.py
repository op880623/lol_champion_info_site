from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import datetime

from .models import Champion

def champion(request):
    return render(request, 'champion/base.html')


# two functions below send data to the page.
def all_data(request):
    champions = Champion.objects.all()
    champions_json_data = []
    for champion in champions:
        champions_json_data.append(champion.to_json())
    return HttpResponse('{"data": [' + ', '.join(champions_json_data) + ']}')

def reccent_update_champion(request):
    champions = Champion.objects.filter(update_date__gte=timezone.now()-datetime.timedelta(days=7))
    champions_json_data = []
    for champion in champions:
        champions_json_data.append(champion.to_json())
    return HttpResponse('{"data": [' + ', '.join(champions_json_data) + ']}')
